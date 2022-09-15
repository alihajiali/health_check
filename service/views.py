from django.shortcuts import render, redirect
from .models import *
import subprocess
import os


def add_service(request):
    if str(request.user) != "AnonymousUser":
        if request.method == "GET":
            return render(request, "service/add_service.html")

        if request.method == "POST":
            data = request.POST
            name = data["name"]
            color = data["color"]
            obj = ServiceModels.objects.create(name=name, color=color)
            obj.save()
            return redirect("service:services")
    else:
        return redirect("account:login")


def status(service_name):
    try:
        status_number = os.system(
            f'systemctl is-active --quiet {service_name}')
        if status_number == 768:
            status = "faild"
        elif status_number == 0:
            status = "active"
        return status
    except:
        return None


def change_status(request, service_name):
    if str(request.user) != "AnonymousUser":
        if request.method == "GET":
            status_number = os.system(f'systemctl is-active --quiet {service_name}')
            if status_number == 768:
                subprocess.check_output(["sudo systemctl restart {}".format(service_name)], shell=True)
            elif status_number == 0:
                subprocess.check_output(["sudo systemctl stop {}".format(service_name)], shell=True)
            return redirect("service:services")
    else:
        return redirect("account:login")


def services(request):
    if str(request.user) != "AnonymousUser":
        if request.method == "GET":
            services = ServiceModels.objects.all()
            response = []
            for service in services:
                response.append({"name":service.name, "color":service.color, "status":status(service.name), "id":service.id})
            return render(request, "service/services.html", context={"response":response})
    else:
        return redirect("account:login")


def edit_service(request, id):
    if str(request.user) != "AnonymousUser":
        if request.method == "GET":
            service = ServiceModels.objects.get(id=id)
            return render(request, "service/edit_service.html", context={"service":service})
        if request.method == "POST":
            service = ServiceModels.objects.get(id=id)
            data = request.POST
            service.name = data["name"]
            service.color = data["color"]
            service.save()
            return redirect("service:services")
    else:
        return redirect("account:login")