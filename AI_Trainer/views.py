from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import StreamingHttpResponse
from AI_Trainer.camera import VideoCamera
from . import POSEMODULE as pm

# Create your views here.

def home(request):
    return render(request, 'Pages/Home.html')

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account is Created {first_name}!')
            
        return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'Pages/register.html')

def about(request):
    return render(request, 'Pages/about.html')

def video(request):
    return render(request, 'Pages/video.html')

def uploadVideo(request):
    return render(request, 'Pages/uploadVideo.html')

def profile(request):
    return render(request, 'Pages/profile.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    cam = VideoCamera()
    return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")

def gen2(camera):
    while True:
        frame = camera.get_frame2()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed_sq(request):
    cam = VideoCamera()
    return StreamingHttpResponse(gen2(cam), content_type="multipart/x-mixed-replace;boundary=frame")
