"""opentravels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static  import static
from django.conf import settings 

import home.urls
import profile_manager.urls
import group_manager.urls
import trip_manager.urls
import relationship_manager.urls


urlpatterns = [
	path('', include(home.urls)),
	path('home/', include(home.urls)),
	path('profile/', include(profile_manager.urls)),
	path('group/', include(group_manager.urls)),
	path('trip/', include(trip_manager.urls)),
	path('relationship/', include(relationship_manager.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)