"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

base_patterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('project.api_auth.urls', namespace='api_auth')),
    path('api/reviews/', include('project.review.urls', namespace='reviews')),
    path('api/restaurants/', include('project.restaurant.urls', namespace='restaurants')),
    path('api/home/', include('project.home.urls', namespace='home')),
    path('api/search/', include('project.search.urls', namespace='search')),
    path('api/opinions/', include('project.opinions.urls', namespace='opinions')),
    # path('docs/', include_docs_urls(title='Family_fun', public=True)),
    path('api/users/', include('project.user_profile.urls', namespace='api')),
]

if settings.DEBUG:
    base_patterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('backend/', include(base_patterns))
]
