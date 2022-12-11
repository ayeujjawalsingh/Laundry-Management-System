from django.shortcuts import render
import mysql.connector as sql
Fu=''
Ag=''
Em=''
Mo=''
Ge=''
Ot=''
Ad=''
Na=''
St=''
Di=''
Bl=''
Wa=''
la=''
Cl=''
We=''
De=''
Is=''
Del=''

# Create your views here.
def about(request):
    global Fu,Ag,Em,Mo,Ge,Ot,Ad,Na,St,Di,Bl,Wa,la,Cl,We,De,Is,Del
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Ujjawal@21",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="FullName":
                Fu=value
            if key=="Age":
                Ag=value
            if key=="Email":
                Em=value
            if key=="Mobile":
                Mo=value
            if key=="Gender":
                Ge=value
            if key=="Others":
                Ot=value
            if key=="Address":
                Ad=value
            if key=="Nationality":
                Na=value
            if key=="State":
                St=value
            if key=="District":
                Di=value
            if key=="Block":
                Bl=value
            if key=="Ward":
                Wa=value
            if key=="laundry":
                la=value
            if key=="Cloths":
                Cl=value
            if key=="Weight":
                We=value
            if key=="Descriptions":
                De=value
            if key=="Issued":
                Is=value
            if key=="Delievry":
                Del=value
  
        c="insert into LoundryDetails Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(Fu,Ag,Em,Mo,Ge,Ot,Ad,Na,St,Di,Bl,Wa,la,Cl,We,De,Is,Del)
        cursor.execute(c)
        m.commit()

    return render(request,'about.html')

def request(request):
    
    return render(request,'request.html')

def home(request):
    return render(request,'welcome.html')

# def about(request):
#     return render(request,'about.html')