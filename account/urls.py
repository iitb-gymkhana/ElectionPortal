from django.conf.urls import url

from .views import VoterLoginView, VoterLogoutView
from django.conf.urls import include

urlpatterns = [
    url(r'^login/$', VoterLoginView.as_view(), name='login'),
    url(r'^logout/$', VoterLogoutView.as_view(), name='logout'),
]
