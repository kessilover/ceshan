from itertools import chain

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserForm, StoryForm, ChapterForm, CommentForm
from .models import Story, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# HomePage
def index(request):
    stories = Story.objects.filter(has_chapter=True)
    if request.user.is_authenticated():
        return render(request, 'stories/index.html', {'user': request.user, 'stories': stories})
    else:
        return render(request, 'stories/index.html', {'stories': stories})

#LoginUser
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('stories:home')
            else:
                return render(request, 'stories/login.html', {'error_message': "your account has been disabled"})
        else:
            return render(request, 'stories/login.html', {'error_message': 'Wrong Username or Password'})
    elif request.user.is_authenticated():
        return redirect('stories:home')
    else:
        return render(request, 'stories/login.html')

#RegisterUser
def register_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user.set_password(password)
        user.username = username
        user.email = email
        user.save()
        return render(request,'stories/login.html')

    return render(request, 'stories/register.html', {'form': form})

#LogoutUSer
def logout_user(request):
    logout(request)
    return redirect('stories:home')


#ProfileUser
def user_profile(request):
    if request.user.is_authenticated():
        user = request.user
        stories = Story.objects.filter(author = user)
        return render(request, 'stories/user_profile.html', {'user': user, 'stories' : stories})
    else:
        return redirect('stories:home')

#ShowPost
def post(request, story_id, page=1):
    story = Story.objects.get(id=story_id)
    chapters = story.chapter_set.all()
    paginator = Paginator(chapters, 1)
    number = chapters.count()
    if number >=1:
        try:
            chapters = paginator.page(page)
        except PageNotAnInteger:
            chapters = paginator.page(1)
        except EmptyPage:
            chapters = paginator.page(paginator.num_pages)
        return render(request, 'stories/post.html', {'story': story, 'chapters': chapters})
    else:
        return redirect('stories:add_chapter',story_id)



#Add Story
def add_story(request):
    if not request.user.is_authenticated():
        return redirect('stories:login_user')
    else:
        form = StoryForm(request.POST or None)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            return redirect('stories:profile')
        context = {
        "form": form,'user' :request.user
        }
        return render(request, 'stories/add_story.html', context)

#not done
def editprofile(request):
    return render(request, 'stories/modify_profile.html')

#Add Chapter
def addChapter(request, story_id):
    if not request.user.is_authenticated():
        return redirect('stories:login_user')
    else:
        form = ChapterForm(request.POST or None)
        if form.is_valid():
            chapter = form.save(commit=False)
            texts = request.POST["chapter"]
            chapter.chapter= texts
            story = Story.objects.get(id=story_id)
            chapter.story = story
            chapter.save()
            return redirect('stories:profile')

        context = {'form': form, 'user' :request.user}
        return render(request, 'stories/add_chapter.html', context)

#Delete Story
def delete_story(request, story_id):
    story = Story.objects.get(id=story_id)
    story.delete()
    return render(request, 'stories/user_profile.html')


def addcomment(request, story_id):
    story = Story.objects.get(id=story_id)
    chapters = story.chapter_set.all()
    if request.method == 'POST':
        review = request.POST['comment']
        writer = request.POST['writer']
        story = Story.objects.get(id = story_id)
        comment = Comment()
        comment.story = story
        comment.writer = writer
        comment.comment = review
        comment.save()
        chapters = story.chapter_set.all()
        return redirect('stories:post', story_id)
    return render(request, 'stories/post.html', {'story' : story, 'chapters' : chapters})


