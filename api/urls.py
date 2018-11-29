from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^pet$',views.PetView.as_view()),
]