from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from tweets import views as tweets_views
from users import views as users_views

urlpatterns = [
    path('', include("users.urls")),
    path('', include("tweets.urls")),
    path('profiles/', include("profiles.urls")),

    # Simple JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
