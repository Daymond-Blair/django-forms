from django.conf.urls import url
from forms_app import views

urlpatterns = [
    url(r'^', views.form_name_view, name='forms')
]
