import operator

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


from django.core.mail import send_mail
from django.conf import settings
# Import smtplib for the actual sending function
import smtplib

# And imghdr to find the types of our images
import imghdr

# Here are the email package modules we'll need
from email.message import EmailMessage

@login_required
def send_email_serve_page(request):
    subject = 'Thank you for registering to our site'
    message = ''
    message = message + '<html>'
    message = message + '<head>'
    message = message + '<style>'
    message = message + '.colored {'
    message = message + '  color: blue;'
    message = message + '}'
    message = message + '#body {'
    message = message + '  font-size: 36px;'
    message = message + '}'
    message = message + '</style>'
    message = message + '</head>'
    message = message + '<body>'
    message = message + '<div id="body">'
    message = message + '<p>Hi Pierce,</p>'
    message = message + '<p class="colored">This text is Very Much Blue!!!</p>'
    message = message + '<p>Jerry</p>'
    message = message + '</div>'
    message = message + '<img src="/media/images/Back.PNG" alt="ahfjaf">'
    message = message + '</body>'
    message = message + '</html>'

    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['omeca13@gmail.com', 'hams.system2019@gmail.com']

    # html_message = message
    html_message = MIMEText('<html><body><h1>Hello World</h1>' +
                            '<p>this is hello world from <a href="http://www.python.org">Python</a>...</p>' +
                            '</body></html>', 'html', 'utf-8')
    send_mail(subject, "Normal Message", email_from, recipient_list, fail_silently=False, auth_user=None, auth_password=None,
              connection=None, html_message=html_message)
    return render(request, 'emailsending/sent.html')


# To Send Image in Email From Your Local Mail Server Probably, Did not work in localhost of our machine though
@login_required
def send_email_serve_page1(request):
    msg = EmailMessage()
    msg['Subject'] = 'Our family reunion'
    sender = 'pospypgre@gmail.com'
    recipients = [
        'omeca13@gmail.com',
        'hams.system2019@gmail.com'
    ]
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # Open the files in binary mode.  Use imghdr to figure out the
    # MIME subtype for each specific image.
    pngfiles = [
        './media/images/Back.PNG',
        './media/images/Front.PNG',
    ]
    for file in pngfiles:
        with open(file, 'rb') as fp:
            img_data = fp.read()
        msg.add_attachment(img_data, maintype='image',
                        subtype=imghdr.what(None, img_data))

    # Send the email via our own SMTP server.
    msg = 'asfhjkashfuasfhuasfh'
    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)
    
