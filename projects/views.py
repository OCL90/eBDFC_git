from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Sum
import requests
from .models import Bol, Stage, Well, sandType, Pad
from .forms import BolForm, SandTypeForm, PadForm, StageForm, WellForm


def projects(request):
    pad = Pad.objects.filter(working_status=True)
    sand_types = sandType.objects.all()
    all_bols = Bol.objects.all()
    stage_number = Stage.objects.all()
    well = Well.objects.all()
    # print('Current Stage: ', stage_number)
    # print('Current Well: ', well)
    # print('**********')
    # complete = Pumped.objects.get(complete=True)
    # print('Complete Stage: ', complete.stage.stage_number)
    # print('Complete Well: ', complete.well.id)



    # if request.method == 'POST':
        # sand_box_map = []
        # box_sand_map = request.POST.get('sand_map_box')
        # if Bol.objects.filter(box_number_1 = box_sand_map):
        #     a = box_sand_map
        #     sand_box_map.append(a)
        #     print("im in box 1: ", sand_box_map)
        # elif Bol.objects.filter(box_number_2 = box_sand_map):
        #     b = box_sand_map
        #     sand_box_map.append(b)
        #     print("im in box 2: ", sand_box_map)
        # else:
        #     print("Box does not exist!")
        # return redirect("home")

    if request.method == 'POST':
        sand_map_box = request.POST.get('sand_map_box')

        try:
            sand_box = Bol.objects.get(box_number = sand_map_box)
            print(sand_box.box_weight)
        except:
            messages.error(request, 'Box is empty or does not exist.')
    

    context = {'sand_types': sand_types, 'pad': pad, 'all_bols': all_bols, 'stage_number': stage_number, 'well': well}
    return render(request, 'projects/projects.html', context)

def setup_job(request):
    well_form = WellForm()
    stage_form = StageForm()
    current_wells_on_pad = Well.objects.all()
    stage_numbers = Stage.objects.all()

    if request.method == "POST":
        well = Well(
        name = request.POST.get('name')
        )
        well.save()
        return redirect('setup_job')

    context = {'well_form': well_form, 'stage_form': stage_form, 'current_wells_on_pad': current_wells_on_pad, 'stage_numbers': stage_numbers}
    return render(request, 'projects/setup.html', context)

def deleteWell(request, pk):
    well = Well.objects.get(id=pk)

    if request.method == 'POST':
        well.delete()
        return redirect('setup_job')
    
    return render(request, 'projects/delete_form.html', {'obj': well})

def create_stage(request):
    
    if request.method == "POST":
        x = int(request.POST.get('first_stage'))
        y = int(request.POST.get('last_stage'))+1
        for i in range(x,y):
            per_stage = Stage(
                well = Well.objects.get(id=request.POST.get('well_name')),
                stage_design_sand = request.POST.get('stage_design_sand'),
                stage_number = i,
            )
            per_stage.save()
        return redirect('setup_job')

    context= {}
    return render(request, 'projects/setup.html', context)

def updateStage(request, pk):
    stage = Stage.objects.get(id=pk)
    stage_form = StageForm(instance=stage)

    if request.method == "POST":
        stage_form = StageForm(request.POST, instance=stage)
        if stage_form.is_valid():
            stage_form.save()
            return redirect('setup_job')

    context= {'stage_form': stage_form}
    return render(request, 'projects/update_stage.html', context)

def updatePad(request, pk):
    pad = Pad.objects.get(id=pk)
    form = PadForm(instance=pad)

    if request.method == 'POST':
        form = PadForm(request.POST, instance=pad)
        if form.is_valid():
            form.save()
            return redirect('pad')

    context = {'form': form}
    return render(request, 'projects/pad_update_form.html', context)

def deletePad(request, pk):
    pad = Pad.objects.get(id=pk)

    if request.method == 'POST':
        pad.delete()
        return redirect('pad')
    
    return render(request, 'projects/delete_form.html', {'obj': pad})

def create_sand_types(request):
    form = SandTypeForm()
    sand_types = sandType.objects.all()
    
    if request.method == "POST":
        sand_type = sandType(
        name = request.POST.get('name')
        )
        sand_type.save()
        return redirect('sand_types')

    context = {'sand_types': sand_types, 'form': form}
    return render(request, 'projects/sand-types.html', context)

