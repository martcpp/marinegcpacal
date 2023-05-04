from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def index(request):


    ## sending user to the right level calculator

    if 'one' in request.POST:
        return redirect('one')
    
    if 'two' in request.POST:
        return redirect('two')
    
    if 'three' in request.POST:
        return redirect('three')
    
    if 'four' in request.POST:
        return redirect('four')
    


    
   

    return render(request, 'index.html',)

def one(request):


    ## using twc as two credit thc and three credit frc as four fvc as five sxc as six
    
    courses= ['EMA281','ECP281','MEE221','MEE211','PRE211','CVE211','EEE211','ENS281','ELA211']
    courses.sort()

    return render(request, 'one.html', {'courses':courses,}, )

def two(request):


    ## using twc as two credit thc and three credit frc as four fvc as five sxc as six
    
    courses= ['e1','f1','g1','h1','i1','j1','k1','l1','m1']
    courses.sort()

    return render(request, 'two.html', {'courses':courses,}, )
def three(request):


    ## using twc as two credit thc and three credit frc as four fvc as five sxc as six
    
    courses= ['e1','f1','g1','h1','i1','j1','k1','l1','m1','n1','o1','p1','q1','r1','s1','t1','a1','b1','c1','d1']
    courses.sort()

    return render(request, 'three.html', {'courses':courses,}, )
def four(request):


    ## using twc as two credit thc and three credit frc as four fvc as five sxc as six
    
    courses= ['e1','f1','g1','h1','i1','j1','k1','l1','m1','n1','o1','p1','q1','r1','s1','t1','a1','b1','c1','d1']
    courses.sort()

    return render(request, 'four.html', {'courses':courses,}, )


