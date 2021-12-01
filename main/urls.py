from django.urls import path, include

from main.views import index, UserLoginView, profile, UserLogOutView, ChangeUserInfoView, UserPasswordChangeView, \
    DeleteUserView, RegisterUserView, RegisterDoneView, other_page, cats_page, upload

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/profile/password/change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', UserLogOutView.as_view(), name='logout'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('upload/', upload, name='upload'),
    path('cats/', cats_page, name='cats'),
    path('<str:page>/', other_page, name='other'),
    # path('test/', include('django.contrib.auth.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
