from django.shortcuts import render,HttpResponse,redirect
from .models import bank_users,transfer_money
from django.contrib import messages

# Create your views here.
def home(request):
    all_users = bank_users.objects.all()
    context = {
        "all":all_users
    }
    return render(request,'home.html',context)
def trans(request):
    a = request.POST['customer1']    
    b = request.POST['customer2']
    first =  bank_users.objects.get(name = a)
    second = bank_users.objects.get(name = b)
    context = {
        "first":first,
        "second":second
    }
    if a == b:
        #return HttpResponse("you cant tansfer to yourself ,you must choose other than you")
        messages.error(request,"  choose other than you to transfer")
        return redirect("/")
    else:
        return render(request,'payment.html',context)    
def confirm(request,id1,id2):
    pay = request.POST['pay']
    user1 = bank_users.objects.get(id=id1)
    user2 = bank_users.objects.get(id=id2)
    if int(pay) > user1.current_balance:
        #return HttpResponse(user1.name+", you don't have sufficient balance!!")
        messages.error(request,user1.name+", you don't have sufficient balance!!")
        return redirect("trans")
    else:
        add_balance = user2.current_balance + int(pay)
        reduce_balance = user1.current_balance - int(pay)
        user1.current_balance = reduce_balance
        user1.save()
        user2.current_balance = add_balance
        user2.save()
        trans = transfer_money(from_user=user1.name,to_user=user2.name,amount=pay)
        trans.save()
        #return HttpResponse(pay+"is credited successfully to"+user2.name)
        messages.success(request,"Rs."+pay+" is credited successfully to "+user2.name)
        return redirect("/")

