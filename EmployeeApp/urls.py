
from django.contrib import admin
from django.urls import path,include

# student api views
from employees_app.api_views import StudentAPI

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employees_app.urls')),
    path('accounts/', include('employees_app.accounts_urls')),
    path('employees-api/', StudentAPI.as_view(), name='employee_api'),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
