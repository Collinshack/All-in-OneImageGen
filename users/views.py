from django.shortcuts import render, redirect

from django.core.files.base import ContentFile
from django.contrib import messages, auth
from .forms import UserForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image, QrCode, Waitlist
from .serializers import ImageSerializer
from dotenv import load_dotenv
import os, openai, requests, qrcode 
from django.conf import settings
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt


load_dotenv()

api_key =str(os.getenv('OPENAI_API_KEY', None))
openai.api_key = api_key

    


def index_view(request):    
    img = None
    context = {}
    if api_key is not None and request.method == 'POST':
        if 'generated_image' in request.session:
            return render(request, 'Generator/signup.html', {'error_message': 'You have already generated an image. Please register to continue.'})

        user_input = request.POST.get('user_input')
        response = openai.Image.create(
            prompt= user_input,
            size= '256x256',
        )
        image_url = response['data'][0]['url']
        response = requests.get(image_url)
        image_file = ContentFile(response.content)
        
        file_name = f'{user_input}-image.jpg'
        img = Image(prompt=user_input)
        img.generated_image.save(file_name, image_file)
        img.save()
        
        request.session['generated_image'] = True
        request.session.modified = True
        
        context = {'image': img}    

        return render(request, 'Generator/index.html', context)
    return render(request, 'Generator/index.html')



def qrcode_view(request):
    context = {}
    if request.method == 'POST':
        user_data = request.POST.get('user_data')
        fill_color = request.POST.get('fill_color')
        background_color = request.POST.get('background_color')
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        
        qr.add_data(user_data)
        qr.make(fit=True)
        image = qr.make_image(fill=(fill_color), back_color=(background_color))
        image_name = f'{slugify(user_data)}.png'
        qrcode_obj = QrCode(user_input=user_data, generated_qrcode=os.path.join('qrcodes', image_name))
        qrcode_obj.save()
        image_path = os.path.join(settings.MEDIA_ROOT, 'qrcodes', image_name)
        image.save(image_path)
        context = {'qrcode': qrcode_obj}
    return render(request, 'Generator/index.html', context)


def signup_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account was created successfully!')
            return redirect('login')
        
    context = {'form': form}
    return render(request, 'Generator/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in')   
            return redirect('pricing')
              
        else:
            messages.error(request, 'Incorrect details')
    return render(request, 'Generator/login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('/')

class api_view(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
    

def documentation_view(request):
    return render(request, 'Generator/docs.html')


def pricing_view(request):
    return render(request, 'Generator/comingsoon.html')


@csrf_exempt  # Temporary disable CSRF protection for simplicity
def waitlist_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        more_features = request.get('more_features')

       
        Waitlist.objects.create(email=email, more_features=more_features)

        return render(request, 'Generator/waitlist-success.html')

    return render(request, 'Generator/comingsoon.html')
