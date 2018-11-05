from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r'^ajax/min-max/$', views.get_min_max_run_number, name='ajax_min_max'),
]
