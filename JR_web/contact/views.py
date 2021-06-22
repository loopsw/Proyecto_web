from django.shortcuts import render,redirect
from contact.form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_Email']
            message = form.cleaned_data['message']
            try:
                mensaje = "DE: " + name + " (" + from_email + ")\n" + message
                send_mail(subject,mensaje,['jackson1reyes2@hotmail.com'],['jackson1reyes2@gmail.com'],fail_silently=False,)
                form = ContactForm() # reiciniar el formulario
            except BadHeaderError:
                return render(request,'contact/contacto.html',{'form':form,'status':"incorrecto"})
            return render(request,'contact/contacto.html',{'form':form,'status':"correcto"})
    return render(request,'contact/contacto.html',{'form':form})