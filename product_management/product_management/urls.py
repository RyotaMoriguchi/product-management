from django.conf.urls import url, include   # ←, includeを追加
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pro/', include('pro.urls')),
]