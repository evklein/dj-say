from django.shortcuts import render
from django.shortcuts import render
from .forms import MyContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib import messages

def contact(request):
    form_class = MyContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():

            # To add your own form elements, follow this template:
            # your_element = request.POST.get('your_element', '')
            # NOTE: You MUST have new elements defined in forms.py.
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_subject = request.POST.get('contact_subject', '')
            form_content = request.POST.get('content', '')
            # your_element = request.POST.get('your_element', '')

            # Create content.
            template = get_template('message_template.html')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_subject': contact_subject,
                'form_content': form_content,
                # 'your_element': your_element,
            })
            all_content = template.render(context)

            # Set email contents and send.
            email = EmailMessage("New Message at YOURSITE.com",
                                 all_content,
                                 "http://www.YOURSITE.com",
                                 ['YOUR.SMTP.EMAIL@email.com'],
                                 headers={'Reply-To': contact_email }
            )
            try:
                email.send()
                alert_success(request)
            except:
                alert_failure(request, message='Connection refused.')
        else:
            alert_failure(request,
            message='Please make sure all information is filled out.')
            # Only fails if form is invalid or there is an error.

    return render(request, 'contact_form.html', { 'form': form_class })

# def create_template():


def alert_success(request):
    messages.add_message(request, messages.SUCCESS, 'Message successfully delivered.')

def alert_failure(request, message):
    messages.add_message(request, messages.ERROR, 'Message failed to deliver. ' + message)
