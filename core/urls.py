from django.urls import path
from . import views

# URL-ROUTES >>> pages
urlpatterns = [
    path("", views.index, name="Home-Page")
]