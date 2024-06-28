from django.shortcuts import render

# Create your views here.


def home(request):
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
