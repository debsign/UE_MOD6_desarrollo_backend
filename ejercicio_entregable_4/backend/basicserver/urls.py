"""
URL configuration for basicserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # se incluyen las urls del archivo creado en api_view
    path('api_view/', include('api_view.urls')),
    path('api_view/recipe/', include('recipe.urls')),
    # path('api_view/ingredient/', include('ingredient.urls')),
    path('api_view/ingredient-recipes/', include('api_view.urls')),
    # viewsets
    # path('viewset/', include('basicserver.routers')),
    path('ingredients/', include('ingredient.urls'))
]
