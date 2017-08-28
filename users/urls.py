from django.conf.urls import url
from django.contrib.auth.views import LogoutView

from .views import RegisterUserView, LoginUserView, DashboardView

urlpatterns = [
    url(r'^signup/$', view=RegisterUserView.as_view(), name='signup'),
    url(r'^login/$', view=LoginUserView.as_view(), name='login'),
    url(r'^logout/$', view=LogoutView.as_view(), name='logout'),
    url(r'^adminpanel/$', view=DashboardView.as_view(), name='adminpanel'),
]