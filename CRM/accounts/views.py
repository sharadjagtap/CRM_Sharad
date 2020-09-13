from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CreateUserForm,AccountForm,ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user,allowed_users,admin_only
from accounts.models import tbl_account_info,Contact


@login_required(login_url='login')
# @admin_only
def table_view(request):
    accounts=tbl_account_info.objects.all()
    contacts=Contact.objects.all()
    total_accounts=accounts.count()
    total_contacts=contacts.count()
    # pending=tbl_account_info.objects.filter(status='Pending').count()
    context={'total_accounts':total_accounts,'total_contacts':total_contacts,}
    return render(request,'accounts/table.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer'])
def home_view(request):
    return render(request,'accounts/home.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer2'])
def order_view(request):
    return render(request,'accounts/order.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def help_view(request):
    return render(request,'accounts/help.html')



def userPage(request):
    context={}
    return render(request,'accounts/user.html',context)

@unauthenticated_user
def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')

            group= Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request,"Account created for " +username)
            return redirect('login')

    context={'form':form}
    return render(request,'accounts/register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')
    context={}
    return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# ------------------------------------ Account CRUD---------------------------------------------------------------------

# view all or fetch all
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer'])
def account(request):
    accounts=tbl_account_info.objects.all()
    context={'accounts':accounts}
    return render(request,'accounts/account.html',context)


#create account
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer'])
def create_account_view(request):
    form=AccountForm()
    if request.method=='POST':
        form=AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account')
    context={'form':form}
    return render(request,'accounts/create_account.html',context)


#Update Account
def updateAccount(request, pk):
	action = 'update'
	acct = tbl_account_info.objects.get(id=pk)
	form = AccountForm(instance=acct)
	if request.method == 'POST':
		form = AccountForm(request.POST, instance=acct)
		if form.is_valid():
			form.save()
			return redirect('/account/' + str(acct.id))

	context =  {'action':action, 'form':form}
	return render(request, 'accounts/account_form.html', context)

# Delete Account
def delete_account(request, pk):
    acct = tbl_account_info.objects.get(id=pk)
    if request.method == 'POST':
        acct_id = acct.id
        acct_url = '/account/' + str(acct_id)
        acct.delete()
        return redirect(acct_url)

    return render(request, 'accounts/delete_account.html', {'item': acct})


# ------------------------------------ Contact CRUD---------------------------------------------------------------------

# View all/fetch all contacts
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer2'])
def contact(request):
    contacts=Contact.objects.all()
    return render(request,'contact/contact.html',{'contacts':contacts})

#create Contact
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','customer2'])
def create_contact(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    context={'form':form}
    return render(request,'contact/create_contact.html',context)


#Update Contact
def updateContact(request, pk):
	action = 'update'
	cont = Contact.objects.get(id=pk)
	form = ContactForm(instance=cont)
	if request.method == 'POST':
		form = ContactForm(request.POST, instance=cont)
		if form.is_valid():
			form.save()
			return redirect('/contact/' + str(cont.id))

	context =  {'action':action, 'form':form}
	return render(request, 'contact/contact_update.html', context)


# Delete Contact
def delete_contact(request, pk):
    cont = Contact.objects.get(id=pk)
    if request.method == 'POST':
        cont_id = cont.id
        cont_url = '/contact/' + str(cont_id)
        cont.delete()
        return redirect(cont_url)

    return render(request,'contact/delete_contact.html', {'item': cont})


# def delete_cont(request, pk):
#     cont = Contact.objects.get(id=pk)
#     if request.method == 'POST':
#         cont_id = cont.id
#         cont_url = '/account/' + str(cont_id)
#         cont.delete()
#         return redirect(cont_url)
#
#     return render(request, 'contatcs/delete_account.html', {'item': acct})