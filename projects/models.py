from django.db import models
from django.utils.text import slugify
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField

# Create your models here.
        
class Well(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Stage(models.Model):
    stage_number = models.CharField(max_length=100)
    stage_design_sand = models.CharField(null = True, max_length=100)
    well = models.ForeignKey(Well, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - Stage %s" % (self.well, self.stage_number)

class Bol(models.Model):
    load_no = models.CharField(max_length=200)
    bol_no = models.CharField(max_length=200)
    po_name = models.CharField(max_length=200)
    box_number = models.CharField(max_length=200)
    box_weight = models.CharField(max_length=200)
    left_on_location = models.CharField(max_length=200, null=True)
    facility_name = models.CharField(max_length=200)
    approved_miles = models.CharField(max_length=200)
    job_name = models.CharField(max_length=200)
    carrier_name = models.CharField(max_length=200)
    sand_type = models.CharField(max_length=200)
    arrived_time = models.DateTimeField(null=True)
    bol_comment = models.CharField(max_length=200, null=True, blank=True)
    stage_number = models.ForeignKey(Stage, on_delete=models.CASCADE, null=True)
    well_name = models.ForeignKey(Well, on_delete=models.CASCADE, null=True)
    si_number = models.CharField(max_length=200, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.box_number

class sandType(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    used = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Pad(models.Model):
    name = models.CharField(max_length=200)
    job_id = models.CharField(max_length=200, null=True)
    crew_name = models.CharField(max_length=200, null=True)
    working_status = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
