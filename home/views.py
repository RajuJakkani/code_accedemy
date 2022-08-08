from django.shortcuts import redirect, render
from .models import Feedback, Customers

# Create your views here.
IS_USER_LOGGED = False
USER_NAME = None

def home(request):
    return render(request, "home/Nevil.html", {"IS_USER_LOGGED": IS_USER_LOGGED, "USER_NAME": USER_NAME})

def content(request):
    return render(request, "home/html_intro.html")

def videopage(request):
    return render(request, "home/VIDEOPAGE.HTML")

def html_intro(request):
    return render(request, "home/html_intro.html")

def html_element(request):
    return render(request, "home/html_element.html")

def css_intro(request):
    return render(request, "home/css_intro.html")

def css_syntax(request):
    return render(request, "home/css_syntax.html")

def contact(request):
    if request.POST:
        customer_name = request.POST['customer_name']
        email = request.POST['email']
        message = request.POST['message']
        create_obj = Feedback.objects.create(
            customer_name=customer_name, 
            email=email,
            message=message,
        )

    return render(request, 'home/contact.html')

def login(request):
    if request.POST:
        global IS_USER_LOGGED
        global USER_NAME
        user_names = []
        passwords = []

        data = Customers.objects.all()
        for info in data:
            user_names.append(info.user)
            passwords.append(info.password)

        user_name = request.POST['user_name']
        password = request.POST['password']
        print(data)
        print(user_name)
        print(password)
        for i in range(len(user_names)):
            if user_names[i] == user_name:
                if passwords[i] == password:
                    IS_USER_LOGGED = True
                    USER_NAME = user_names[i]
                    print("log in succesfully")
                    print(USER_NAME)
                    break

        return redirect("/")
    return render(request, 'home/logi.html')

def register(request):
    if request.POST:
        user_name = request.POST['user_name']
        password = request.POST['password']
        create_obj = Customers.objects.create(
            user=user_name,
            password=password
        )
        return redirect("/login")
    return render(request, 'home/register.html')

def logout(request):
    global IS_USER_LOGGED
    global USER_NAME
    IS_USER_LOGGED = False
    USER_NAME = None
    return redirect("/")


def html_quiz(request):
    return render(request, 'home/html_quiz.html')

def css_quiz(request):
    return render(request, 'home/css_quiz.html')
    
def javascript_quiz(request):
    return render(request, 'home/javascript_quiz.html')
    