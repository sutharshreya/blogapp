from django.shortcuts import render,redirect
from about.models import Contact
from about.forms import ContactForm  
from blogapp import settings  
from django.core.mail import send_mail  

# use for contact_us page.
def contact(request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Blog_Contact"  
            msg     = "Your message sent successfully thanks to contact_us."  
            to      = form.cleaned_data.get('email') 
            res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
            return redirect('home')
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form':form}) 

   