from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def main_page(request):
    return render(request,'inde.html')

