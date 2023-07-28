from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactForm
from django.urls import reverse
# from .models import ContactSubmission

# Create your views here.
def home(request):
    return render(request=request, template_name='blog/home.html')

def about(request):
    return render(request=request, template_name='blog/about.html')

def service(request):
    return render(request=request, template_name='blog/services.html')

def gallery(request):
    return render(request=request, template_name='blog/gallery.html')

def contact(request):    
    if request.method == 'POST': # User has submitted the form
        form = ContactForm(request.POST)
        if form.is_valid():
            # Validates values for each field
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']

            # Create ContactSubmission model instance and pass form values to the model as arguments
            # contact_submission = ContactSubmission(
            #     name=name,
            #     email=email,
            #     phone_number=phone_number,
            #     message=message
            # )
            # Create ContactSubmission model instance and pass form values to the model as arguments
            contact_submission = form.save()

            # Save to database
            contact_submission.save()

            return redirect(reverse('blog-contact'))  # Redirect to a success page
    else: # User is requesting to view the form
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})