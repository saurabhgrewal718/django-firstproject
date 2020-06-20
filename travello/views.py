from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    
    dest1= Destination()
    dest1.name="Mumbai"
    dest1.desc="Mumbai is just awsome for all the things we can think of"
    dest1.price=345
    dest1.img="str"

    dest2= Destination()
    dest2.name="Shimla"
    dest2.desc="Shimla is just awsome for all the things we can think of"
    dest2.price=845
    dest2.img="str"

    dest3= Destination()
    dest3.name="Rohtak"
    dest3.desc="Rohtak is just awsome for all the things we can think of"
    dest3.price=900
    dest3.img="str"

    return render(request,'index.html',{'dest1':dest1,'dest2':dest2,'dest3':dest3})