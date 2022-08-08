from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("content", views.content, name="content"),
    path("videopage", views.videopage, name="videopage"),
    path("html_intro", views.html_intro, name="videopage"),
    path("html_element", views.html_element, name="videopage"),
    path("css_intro", views.css_intro, name="videopage"),
    path("css_syntax", views.css_syntax, name="videopage"),
    path("contact", views.contact, name="contact"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("Register", views.register, name="register"),
    path("html_quiz", views.html_quiz, name="html_quiz"),
    path("css_quiz", views.css_quiz, name="css_quiz"),
    path("javascript_quiz", views.javascript_quiz, name="javascript_quiz"),
]
