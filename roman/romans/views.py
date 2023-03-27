from django.shortcuts import render,HttpResponse
from . import models
from django.contrib import messages

def home(request):

    if request.method=="POST":
        input=request.POST["num"]
        # messages.info(request,models.encoding_to_number.transform(int(input)))
        try:
            if input=="":
                messages.info(request,"empty")
            elif (int(input)>=1 and int(input)<=4000):
                messages.info(request,models.encoding_to_number.transform(int(input)))
            elif (int(input)>4000):
                messages.info(request,"Roman numbers limitation is 4000")
        except:
            messages.info(request,"string found in input")
    return render(request,"roman.html")
