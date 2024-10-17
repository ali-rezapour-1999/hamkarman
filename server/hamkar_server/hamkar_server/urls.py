from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from axes.decorators import axes_dispatch

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/login/', axes_dispatch(TokenObtainPairView.as_view()), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('auth/' , include('users.urls')),
    path('profile/' , include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


