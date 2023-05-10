from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import request

def Welcome(request):
	return render(request, 'show.html')


