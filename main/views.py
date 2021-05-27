from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
def main_page(request):
    return render(request,'inde.html')

def mail(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    msg=request.POST.get('message')



    subject = 'trail mail'
    message = f'<h1>{name}</h1><h1>we recived your msg</h1>'
    # html_content = render_to_string('mail.html')
    # text_content = strip_tags(html_content)
    html_content=f'<p>this message is sent by <strong>{name}</strong></p><br><p>from email<strong> {email}</strong></p><p><br>message:<strong>{msg}</strong></p>'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['aravindharinarayanan111@gmail.com']
    #recipient_list.append(email)
    # send_mail(subject, text_content, email_from, recipient_list)
    msg = EmailMultiAlternatives(subject, message, email_from, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return HttpResponseRedirect("/")