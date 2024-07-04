
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Message, UserProfile
from .forms import ProjectForm, UserProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Message
from .forms import ProjectForm, MessageForm


def home(request):
    projects = Project.objects.all()
    messages = Message.objects.filter(recipient=request.user) if request.user.is_authenticated else []
    user_profile = UserProfile.objects.get(user=request.user) if request.user.is_authenticated else None
    context = {'projects': projects, 'messages': messages, 'user': request.user, 'user_profile': user_profile}
    return render(request, 'main/home.html', context)

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'hub/project_detail.html', {'project': project})

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

@login_required
def update_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'main/update_profile.html', {'form': form})


@login_required
def send_message(request, recipient_id):
    recipient = get_object_or_404(User, pk=recipient_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('hub:message_list')
    else:
        form = MessageForm()
    return render(request, 'hub/send_message.html', {'form': form, 'recipient': recipient})

@login_required
def message_list(request):
    messages_sent = Message.objects.filter(sender=request.user)
    messages_received = Message.objects.filter(recipient=request.user)
    return render(request, 'hub/message_list.html', {'messages_sent': messages_sent, 'messages_received': messages_received})
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
