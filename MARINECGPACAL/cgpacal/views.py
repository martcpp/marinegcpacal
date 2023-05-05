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


    coursesA= ['CHM111','CHM113','GST111','GST112','MTH110','MTH112','PHY111','PHY113']
    coursesA.sort()
    coursesB= ['CHM122','CHM124','GST121','GST122','GST123','MTH123','MTH125','PHY124','PHY109']
    coursesB.sort()

    mydict = {

        'coursesA':coursesA,
        'coursesB':coursesB,

    }
        
   
    
    return render(request, 'one.html', context=mydict)


def two(request):


    ## using twc as two credit thc and three credit frc as four fvc as five sxc as six
    coursesA= ['EMA281','ECP281','MEE221','MEE211','PRE211','CVE211','EEE211','ENS211','ELA211']
    coursesA.sort()
    coursesB= ['EMA282','MEE222','MEE212','PRE212','CHE222','EEE212','ELA211','MRE212']
    coursesB.sort()

    mydict = {

        'coursesA':coursesA,
        'coursesB':coursesB,

    }
        
   
    
    return render(request, 'two.html', context=mydict)


def three(request):



    coursesA= ['EMA381','MEE351','EEE311','MEE361','MRE310','PRE311','MRE316','MRE311','ELA301','MRE317']
    coursesA.sort()
    coursesB= ['EMA382','MRE376','EEE312','MRE314','EEE316','EEE332','ELA302','MRE312']
    coursesB.sort()

    mydict = {

        'coursesA':coursesA,
        'coursesB':coursesB,

    }
        
   
    
    return render(request, 'three.html', context=mydict)


def four(request):

    coursesA= ['EMA481','MRE431','MRE411','MRE410','MRE412','MRE416','EEE453','ELA401']
    coursesA.sort()
    coursesB= ['UBITS(INDUSTRIAL TRAINING IT)']
    coursesB.sort()

    mydict = {

        'coursesA':coursesA,
        'coursesB':coursesB,

    }
        
   
    
    return render(request, 'four.html', context=mydict)


def resultA (request):

    mydict = {}
        
    try:

        credit1 = int(request.POST['credit1'])
        credit2 = int(request.POST['credit2'])
        credit3 = int(request.POST['credit3'])
        credit4 = int(request.POST['credit4'])
        credit5 = int(request.POST['credit5'])
        credit6 = int(request.POST['credit6'])
        credit7 = int(request.POST['credit7'])
        credit8 = int(request.POST['credit8'])
        
        grade1 = int(request.POST['grade1'])
        grade2= int(request.POST['grade2'])
        grade3 = int(request.POST['grade3'])
        grade4 = int(request.POST['grade4'])
        grade5 = int(request.POST['grade5'])
        grade6 = int(request.POST['grade6'])
        grade7 = int(request.POST['grade7'])
        grade8 = int(request.POST['grade8'])
       

        credit11 = int(request.POST['credit11'])
        credit12 = int(request.POST['credit12'])
        credit13 = int(request.POST['credit13'])
        credit14 = int(request.POST['credit14'])
        credit15 = int(request.POST['credit15'])
        credit16 = int(request.POST['credit16'])
        credit17 = int(request.POST['credit17'])
        credit18 = int(request.POST['credit18'])
        credit19 = int(request.POST['credit19'])
        grade11 = int(request.POST['grade11'])
        grade12= int(request.POST['grade12'])
        grade13 = int(request.POST['grade13'])
        grade14 = int(request.POST['grade14'])
        grade15 = int(request.POST['grade15'])
        grade16 = int(request.POST['grade16'])
        grade17 = int(request.POST['grade17'])
        grade18 = int(request.POST['grade18'])
        grade19 = int(request.POST['grade19'])
        
   
        firstTC = credit1 + credit2 + credit3 + credit4 + credit5 + credit6 + credit7 + credit8 
        firstGP = (credit1*grade1) + (credit2*grade2) + (credit3*grade3) + (credit4*grade4) + (credit5*grade5) + (credit6*grade6) + (credit7*grade7) + (credit8*grade8)

        firstGPA = firstGP/firstTC


        secondTC = credit11 + credit12 + credit13 + credit14 + credit15 + credit16 + credit17 + credit18 + credit19
        secondGP = (credit11*grade11) + (credit12*grade12) + (credit13*grade13) + (credit14*grade14) + (credit15*grade15) + (credit16*grade16) + (credit17*grade17) + (credit18*grade18) + (credit19*grade19)

        secondGPA = secondGP/secondTC

        totalCGPA = (firstGPA + secondGPA)/ 2


        mydict = {

        'firstTC': firstTC,
        'firstGPA': round(firstGPA,3),
        'secondTC': secondTC,
        'secondGPA': round(secondGPA,3) ,
        'totalCGPA': round(totalCGPA,3),
        

        
    }
    except:
        pass 

    if 'homepage' in request.GET:
        return redirect('/')
    if 'another' in request.GET:
        return redirect('one')

    
    return render(request,'resultA.html', context=mydict)

