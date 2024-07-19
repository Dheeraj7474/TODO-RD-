from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
    path('api/', RedirectView.as_view(url='/api/todos/', permanent=False)),
]
