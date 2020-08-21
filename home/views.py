# Views for home app

from django.shortcuts import render
from django.http import HttpResponse

# View for index page
def indexView(request):
	return HttpResponse("Index Page")
