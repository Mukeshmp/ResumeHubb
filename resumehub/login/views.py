from django.shortcuts import render,HttpResponse,redirect
from .models import User,Resume
import mysql.connector as sql
# from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# from .forms import LoginForm
em=''
pwd=''
# Create your views here.
def HomePage(request):
    return render(request,'home.html')
def SignupPage(request):
    if request.method=='POST':
        name=request.POST['username'];
        email=request.POST['email'];
        password=request.POST['password1'];
        us=User(name=name,email=email,password=password);
        us.save();
        return redirect('login')
    return render(request,'signup.html')



def LoginPage(request):
    global em,pwd
    if request.method=='POST':
        m=sql.connect(host="localhost",user="root",passwd="mpboss",database='resumehub')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from user where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'login1.html')
        else:
            return redirect('home')
    return render(request, 'login.html')

def CreateResume(request):
    if request.method=='POST':
        name=request.POST['name'];
        email=request.POST['email'];
        phone=request.POST['phone'];
        address=request.POST['address'];
        workexp=request.POST['work-experience'];
        degree=request.POST['degree'];
        dyear=request.POST['dyear'];
        d1year=request.POST['d1year'];
        inter=request.POST['intermediate'];
        iyear=request.POST['iyear'];
        i1year=request.POST['i1year'];
        school=request.POST['school'];
        syear=request.POST['syear'];
        s1year=request.POST['s1year'];
        skills=request.POST['skills'];
        certifications=request.POST['certifications'];
        achievements=request.POST['achievements'];
        if (name == '' or email=='' or phone == '' or address == '' or workexp == '' or degree == '' or dyear == ''  or d1year=='' or inter == '' or iyear == '' or i1year=='' or school=='' or syear == '' or s1year == '' or skills =='' or certifications=='' or achievements =='' ):
            return render(request,'detailsrequired.html')
        us=Resume(name=name,email=email,phone=phone,address=address,workexp=workexp,dins=degree,d1y=dyear,d2y=d1year,iins=inter,i1y=iyear,i2y=i1year,sins=school,s1y=syear,s2y=s1year,skills=skills,certifications=certifications,achievements=achievements);
        us.save();
        return redirect('home')
        
    return render(request,"createresume.html")

def MyProfile(request):
    print(em)
    m=sql.connect(host="localhost",user="root",passwd="mpboss",database='resumehub')
    cursor=m.cursor()
    c="select * from resume where email='{}'".format(em)
    t=cursor.execute(c)
    t=tuple(cursor.fetchall())
    if t==():
        return render(request,'failed.html')
    else:
        s=t[0][1].split()
        return render(request,'myprofile.html',{'name' : s[0],'lname': s[1],'email': t[0][2],'phone':t[0][3],'address':t[0][4],'workexp':t[0][5],'dins':t[0][6],'d1y':t[0][7],'d2y':t[0][8],'iins':t[0][9],'i1y':t[0][10],'i2y':t[0][11],'sins':t[0][12],'s1y':t[0][13],'s2y':t[0][14],'skills':t[0][15],'certifications':t[0][16],'achievements':t[0][17]})
    

def SearchedProfile(request):
    search=request.GET.get('search')
    search=search.strip()
    print(search)
    m=sql.connect(host="localhost",user="root",passwd="mpboss",database='resumehub')
    cursor=m.cursor()
    c="select * from resume where name='{}'".format(search)
    t=cursor.execute(c)
    t=tuple(cursor.fetchall())
    if t==():
        return render(request,'failed.html')
    else:
        s=t[0][1].split()
        return render(request,'myprofile.html',{'name' : s[0],'lname': s[1],'email': t[0][2],'phone':t[0][3],'address':t[0][4],'workexp':t[0][5],'dins':t[0][6],'d1y':t[0][7],'d2y':t[0][8],'iins':t[0][9],'i1y':t[0][10],'i2y':t[0][11],'sins':t[0][12],'s1y':t[0][13],'s2y':t[0][14],'skills':t[0][15],'certifications':t[0][16],'achievements':t[0][17]})
    
