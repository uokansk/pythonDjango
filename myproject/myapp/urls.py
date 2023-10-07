from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('prefix/', include('myapp2.urls')),
    path('les3/', include('myapp3.urls')),

]
