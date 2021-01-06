from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from student.controllers.dashboard_controller import index

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='home'),
    path('students/', include('student.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
