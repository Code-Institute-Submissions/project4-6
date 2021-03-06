from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('restaurants/', include('restaurants.urls')),
    path('shoppingbag/', include('shoppingbag.urls')),
    path('checkoutitems/', include('checkoutitems.urls')),
    path('userprofile/', include('userprofile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