def resultB (request):

    mydict = {}
        
    try:

        credit1 = int(request.POST['credit1'])
        credit2 = int(request.POST['credit2'])
        credit3 = int(request.POST['credit3'])
        credit4 = int(request.POST['credit4'])
        credit5 = int(request.POST['credit5'])
        credit6 = int(request.POST['credit6'])
        credit7 = int(request.POST['credit7'])
        credit8 = int(request.POST['credit8'])
        credit9 = int(request.POST['credit9'])
        grade1 = int(request.POST['grade1'])
        grade2= int(request.POST['grade2'])
        grade3 = int(request.POST['grade3'])
        grade4 = int(request.POST['grade4'])
        grade5 = int(request.POST['grade5'])
        grade6 = int(request.POST['grade6'])
        grade7 = int(request.POST['grade7'])
        grade8 = int(request.POST['grade8'])
        grade9 = int(request.POST['grade9'])

        credit11 = int(request.POST['credit11'])
        credit12 = int(request.POST['credit12'])
        credit13 = int(request.POST['credit13'])
        credit14 = int(request.POST['credit14'])
        credit15 = int(request.POST['credit15'])
        credit16 = int(request.POST['credit16'])
        credit17 = int(request.POST['credit17'])
        credit18 = int(request.POST['credit18'])
        grade11 = int(request.POST['grade11'])
        grade12= int(request.POST['grade12'])
        grade13 = int(request.POST['grade13'])
        grade14 = int(request.POST['grade14'])
        grade15 = int(request.POST['grade15'])
        grade16 = int(request.POST['grade16'])
        grade17 = int(request.POST['grade17'])
        grade18 = int(request.POST['grade18'])
        
   
        firstTC = credit1 + credit2 + credit3 + credit4 + credit5 + credit6 + credit7 + credit8 + credit9
        firstGP = (credit1*grade1) + (credit2*grade2) + (credit3*grade3) + (credit4*grade4) + (credit5*grade5) + (credit6*grade6) + (credit7*grade7) + (credit8*grade8) + (credit9*grade9)

        firstGPA = firstGP/firstTC


        secondTC = credit11 + credit12 + credit13 + credit14 + credit15 + credit16 + credit17 + credit18 
        secondGP = (credit11*grade11) + (credit12*grade12) + (credit13*grade13) + (credit14*grade14) + (credit15*grade15) + (credit16*grade16) + (credit17*grade17) + (credit18*grade18)

        secondGPA = secondGP/secondTC

        totalCGPA = (firstGPA + secondGPA)/ 2


        mydict = {

        'firstTC': firstTC,
        'firstGPA': round(firstGPA,3),
        'secondTC': secondTC,
        'secondGPA': round(secondGPA,3) ,
        'totalCGPA': round(totalCGPA,3),
        

        
    }
    except:
        pass

    if 'homepage' in request.GET:
        return redirect('/')
    if 'another' in request.GET:
        return redirect('two')

    
    return render(request,'resultB.html', context=mydict)


