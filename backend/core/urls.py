from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('buildprojects/', views.buildproject_list, name='buildproject_list'),
    path('buildprojects/create/', views.buildproject_create, name='buildproject_create'),
    path('buildprojects/<int:pk>/edit/', views.buildproject_edit, name='buildproject_edit'),
    path('buildprojects/<int:pk>/delete/', views.buildproject_delete, name='buildproject_delete'),
    path('buildtasks/', views.buildtask_list, name='buildtask_list'),
    path('buildtasks/create/', views.buildtask_create, name='buildtask_create'),
    path('buildtasks/<int:pk>/edit/', views.buildtask_edit, name='buildtask_edit'),
    path('buildtasks/<int:pk>/delete/', views.buildtask_delete, name='buildtask_delete'),
    path('materials/', views.material_list, name='material_list'),
    path('materials/create/', views.material_create, name='material_create'),
    path('materials/<int:pk>/edit/', views.material_edit, name='material_edit'),
    path('materials/<int:pk>/delete/', views.material_delete, name='material_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
