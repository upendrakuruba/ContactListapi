from django.urls import path
from .views import *

urlpatterns = [
    path("", Slist.as_view(), name="list"),
    path("retrieve/<int:pk>/", Sretrieve.as_view(), name="retrieve"),
]
