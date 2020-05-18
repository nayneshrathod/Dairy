from django.shortcuts import render


# Create your views here.
def index(request):
    sample = "this is a new Data"
    return render(request, "Index.html", {'data': sample})
