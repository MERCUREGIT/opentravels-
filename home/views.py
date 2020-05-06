from django.shortcuts import render

# Create your views here.

#default view for the home app
def index (http_request):
	return render(http_request, 'home/index.html')
