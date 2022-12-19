from django.shortcuts import render
import mysql.connector as sql
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
        # d="SELECT LAST_INSERT_ID();"
        # cursor.execute(d)
        # print("hhh")
        
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

def request(request):
    
    return render(request,'request.html')

def home(request):
    return render(request,'welcome.html')

def about(request):
    return render(request,'about.html')

def track(request):
    return render(request,'trackstatus.html')

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
        Status="Request Received"
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
    
    return render(request,'trackstatus.html',Data)