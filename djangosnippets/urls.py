"""djangosnippets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from snippets.views import top
from snippets import api_views as snippet_api_views

snippet_list = snippet_api_views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = snippet_api_views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', top, name='top'),
    path('snippets/', include('snippets.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('api/snippets/', snippet_list, name='snippet_list'),
    path('api/snippets/<int:pk>/', snippet_detail, name='snippet_detail'),
]