def sand_type(request, slug):
    pad = Pad.objects.filter(working_status=True)
    bols = Bol.objects.all().order_by('-created')
    sand_types = sandType.objects.all()
    one_sand_type = sandType.objects.get(slug=slug)
    SI_number = 1001

    sand_total_weight_on_location = Bol.objects.aggregate(total_sand_location = Sum('left_on_location'))
    sand_total_per_type = Bol.objects.filter(sand_type = one_sand_type).aggregate(total_sand_location_per_type = Sum('left_on_location'))
    box_count_location_per_type = Bol.objects.filter(sand_type = one_sand_type).count()
    

    if request.method == 'POST':
        box_number = request.POST.get('box_number')
        api_key = 'dbce44bf-1e65-4a18-a38e-a5e2d4b06c84'
        response = requests.get('https://publicapis.propx.com/api/v1/boxes/' + str(box_number) + '/lastload?authorization=' + api_key)
        data = response.json()
        print(data)
        
        if not data['data']:
            messages.add_message(request, messages.INFO, 'Box does not exist!')
            return redirect('sand_type', slug=slug)
        elif not pad:
            messages.add_message(request, messages.INFO, 'Need to select or add Active pad for your crew!!')
            return redirect('pad')
        elif str(pad[0].name).lower() != str(data['data'][0]['job_name']).lower():
            messages.add_message(request, messages.INFO, 'Box belongs to a different pad!')
            return redirect('sand_type', slug=slug)
        else:
            bol1 = Bol(
                load_no = data['data'][0]['load_no'],
                bol_no = data['data'][0]['ticket_no'],
                po_name = data['data'][0]['po_name'],
                arrived_time = data['data'][0]['destination_on'],
                box_number = data['data'][0]['load_boxes'][0]['box_number'],
                box_weight = data['data'][0]['load_boxes'][0]['box_weight'],
                left_on_location = data['data'][0]['load_boxes'][0]['box_weight'],
                facility_name = data['data'][0]['terminal_name'],
                approved_miles = data['data'][0]['approved_mileage'],
                job_name = data['data'][0]['job_name'],
                carrier_name = data['data'][0]['carrier_name'],
                sand_type = data['data'][0]['product_name'],
                # si_number = SI_number.count() + 1,
                
            )
            bol2 = Bol(
                load_no = data['data'][0]['load_no'],
                bol_no = data['data'][0]['ticket_no'],
                po_name = data['data'][0]['po_name'],
                arrived_time = data['data'][0]['destination_on'],
                box_number = data['data'][0]['load_boxes'][1]['box_number'],
                box_weight = data['data'][0]['load_boxes'][1]['box_weight'],
                left_on_location = data['data'][0]['load_boxes'][1]['box_weight'],
                facility_name = data['data'][0]['terminal_name'],
                approved_miles = data['data'][0]['approved_mileage'],
                job_name = data['data'][0]['job_name'],
                carrier_name = data['data'][0]['carrier_name'],
                sand_type = data['data'][0]['product_name'],
                # si_number = SI_number.count() + 1,

            )
            bol1.save()
            SI_number += 1
            print('=============')
            print(SI_number)
            bol2.save()
            SI_number += 1
            print('=============')
            print(SI_number)

            return redirect('sand_type', slug=slug)
        
    context = {'one_sand_type': one_sand_type, 'bols': bols, 'sand_types': sand_types, 'sand_total_weight_on_location': sand_total_weight_on_location, 'sand_total_per_type': sand_total_per_type, 'box_count_location_per_type': box_count_location_per_type}
    return render(request, 'projects/one_sand_type.html', context)

def updateSandType(request, pk):
    one_sand_type = sandType.objects.get(id=pk)
    form = SandTypeForm(instance=one_sand_type)

    if request.method == 'POST':
        form = SandTypeForm(request.POST, instance=one_sand_type)
        if form.is_valid():
            form.save()
            return redirect('sand_types')

    context = {'form': form}
    return render(request, 'projects/sand_type_form.html', context)

def deleteSandType(request, pk):
    one_sand_type = sandType.objects.get(id=pk)

    if request.method == 'POST':
        one_sand_type.delete()
        return redirect('sand_types')
    
    return render(request, 'projects/delete_form.html', {'obj': one_sand_type})

def get_all_active_jobs(request):
    active_jobs = Pad.objects.all()
    
    if request.method == 'POST':
        api_key = 'dbce44bf-1e65-4a18-a38e-a5e2d4b06c84'
        response = requests.get('https://publicapis.propx.com/api/v1/jobs/?authorization=' + api_key)
        propconnect_jobs = response.json()
        
        working_crew = request.POST.get('crew')

        for dic in propconnect_jobs['data']:
            if working_crew.lower() in dic['crew_name'].lower() and dic['working_status'] == 'Not Started':
                messages.add_message(request, messages.INFO, 'Pad is not active on PropConnect, contact Liberty Dispatch.')
                return redirect('pad')
            elif working_crew.lower() in dic['crew_name'].lower() and dic['working_status'] == 'Active':
                pad = Pad(
                    job_id = dic['id'],
                    name = dic['name'],
                    crew_name = dic['crew_name']
                )
                pad.save()
        return redirect('pad')
    context = {'active_jobs': active_jobs}
    return render(request, 'projects/pads.html', context)

def sandInfo(request):
    wells = Well.objects.all()
    well_stages = Stage.objects.all().order_by('well')

    context = {'wells': wells, 'well_stages': well_stages}
    return render(request, 'projects/sand_info.html', context)