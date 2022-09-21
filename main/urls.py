from django.urls import path
from . import views
from main.views import CategoryViewSet, HomeApi, home


urlpatterns = [
    path('', home, name='home'),
    path('1/', CategoryViewSet.as_view()),
    path('1/<int:pk>/', CategoryViewSet.as_view())
]

