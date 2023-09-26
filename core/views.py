from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import User, Category, Task,SingleTask
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.

def index_view(request):
    
    return render(request, "core/index.html") 

def signup_view(request):  
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        
        else:
            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('home')
            
    return render(request, 'core/signup.html')
    



def signin_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            # Authentication failed, display an error message
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'core/signin.html') 



@login_required
def profile_view(request):
    user = request.user
    try:
        userDetail = User.objects.get(username=user.username)
    except User.DoesNotExist:
        print("User does not exist in the database")

    context = {
        "userDetail": userDetail
    }

    return render(request, 'core/profile.html', context)

@login_required
def update_profile_view(request):
    if request.method == "POST":
        user = request.user
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_bio = request.POST.get('bio')
        
        if User.objects.exclude(pk=user.pk).filter(username=username).exists():
            messages.error(request, "Username is already taken. Please choose a different one.")
        else:
            user.username = username
            user.email = email
            user.bio = user_bio
            user.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")
        
    return render(request, 'core/profile.html')

@login_required
def update_password_view(request):
    if request.method == "POST":
        current_password = request.POST.get('current-password')
        new_password = request.POST.get('new-password')
        conf_password = request.POST.get('new-conf-password')

        user = request.user  # Get the currently logged-in user

        # Check if the current password is valid
        if user.check_password(current_password):
            if new_password == conf_password:
                # Set the new password for the user
                user.set_password(new_password)
                user.save()

                # Update the session to prevent the user from being logged out
                update_session_auth_hash(request, user)

                messages.success(request, 'Password updated successfully.')
                return redirect("profile")
            
            else:
                messages.error(request, 'New passwords do not match.')
                return redirect("profile")

        else:
            messages.error(request, 'Current password is incorrect.')
            return redirect("profile")


    return render(request, 'core/profile.html')

@login_required
def delete_profile_view(request):
    if request.method == "POST":
        request.user.delete()
        logout(request)

        
        return redirect('signout')  

    return render(request, 'core/profile.html')


@login_required 
def home_view(request):
    return render(request, 'core/home.html')

@login_required
def single_task_view(request):
    user = request.user

    # Filter SingleTask objects by the user
    singleTasks = SingleTask.objects.filter(user=user).order_by('-date_created')

    total_tasks = singleTasks.count()  
    completed_tasks = singleTasks.filter(status=True).count() 

    # Calculate the completion percentage (avoid division by zero)
    completion_percentage = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    context = {
        "singleTasks": singleTasks,
        "total_tasks": total_tasks,
        "completion_percentage": completion_percentage,
    }
    
    if request.method == "POST":
        single_task_name = request.POST.get("single-task-name")

        single_task = SingleTask(
            singletask_name=single_task_name,
            user=user,
        )
        single_task.save()

        return redirect('single_task')

    return render(request, 'core/home.html', context)





@require_POST
def update_task_status(request):
    task_id = request.POST.get('task_id')
    is_checked = request.POST.get('is_checked')  # Should be 'true' or 'false'

    # Fetch the task by ID and update its status
    task = SingleTask.objects.get(id=task_id)
    task.status = (is_checked == 'true')  # Convert the string to a boolean
    task.save()

    return JsonResponse({'message': 'Status updated successfully'})

@require_POST
def delete_single_task(request):
    task_id = request.POST.get('task_id')

    # Delete the task by ID
    try:
        task = SingleTask.objects.get(id=task_id)
        task.delete()
    except SingleTask.DoesNotExist:
        pass  # Handle the case where the task does not exist

    return redirect('single_task')  # Redirect back to the task list page


@login_required 
def create_task_view(request):
    return render(request, 'core/task.html') 


# @login_required
def signout_view(request):
    logout(request)
    return render(request, 'core/signout.html')

def custom_404(request, exception):
    return render(request, 'core/404.html', status=404)