def resultC (request):

    mydict = {}
        
    try:

        credit1 = int(request.POST['credit1'])
        credit2 = int(request.POST['credit2'])
        credit3 = int(request.POST['credit3'])
        credit4 = int(request.POST['credit4'])
        credit5 = int(request.POST['credit5'])
        credit6 = int(request.POST['credit6'])
        credit7 = int(request.POST['credit7'])
        credit8 = int(request.POST['credit8'])
        credit9 = int(request.POST['credit9'])
        credit10 = int(request.POST['credit10'])
        grade1 = int(request.POST['grade1'])
        grade2= int(request.POST['grade2'])
        grade3 = int(request.POST['grade3'])
        grade4 = int(request.POST['grade4'])
        grade5 = int(request.POST['grade5'])
        grade6 = int(request.POST['grade6'])
        grade7 = int(request.POST['grade7'])
        grade8 = int(request.POST['grade8'])
        grade9 = int(request.POST['grade9'])
        grade10 = int(request.POST['grade10'])

        credit11 = int(request.POST['credit11'])
        credit12 = int(request.POST['credit12'])
        credit13 = int(request.POST['credit13'])
        credit14 = int(request.POST['credit14'])
        credit15 = int(request.POST['credit15'])
        credit16 = int(request.POST['credit16'])
        credit17 = int(request.POST['credit17'])
        credit18 = int(request.POST['credit18'])
        grade11 = int(request.POST['grade11'])
        grade12= int(request.POST['grade12'])
        grade13 = int(request.POST['grade13'])
        grade14 = int(request.POST['grade14'])
        grade15 = int(request.POST['grade15'])
        grade16 = int(request.POST['grade16'])
        grade17 = int(request.POST['grade17'])
        grade18 = int(request.POST['grade18'])
        
   
        firstTC = credit1 + credit2 + credit3 + credit4 + credit5 + credit6 + credit7 + credit8 + credit9 + credit10
        firstGP = (credit1*grade1) + (credit2*grade2) + (credit3*grade3) + (credit4*grade4) + (credit5*grade5) + (credit6*grade6) + (credit7*grade7) + (credit8*grade8) + (credit9*grade9) + (credit10*grade10)

        firstGPA = firstGP/firstTC


        secondTC = credit11 + credit12 + credit13 + credit14 + credit15 + credit16 + credit17 + credit18 
        secondGP = (credit11*grade11) + (credit12*grade12) + (credit13*grade13) + (credit14*grade14) + (credit15*grade15) + (credit16*grade16) + (credit17*grade17) + (credit18*grade18)

        secondGPA = secondGP/secondTC

        totalCGPA = (firstGPA + secondGPA)/ 2


        mydict = {

        'firstTC': firstTC,
        'firstGPA': round(firstGPA,3),
        'secondTC': secondTC,
        'secondGPA': round(secondGPA,3) ,
        'totalCGPA': round(totalCGPA,3),
        

        
    }
    except:
        pass 

    if 'homepage' in request.GET:
        return redirect('/')
    if 'another' in request.GET:
        return redirect('three')

    
    return render(request,'resultC.html', context=mydict)


def resultD (request):

    mydict = {}
        
    try:

        credit1 = int(request.POST['credit1'])
        credit2 = int(request.POST['credit2'])
        credit3 = int(request.POST['credit3'])
        credit4 = int(request.POST['credit4'])
        credit5 = int(request.POST['credit5'])
        credit6 = int(request.POST['credit6'])
        credit7 = int(request.POST['credit7'])
        credit8 = int(request.POST['credit8'])
        
        grade1 = int(request.POST['grade1'])
        grade2= int(request.POST['grade2'])
        grade3 = int(request.POST['grade3'])
        grade4 = int(request.POST['grade4'])
        grade5 = int(request.POST['grade5'])
        grade6 = int(request.POST['grade6'])
        grade7 = int(request.POST['grade7'])
        grade8 = int(request.POST['grade8'])
        

        credit11 = int(request.POST['credit11'])
       
        grade11 = int(request.POST['grade11'])
       
   
        firstTC = credit1 + credit2 + credit3 + credit4 + credit5 + credit6 + credit7 + credit8
        firstGP = (credit1*grade1) + (credit2*grade2) + (credit3*grade3) + (credit4*grade4) + (credit5*grade5) + (credit6*grade6) + (credit7*grade7) + (credit8*grade8) 

        firstGPA = firstGP/firstTC


        secondTC = credit11 
        secondGP = (credit11*grade11) 

        secondGPA = secondGP/secondTC

        totalCGPA = (firstGPA + secondGPA)/ 2


        mydict = {

        'firstTC': firstTC,
        'firstGPA': round(firstGPA,3),
        'secondTC': secondTC,
        'secondGPA': round(secondGPA,3) ,
        'totalCGPA': round(totalCGPA,3),
        

        
    }
    except:
        pass 
    if 'homepage' in request.GET:
        return redirect('/')
    if 'another' in request.GET:
        return redirect('four')

    
    return render(request,'resultD.html', context=mydict)