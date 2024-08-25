
#from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def ajoute(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['nom']
            pr = fm.cleaned_data['prenom']
            ag = fm.cleaned_data['age']
            em = fm.cleaned_data['email']
            op = fm.cleaned_data['option']
            reg = User(nom = nm, prenom = pr, age = ag, email = em, option = op)
            reg.save()
            fm = StudentRegistration() 
    else:
        fm = StudentRegistration()

    return render(request, 'inscription_app/ajout.html',{'form':fm})


def lister(request):
    stud = User.objects.all()

    return render(request,'inscription_app/listes.html',{'stu':stud})
