from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('administration.urls')),
    # path('academic/', include('academic.urls')),
    # path('account/', include('account.urls')),
    # path('attendance/', include('attendance.urls')),
    # path('', include('core.urls')),
    # path('employee/', include('employee.urls')),
    # path('event/', include('event.urls')),
    # path('finance/', include('finance.urls')),
    # path('parents/', include('parents.urls')),
    # path('result/', include('result.urls')),
    # path('student/', include('student.urls')),
    # path('teacher/', include('teacher.urls')),
    # path('advanced_filters/', include('advanced_filters.urls'))
]
# if settings.DEBUG:
    
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)