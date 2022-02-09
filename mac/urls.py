from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls,name="admin"),
    path('',views.home,name="home"),
    path('about',views.about,name='about'),
    path('service',views.service,name="service"),
    
    path('shop/', include('shop.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




