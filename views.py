from django.shortcuts import render, redirect
from .models import Module, Student, Registration
from django.contrib.auth.decorators import login_required

def home(request):
    modules = Module.objects.all()
    return render(request, 'app/home.html', {'modules': modules})

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

@login_required
def list_modules(request):
    modules = Module.objects.all()
    return render(request, 'app/list_modules.html', {'modules': modules})

@login_required
def module_details(request, module_id):
    module = Module.objects.get(pk=module_id)
    return render(request, 'app/module_details.html', {'module': module})

@login_required
def registration(request):
    if request.method == 'POST':
        module_id = request.POST.get('module_id')
        student = Student.objects.get(user=request.user)
        module = Module.objects.get(pk=module_id)
        registration = Registration.objects.create(student=student, module=module)
        return redirect('module_details', module_id=module_id)
    else:
        return redirect('list_modules')

