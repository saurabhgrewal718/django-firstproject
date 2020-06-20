from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    
    dest1= Destination()
    dest1.name="Mumbai"
    dest1.desc="Mumbai is just awsome for all the things we can think of"
    dest1.price=345
    dest1.img="destination_1.jpg"
    dest1.offer= True

    dest2= Destination()
    dest2.name="Shimla"
    dest2.desc="Shimla is just awsome for all the things we can think of"
    dest2.price=845
    dest2.img="destination_2.jpg"
    dest2.offer= False

    dest3= Destination()
    dest3.name="Rohtak"
    dest3.desc="Rohtak is just awsome for all the things we can think of"
    dest3.price=900
    dest3.img="destination_3.jpg"
    dest3.offer= False

    dests=[dest1,dest2,dest3]

    return render(request,'index.html',{'dests':dests})