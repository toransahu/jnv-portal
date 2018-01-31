"""jnvportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin

from jnvportal import views
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Users API', description='RESTful API for users')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', views.api_root),
    # format: include((pattern_list, app_namespace), namespace=None)
    path('api/', include(('users.urls', 'users'), namespace='users',)),
    path('account/', include(('account.urls', 'account'), namespace='account',)),
]
