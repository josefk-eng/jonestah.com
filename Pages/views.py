from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms import ContactMessageForm
from .emailConfigs import sendMail
from django.contrib import messages


# Create your views here.

def index(request):
    # service = None
    services = models.Service.objects.all()
    members = models.TeamMember.objects.all()
    # if pk != -1:
    #     service = models.Service.objects.get(id=pk)
    form = ContactMessageForm()
    context = {"services": services, "members": members,"form": form}
    # if service:
    #     return redirect(service, context)
    # else:
    return render(request, 'home.html', context)


def serviceRequest(request):
    return render(request, 'requestTabs.html')


def feedback(request):
    if request.method == 'POST':
        contactForm = ContactMessageForm(data=request.POST)
        if contactForm.is_valid():
            contactForm.save()
            title = request.POST['name']
            if title is None:
                title = request.POST['email']
            sendMail(
                subject=f"{request.POST['subject']} from {title}",
                message=request.POST['message'],
                rcpt_list=["kigozijosefed1993@gmail.com", ]
            )
            messages.success(request, "Your message has been sent successfully. Thank You")
            return redirect('index')
        else:
            messages.error(request, "Could not send your message please try again")
            return redirect('index')

    else:
        print("Nothing is done")
        return redirect('index')
