from django.shortcuts import render

# Create your views here.
import datetime
def built_in_filters(request):
    dt=datetime.datetime.now()
    d={'data':'TODAY WE HaVe Mock SHOOTing ','c':1,'dt':dt}
    return render(request,'bulitin_filters.html',d)