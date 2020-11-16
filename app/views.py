from django.shortcuts import render,HttpResponse,redirect
from .models import bank_users,transfer_money
from django.contrib import messages

# Create your views here.
def base(request):
    user = bank_users.objects.get(id=1)
    context = {
        "user":user
    }
    return render(request,'base.html',context)
def start(request):
    if request.method=='POST':
        pay = request.POST['pay']
        user = request.POST['customer']
        user1 = bank_users.objects.get(id=1)
        user2 = bank_users.objects.get(name=user)
        if int(pay) > user1.current_balance:
            #return HttpResponse(user1.name+", you don't have sufficient balance!!")
            messages.error(request,user1.name+", you don't have sufficient balance!!")
            return redirect("start")
        else:
            add_balance = user2.current_balance + int(pay)
            reduce_balance = user1.current_balance - int(pay)
            user1.current_balance = reduce_balance
            user1.save()
            user2.current_balance = add_balance
            user2.save()
            trans = transfer_money(to_user=user2.name,amount=pay)
            trans.save()
            #return HttpResponse(pay+"is credited successfully to"+user2.name)
            messages.success(request,"Rs."+pay+" is credited successfully to "+user2.name)
            return redirect('start')
    else:        
        user = bank_users.objects.get(id=1)
        all = bank_users.objects.all()
        context ={
            "all": all,
            "user":user
        }    
        return render(request,'start.html',context)
#def home(request):
#    all_users = bank_users.objects.all()
#    context = {
#        "all":all_users
#    }
#    return render(request,'home.html',context)
def transfer(request):
    all = transfer_money.objects.all()
    user = bank_users.objects.get(id=1)
    context = {
        "user": user,
        "all":all
    }
    return render(request,'customer.html',context)
