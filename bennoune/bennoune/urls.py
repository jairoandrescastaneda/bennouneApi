from django.contrib import admin
from django.urls import path , include


urls = [
    # url(r'^todos/', include('todos.urls')),
    path('', include('users.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls) )
]
