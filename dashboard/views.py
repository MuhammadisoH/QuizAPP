import os
from django.shortcuts import render

def dashboard_view(request):
    return render(request, template_name='file.html')