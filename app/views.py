from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10}
    return render(request,'conditions.html',context=d)

def if_else(request):
    d={'a':10,'b':20}
    return render(request,'if_else.html',context=d)


def if_elif(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'if_elif.html',context=d)