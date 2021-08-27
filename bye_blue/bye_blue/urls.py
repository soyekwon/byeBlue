"""bye_blue URL Configuration

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
from main import views
from online_class import views
import main.urls
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main.views.index),
    path("account/", include("account.urls", namespace="account")),
    path("online_class/", include("online_class.urls", namespace="online_class")),
    path("HomeTraining/", include("HomeTraining.urls", namespace="HomeTraining")),
    path("OTT/", include("OTT.urls", namespace="OTT")),
    path("MbTi/", include("mbti.urls", namespace="mbti")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


