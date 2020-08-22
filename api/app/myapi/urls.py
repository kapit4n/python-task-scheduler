from django.urls import include, path
from rest_framework import routers
from .views import CreateUserView, UserList, UserInfo, TaskCurrentList, TaskCurrentDetail
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register(r'api/tasks', views.TaskViewSet)
router.register(r'users', CreateUserView)
router.register(r'api/task-logs', views.TaskLogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/request-reset-email/',
         views.RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('api/password-reset/<uidb64>/<token>/',
         views.PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('api/password-reset-complete',
         views.SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    path('api/users/', UserList.as_view()),
    path('api/me/', UserInfo.as_view()),
    path('api/tasks-actions/current/', TaskCurrentList.as_view()),
    path('api/tasks-actions/current/<int:pk>/', TaskCurrentDetail.as_view()),
]
