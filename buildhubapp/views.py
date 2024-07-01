
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Message, UserProfile
from .forms import ProjectForm, UserProfileForm

def home(request):
    projects = Project.objects.all()
    messages = Message.objects.filter(recipient=request.user) if request.user.is_authenticated else []
    user_profile = UserProfile.objects.get(user=request.user) if request.user.is_authenticated else None
    context = {'projects': projects, 'messages': messages, 'user': request.user, 'user_profile': user_profile}
    return render(request, 'main/home.html', context)


@login_required
def post_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'main/post_project.html', {'form': form})


"""def home(request):
    return render(request, 'buildhubapp/indexxcc.html')
    #projects = Project.objects.all()
    #messages = Message.objects.all()
    #user = request.user
    #return render(request, 'home.html', {'projects': projects, 'messages': messages, 'user': user})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project': project})

def post_project(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'post_project.html')

def messages(request):
    messages = Message.objects.all()
    return render(request, 'messages.html', {'messages': messages})

def profile(request):
    user = request.user
    if request.method == 'POST':
        # Handle profile update
        pass
    return render(request, 'profile.html', {'user': user})
    """
