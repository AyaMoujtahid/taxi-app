from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import CustomUserCreationForm, DriverProfileForm, ClientProfileForm
from .models import CustomUser

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def home(request):
    return render(request, "home.html")


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos":items})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, DriverProfileForm, ClientProfileForm
from .models import CustomUser

def register(request):
    role = request.GET.get('role', 'client')  # Default to 'client' if no role is specified
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        driver_form = DriverProfileForm(request.POST)
        client_form = ClientProfileForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save(commit=False)
            if role == 'driver':
                user.is_driver = True
            elif role == 'admin':
                user.is_admin = True
            else:
                user.is_client = True
            user.save()
            
            if role == 'driver' and driver_form.is_valid():
                driver_profile = driver_form.save(commit=False)
                driver_profile.user = user
                driver_profile.save()
            elif role == 'client' and client_form.is_valid():
                client_profile = client_form.save(commit=False)
                client_profile.user = user
                client_profile.save()
            
            return redirect('login')  # Redirect to login page after successful registration
        else:
            print(user_form.errors)  # Debugging: Print form errors
    else:
        user_form = CustomUserCreationForm()
        driver_form = DriverProfileForm()
        client_form = ClientProfileForm()
    
    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'driver_form': driver_form,
        'client_form': client_form,
        'role': role
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_driver:
                return redirect('driver_dashboard')
                
            elif user.is_client:
                return redirect('client_dashboard')
        else:
            print("Authentication failed")  # Debugging: Print authentication failure
    return render(request, 'accounts/login.html')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def driver_dashboard(request):
    return render(request, 'driver_dashboard.html')




def client_dashboard(request):
    context = {
        'statut': True,
        'chauffeur': 'Chauffeur',
        'lat': 31.932940,
        'lng': -4.423060,
    }
    return render(request, 'client_dashboard.html', context)

@csrf_exempt
def update_lat_lng(request):
    if request.method == 'POST':
        latitude = request.POST.get('Latitude')
        longitude = request.POST.get('Longitude')
        # Process latitude and longitude as needed
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

@csrf_exempt
def demande_passager(request):
    if request.method == 'POST':
        depart = request.POST.get('depart')
        destination = request.POST.get('destination')
        nombre_de_places = request.POST.get('nombreDePlaces')
        # Process the request data as needed
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)