from django.shortcuts import render, redirect
from back_end.forms import RegistrationForm, EditUserForm, CreatPostForm
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views.generic import(
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from classwork_app.models import Post
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'back_end/index.html')

@login_required
def register(request):
    if request.method == 'POST':
        register_data = RegistrationForm(request.POST)
        if register_data.is_valid():
            register_data.save(commit=True)
            return redirect('back_end:login')
    else:
        register_data = RegistrationForm()
    return render(request, 'back_end/register.html', {'reg':register_data})

@login_required
def view_profile(request):
    return render(request, 'back_end/view-profile.html', {'view':request.user})

@login_required
def edit_user(request):
    if request.method == 'POST':
        edit_data = EditUserForm(request.POST, instance=request.user)
        if edit_data.is_valid():
            edit_data.save(commit=True)
            messages.success(request, 'User edited successfully.')
    else:
        edit_data = EditUserForm(instance=request.user)
    return render(request, 'back_end/edit-profile.html', {'edit':edit_data})

@login_required
def pass_form(request):
	if request.method == 'POST':
		pass_form = PasswordChangeForm(data=request.POST, user=request.user)
		if pass_form.is_valid():
			pass_form.save()
			update_session_auth_hash(request, pass_form.user)
			messages.success(request, 'Password changed successfully.')
			
	else:
		pass_form = PasswordChangeForm(user=request.user)
	return render(request, 'back_end/pass-form.html', {'pass_key':pass_form})

class DisplayPost(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'back_end/display-post.html'
    context_object_name = 'display_post'

    def get_queryset(self):
        return Post.objects.order_by('-create_date')

class DetailPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'back_end/detail-post.html'
    context_object_name = 'detail_post'

class AddPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'back_end/add-post.html'
    form_class = CreatPostForm
    success_message = 'Post added successfully'
    success_url = reverse_lazy('back_end:add_post')

class EditPost(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    # form_class = CreatPostForm
    fields = ('post_title', 'post_img', 'content', 'category', 'author')
    template_name = 'back_end/add-post.html'
    success_message = 'Post added successfully'
    success_url = reverse_lazy('back_end:add_post')

class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'back_end/confirm-post.html'
    success_url = reverse_lazy('back_end:show_post')





