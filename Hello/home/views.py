from django.shortcuts import render,HttpResponseRedirect
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    data = Contact.objects.all()
    # for a in data:
    #    print(a.name)
    Contact_data = {
        'ContactData':data
    }
    return render(request, 'index.html', Contact_data)
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
    
def contact(request):
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone') 
      desc = request.POST.get('desc') 
      contact = Contact(name=name, email=email, phone=phone,desc=desc)
      contact.save()
      return HttpResponseRedirect('/')
    return render(request, 'contact.html')
   
   
