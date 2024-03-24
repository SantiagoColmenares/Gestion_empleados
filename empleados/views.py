from django.shortcuts import render
from django.http import HttpResponse
from .models import Salary, Job

# Create your views here.
def inicio(request):

  return render(request, 'index.html', {})

def salary(request):
  return render(request, 'salary.html', {})

def save(request):
  amound = request.GET['amound']
  salary = Salary(amound = amound)
  salary.save()
  return HttpResponse("Hola")

def job(request):
  salary = Salary.objects.all()
  return render(request, 'trabajo.html', {
    'salary':salary
  })

def save_job(request):
  name = request.GET['name']
  description = request.GET['descripcion']
  salary = Salary.objects.get(id = request.GET['salary']) 
  job = Job(name = name, description = description, salary = salary)
  job.save()

  return HttpResponse("Hemos creado")

def list_salary(request):
  salary = Salary.objects.all()
  return render(request, 'list_salary.html', {
    'salary':salary
  })

def id_salary(request, id):
    salary = Salary.objects.get(id = id)
    return HttpResponse("Actualizar Salario")

