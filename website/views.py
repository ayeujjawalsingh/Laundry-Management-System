from django.shortcuts import render
import mysql.connector as sql
import json
import os



#----------------------Request Submit---------------------- 

Fu=''
Mo=''
St=''
Ci=''
Pi=''
Ad=''
La=''
Cl=''
We=''
De=''
Is=''
Del=''

# Create your views here.
def submitted(request):
    print(1)
    global Fu,Mo,St,Ci,Pi,Ad,La,Cl,We,De,Is,Del
    if request.method=="POST":
        print(2)
        m=sql.connect(host="localhost",user="root",passwd="Ujjawal@21",database='website')
        cursor=m.cursor()
        print(3)
        d=request.POST
        print('post-4')
        for key,value in d.items():
            print('for-5')
            if key=="FullName":
                Fu=value
            if key=="Mobile":
                Mo=value
            if key=="State":
                St=value
            if key=="City":
                Ci=value
            if key=="PinCode":
                Pi=value
            if key=="Address":
                Ad=value
            if key=="Laundry":
                La=value
            if key=="Cloths":
                Cl=value
            if key=="Weight":
                We=value
            if key=="Descriptions":
                De=value
            if key=="Issued":
                Is=value
            if key=="Delivery":
                Del=value
            print('outfor-6')
        c="insert into Details(FullName,Mobile,State,City,PinCode,Address,Laundry,Cloths,Weight,Descriptions,Issued,Delivery) Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Fu,Mo,St,Ci,Pi,Ad,La,Cl,We,De,Is,Del)
        print('c-7')
        cursor.execute(c)
        
        print('execut-8')
        m.commit()
        print('comit-9')
        print(cursor.rowcount, "hhhhhhhhhhhhhh")
        tid  = cursor.lastrowid
        print('comit-10')
        d = f"INSERT INTO Track(Status,Trackid) Values('1',{tid})"
        cursor.execute(d)
        m.commit()
        Data = {
            'TrackingId' : tid,
            'Name' : Fu,
            'Address' : Ad
        }
    # print('rendered')
        
    return render(request,'requestdone.html',Data)


#----------------------Request Rendor Function---------------------- 


def request(request):
    
    return render(request,'request.html')


#----------------------Home Rendor Function---------------------- 


def home(request):
    return render(request,'welcome.html')


#----------------------About Rendor Function---------------------- 


def about(request):
    return render(request,'about.html')



#----------------------Track Rendor Function---------------------- 


def track(request):
    return render(request,'trackstatus.html')




#----------------------Tracking Details Function---------------------- 


Tid=''
def trackingdetails(request):
    global Tid
    st=''
    if request.method=="POST":
        print(2)
        m=sql.connect(host="localhost",user="root",passwd="Ujjawal@21",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            print('for-5')
            if key=="TrackingId":
                Tid=value
        print("Out for")
        c="select * from Track where Trackid='{}'".format(Tid)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        st = (int)(t[0][0])
    Status = ""
    if st==1:
        Status="Received"
    elif st==2:
        Status="Out For Pickup"
    elif st==3:
        Status="Washing"
    elif st == 4:
        Status="Out For Delivery"
    else:
        Status="Deliverd"
    
    Data ={
        'Status' : Status
    }
    # print("iefif")
    print
    
    return render(request,'statusshow.html',Data)




#----------------------Admin Logout Function---------------------- 

# fn=''
# ln=''
# s=''
# em=''
# pwd=''
# # Create your views here.
# def Signup(request):
#     global fn,ln,s,em,pwd
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",passwd="Ujjawal@21",database='website')
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="first_name":
#                 fn=value
#             if key=="last_name":
#                 ln=value
#             if key=="sex":
#                 s=value
#             if key=="email":
#                 em=value
#             if key=="password":
#                 pwd=value
        
#         c="insert into AdminDetails Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
#         cursor.execute(c)
#         m.commit()

#     return render(request,'AdminLogin.html')


# def AdminSignup(request):
#     return render(request,'AdminLogout.html')

#----------------------Admin Login Function---------------------- 

eem=''
pwd=''
# Create your views here.
def Login(request):
    global eem,pwd
    json_path = os.path.join(os.path.dirname(__file__),'static/Json/Track.json')
    with open(json_path) as json_file:
        data = json.load(json_file)
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Ujjawal@21",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                eem=value
            if key=="password":
                pwd=value
        
        c="select * from AdminDetails where email='{}' and password='{}'".format(eem,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcomeAdmin.html',{'data':data})

    return render(request,'WelcomeAdmin.html',{'data':data})


def AdminSignin(request):
    return render(request,'AdminLogin.html')