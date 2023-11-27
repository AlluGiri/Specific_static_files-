from django.shortcuts import render

# Create your views here.
def cool(request):
    return render(request,'form.html')

def inst(request):
    return render(request,'inst.html')