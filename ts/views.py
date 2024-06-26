from django.shortcuts import render, redirect
from django.http import FileResponse
from django.contrib import messages
from django.core.mail import send_mail

from .forms import ContactForm
# from pathlib import Path
# import os
from django.conf import settings

def home( request ):
 form = ContactForm( )
 return render( request, 'home.html', { 'form': form } )

def contact( request ):
 if request.method == 'POST':
  form = ContactForm( request.POST )
  if form.is_valid( ):
   name = form.cleaned_data[ 'name' ]
   email = form.cleaned_data[ 'email' ]
   message = form.cleaned_data[ 'message' ]

   try:
    send_mail(
     'aubreydmoralesfigueroa.pythonanywhere.com',
     f'Name: {name}\nEmail: {email}\n\nMessage: {message}',
     'aubreymorales1989@gmail.com',
     [ 'aubreymorales1989@gmail.com' ],
     fail_silently = False, )
    messages.success( request, 'Your message has been sent.' )

   except Exception as e:
    messages.error( request, f'An error occurred while sending your message: {e}' )

   return redirect( 'home' )
 else:
  form = ContactForm( )
 return render( request, 'home.html', { 'form': form } )

def download_resume( request ):
 file_path = 'resumes/resume-aubrey-morales-figueroa.pdf'
 absolute_path = settings.BASE_DIR / 'ts/static' / file_path

 response = FileResponse( open( absolute_path, 'rb' ), content_type = 'application/pdf' )
 response[ 'Content-Disposition' ] = 'attachment; filename="resume-aubrey-morales-figueroa.pdf"'

 messages.success( request, "Aubrey's resume [.pdf] has downloaded." )

 return response
