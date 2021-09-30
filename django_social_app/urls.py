from django.urls import include, path
from django.views.generic.base import TemplateView
import social_django.urls
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('cadastro/', create_user, name='cadastro')
]