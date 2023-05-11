from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login, logout
from .models import Notes
from django.contrib import messages


@login_required(login_url='/login')
def Home(request):
    mynotes = Notes.objects.filter(user=request.user)
    context = {
        'mynotes':mynotes
    }
    

    if request.method=="POST":
        title = request.POST['title']
        description = request.POST['description']

        notesave = Notes(title=title,description=description)
        notesave.user = request.user
        notesave.save()
        messages.success(request, 'Note created successfully',extra_tags='noteadd')

        return redirect(request.META['HTTP_REFERER'])



    return render(request,"index.html",context)


def register_page(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=email)
        if user_obj.exists():
            messages.warning(request, 'Email is already exist')
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create( email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, 'Successfully Register' , extra_tags='register')

        return redirect('/login')

    
    return render(request ,'register.html')



def login_page(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request, 'Invalid email and password' , extra_tags='login-error')
            # return render(request ,'alert/login-alert.html')




        user_obj = authenticate(username = email , password = password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')
            
        return HttpResponseRedirect(request.path_info)
    return render(request ,'login.html')




def NotesEdit(request, id):  
    notesedit = Notes.objects.get(nid=id)
    if notesedit.user != request.user:
            return redirect('/register')
    return render(request,'notes-edit.html', {'notesedit':notesedit}) 



def Notesupdate(request , id):  

    
    if request.method=="POST":
        notesedit=Notes.objects.get(nid=id)
        if notesedit.user != request.user:
            return redirect('/register')

        title = request.POST['title']
        description = request.POST['description']
        notesedit.title = title
        notesedit.description = description
        notesedit.save()
        messages.success(request, 'Note updated successfully' , extra_tags='noteupdate')

        return redirect("/")

    return render(request, 'notes-edit.html', {'notesedit': notesedit})  
    



def delete(request,id):   
        notesedit = Notes.objects.get(nid=id)
        if notesedit.user != request.user:
            return redirect('/register')
        notesedit.delete()
        messages.error(request, 'Note deleted successfully' , extra_tags='notedelete')

        return redirect('/')

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')






    


# def Notesupdate(request, id ):  

#     notesedit=Notes.objects.get(id=id)
    
#     form=detailsform(request.POST,instance=notesedit )

#     if notesedit.user != request.user:
#         messages.error(request, 'You are not authenticated to perform this action')
#         return redirect('/login')
    
#     if form.is_valid():
#         # form.user = request.user
#         # form = request
#         form.save()
        
#         return redirect('/')

#     return render(request, 'notes-edit.html', {'notesedit': notesedit})  