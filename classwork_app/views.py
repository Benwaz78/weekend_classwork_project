from django.shortcuts import render
from classwork_app.models import Post, Category, UserProfile, ContactModel
from django.contrib.auth.models import User
from classwork_app.forms import BasicForm, ContactForm, ContactUsForm
# Create your views here.
def index(request):
    post_list = Post.objects.order_by('-create_date')
    user_list = User.objects.all()
    return render(request, 'classwork_app/index.html', 
        {'post_key':post_list,
        'user_key':user_list
        }
        )

def detail(request, my_id):
    detail_post = Post.objects.get(pk=my_id)
    return render(request, 'classwork_app/post-detail.html', {'post_detail_key':detail_post})

def about(request):
    return render(request, 'classwork_app/about.html', {'heading':'About Us'})

def users(request):
    user_list = User.objects.all()
    return render(request, 'classwork_app/users.html', {'user_key':user_list})

def service(request):
    return render(request, 'classwork_app/service.html')

def contact(request):
    return render(request, 'classwork_app/contact.html')

def basic_form(request):
    if request == 'POST':
        my_form = BasicForm(request.POST)
        if my_form.is_valid():
            print('Name: '+my_form.cleaned_data['name'])
            print('Email: '+my_form.cleaned_data['email'])
            print('Message: '+my_form.cleaned_data['message'])    
    else:
        my_form = BasicForm()
    return render(request, 'classwork_app/basic-form.html', {'form_key':my_form})

def contact_form(request):
    contact_form = ContactForm()
    return render(request, 'classwork_app/contact.html', {'contact_key':contact_form})

def contact_us_form(request):
    if request.method == 'POST':
        contact_us = ContactUsForm(request.POST)
        if contact_us.is_valid():
            contact_us.save(commit=True)
    else:
        contact_us = ContactUsForm()
    return render(request, 'classwork_app/contact-model.html', {'contact_us_key':contact_us})

        