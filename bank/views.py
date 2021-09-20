from bank.admin import HistoryAdmin
from bank.forms import ActionForm, TransactionForm
from bank.models import Deposit, History, Transact, Users
from django.shortcuts import render,redirect

# Create your views here.
def Homepage(request):
    return render(request,"home.html")

def Depositpage(request,id):
    if request.method == "POST":
        pi = Users.objects.get(pk = id)
        fm = ActionForm(request.POST, instance = pi)
        if fm.is_valid():
            unm = fm.cleaned_data['username']
            eid = fm.cleaned_data['email_id']
            cnt = fm.cleaned_data['contact_no']
            amt = fm.cleaned_data['amount']
            reg = Deposit(username=unm, email_id=eid, contact_no=cnt, amount=amt)
            reg.save()
            act = "Deposit"
            sts = "Success"
            hst = History(username=unm, email_id=eid, contact_no=cnt, amount=amt, action=act, status=sts)
            hst.save()
            bal = int(amt)
            pi.balance += bal
            pi.save()
            return redirect('users')
    else:
        pi = Users.objects.get(pk = id)
        fm = ActionForm(instance = pi)
    return render(request, 'deposit.html', {"form" : fm})
    

def Transfer(request,id):
    if request.method == "POST":
        pi = Users.objects.get(pk = id)
        fm = TransactionForm(request.POST, instance = pi)
        if fm.is_valid():
            unm = fm.cleaned_data['username']
            eid = fm.cleaned_data['email_id']
            cnt = fm.cleaned_data['contact_no']
            amt = fm.cleaned_data['amount']
            rev = fm.cleaned_data['receiver']
            if amt <= pi.balance:
                reg = Transact(username=unm, email_id=eid, contact_no=cnt, amount=amt, receiver=rev)
                reg.save()
                bal = int(amt)
                pi.balance -= bal
                pi.save()
                us = Users.objects.get(username = rev)
                us.balance += bal
                us.save()
                act = "Transfer"
                sts = "Success"
                hst = History(username=unm, email_id=eid, contact_no=cnt, amount=amt, action=act, status=sts)
                hst.save()
                return redirect('users')
            else:
                at = "Insufficient Balance!"
                act = "Transfer"
                sts = "Failed"
                hst = History(username=unm, email_id=eid, contact_no=cnt, amount=amt, action=act, status=sts)
                hst.save()
                return render(request, 'transfer.html', {"form" : fm, "status": at})
    else:
        pi = Users.objects.get(pk = id)
        fm = TransactionForm(instance = pi)
    return render(request, 'transfer.html', {"form" : fm}) 
   

def Withdraw (request,id):
    if request.method == "POST":
        pi = Users.objects.get(pk = id)
        fm = ActionForm(request.POST, instance = pi)
        if fm.is_valid():
            unm = fm.cleaned_data['username']
            eid = fm.cleaned_data['email_id']
            cnt = fm.cleaned_data['contact_no']
            amt = fm.cleaned_data['amount']
            if amt <= pi.balance:
                reg = Deposit(username=unm, email_id=eid, contact_no=cnt, amount=amt)
                reg.save()
                bal = int(amt)
                pi.balance -= bal
                pi.save()
                act = "Withdraw"
                sts = "Success"
                hst = History(username=unm, email_id=eid, contact_no=cnt, amount=amt, action=act, status=sts)
                hst.save()
                return redirect('users')
            else:
                at = "Insufficient Balance!"
                act = "Withdraw"
                sts = "Failed"
                hst = History(username=unm, email_id=eid, contact_no=cnt, amount=amt, action=act, status=sts)
                hst.save()
                return render(request, 'withdraw.html', {"form" : fm, "status": at})
    else:
        pi = Users.objects.get(pk = id)
        fm = ActionForm(instance = pi)
    return render(request, 'withdraw.html', {"form" : fm})
    
def Userpage (request):
    data= Users.objects.all()
    return render(request,"users.html",{'data':data})

def Historypage(request):
    data = History.objects.all ()
    return render(request, 'history.html', {"data" : data})