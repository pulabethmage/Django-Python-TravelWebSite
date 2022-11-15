from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.price = 850
    dest1.name = 'New York'
    dest1.desc = 'We love This Place so much'
    dest1.img = '1.png'
    dest1.offer = True

    dest2 = Destination()
    dest2.price = 950
    dest2.name = 'Sri Lanka'
    dest2.desc = 'Nothing Like Ceylon'
    dest2.img = '2.png'
    dest2.offer = False

    dest3 = Destination()
    dest3.price = 725
    dest3.name = 'Hydrabath'
    dest3.desc = 'Biriyani Comes First'
    dest3.img = '3.png'
    dest3.offer = False

    dest_list = [dest1,dest2,dest3]


    return render(request,'index.html',{'dests':dest_list})
