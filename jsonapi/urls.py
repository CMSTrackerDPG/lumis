from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^all/$", views.all, name="all"),
    url(r"^good/$", views.good, name="good"),
    url(r"^bad/$", views.bad, name="bad"),
    url(r"^nodcs/$", views.no_dcs, name="nodcs"),
]
