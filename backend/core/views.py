import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import BuildProject, BuildTask, Material


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['buildproject_count'] = BuildProject.objects.count()
    ctx['buildproject_planning'] = BuildProject.objects.filter(status='planning').count()
    ctx['buildproject_in_progress'] = BuildProject.objects.filter(status='in_progress').count()
    ctx['buildproject_on_hold'] = BuildProject.objects.filter(status='on_hold').count()
    ctx['buildproject_total_budget'] = BuildProject.objects.aggregate(t=Sum('budget'))['t'] or 0
    ctx['buildtask_count'] = BuildTask.objects.count()
    ctx['buildtask_pending'] = BuildTask.objects.filter(status='pending').count()
    ctx['buildtask_in_progress'] = BuildTask.objects.filter(status='in_progress').count()
    ctx['buildtask_completed'] = BuildTask.objects.filter(status='completed').count()
    ctx['buildtask_total_cost'] = BuildTask.objects.aggregate(t=Sum('cost'))['t'] or 0
    ctx['material_count'] = Material.objects.count()
    ctx['material_cement'] = Material.objects.filter(category='cement').count()
    ctx['material_steel'] = Material.objects.filter(category='steel').count()
    ctx['material_brick'] = Material.objects.filter(category='brick').count()
    ctx['material_total_unit_cost'] = Material.objects.aggregate(t=Sum('unit_cost'))['t'] or 0
    ctx['recent'] = BuildProject.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def buildproject_list(request):
    qs = BuildProject.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'buildproject_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def buildproject_create(request):
    if request.method == 'POST':
        obj = BuildProject()
        obj.name = request.POST.get('name', '')
        obj.client = request.POST.get('client', '')
        obj.location = request.POST.get('location', '')
        obj.budget = request.POST.get('budget') or 0
        obj.spent = request.POST.get('spent') or 0
        obj.status = request.POST.get('status', '')
        obj.start_date = request.POST.get('start_date') or None
        obj.end_date = request.POST.get('end_date') or None
        obj.progress = request.POST.get('progress') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/buildprojects/')
    return render(request, 'buildproject_form.html', {'editing': False})


@login_required
def buildproject_edit(request, pk):
    obj = get_object_or_404(BuildProject, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.client = request.POST.get('client', '')
        obj.location = request.POST.get('location', '')
        obj.budget = request.POST.get('budget') or 0
        obj.spent = request.POST.get('spent') or 0
        obj.status = request.POST.get('status', '')
        obj.start_date = request.POST.get('start_date') or None
        obj.end_date = request.POST.get('end_date') or None
        obj.progress = request.POST.get('progress') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/buildprojects/')
    return render(request, 'buildproject_form.html', {'record': obj, 'editing': True})


@login_required
def buildproject_delete(request, pk):
    obj = get_object_or_404(BuildProject, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/buildprojects/')


@login_required
def buildtask_list(request):
    qs = BuildTask.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'buildtask_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def buildtask_create(request):
    if request.method == 'POST':
        obj = BuildTask()
        obj.title = request.POST.get('title', '')
        obj.project_name = request.POST.get('project_name', '')
        obj.assigned_to = request.POST.get('assigned_to', '')
        obj.status = request.POST.get('status', '')
        obj.priority = request.POST.get('priority', '')
        obj.due_date = request.POST.get('due_date') or None
        obj.cost = request.POST.get('cost') or 0
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/buildtasks/')
    return render(request, 'buildtask_form.html', {'editing': False})


@login_required
def buildtask_edit(request, pk):
    obj = get_object_or_404(BuildTask, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.project_name = request.POST.get('project_name', '')
        obj.assigned_to = request.POST.get('assigned_to', '')
        obj.status = request.POST.get('status', '')
        obj.priority = request.POST.get('priority', '')
        obj.due_date = request.POST.get('due_date') or None
        obj.cost = request.POST.get('cost') or 0
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/buildtasks/')
    return render(request, 'buildtask_form.html', {'record': obj, 'editing': True})


@login_required
def buildtask_delete(request, pk):
    obj = get_object_or_404(BuildTask, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/buildtasks/')


@login_required
def material_list(request):
    qs = Material.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(category=status_filter)
    return render(request, 'material_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def material_create(request):
    if request.method == 'POST':
        obj = Material()
        obj.name = request.POST.get('name', '')
        obj.category = request.POST.get('category', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.unit = request.POST.get('unit', '')
        obj.unit_cost = request.POST.get('unit_cost') or 0
        obj.supplier = request.POST.get('supplier', '')
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/materials/')
    return render(request, 'material_form.html', {'editing': False})


@login_required
def material_edit(request, pk):
    obj = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.category = request.POST.get('category', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.unit = request.POST.get('unit', '')
        obj.unit_cost = request.POST.get('unit_cost') or 0
        obj.supplier = request.POST.get('supplier', '')
        obj.status = request.POST.get('status', '')
        obj.save()
        return redirect('/materials/')
    return render(request, 'material_form.html', {'record': obj, 'editing': True})


@login_required
def material_delete(request, pk):
    obj = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/materials/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['buildproject_count'] = BuildProject.objects.count()
    data['buildtask_count'] = BuildTask.objects.count()
    data['material_count'] = Material.objects.count()
    return JsonResponse(data)
