from django.urls import path

from . import views

urlpatterns = [
    path('', views.projects, name='home'),
    path('setup', views.setup_job, name='setup_job'),
    path('delete_well/<str:pk>', views.deleteWell, name='delete_well'),
    path('create_stage', views.create_stage, name='create_stage'),
    path('update_stage/<str:pk>', views.updateStage, name='update_stage'),
    path('pad', views.get_all_active_jobs, name='pad'),
    path('update_pad/<str:pk>', views.updatePad, name='update_pad'),
    path('delete_pad/<str:pk>', views.deletePad, name='delete_pad'),
    path('sand_type/<slug:slug>', views.sand_type, name='sand_type'),
    path('sand_types_db', views.create_sand_types, name='sand_types'),
    path('update_sand_type/<str:pk>/', views.updateSandType, name='update_sand_type'),
    path('delete_sand_type/<str:pk>/', views.deleteSandType, name='delete_sand_type'),
    path('sandInfo', views.sandInfo, name='sandInfo'),



]