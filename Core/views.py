from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import send_contact_email_async
from .forms import ContactForm

# Create your views here.

def home(request):
    context = {

    }
    return render(request, 'index.html', context)


def about(request):
    context = {

    }
    return render(request, 'about.html', context)

def contact_view(request):
    form = ContactForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_contact_email_async(name, email, subject, message)

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
        else:
            messages.error(request, "Please check your inputs.")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})