from django.urls import path, include

from main.views import index, UserLoginView, profile, UserLogOutView, ChangeUserInfoView, UserPasswordChangeView, \
    DeleteUserView, RegisterUserView, RegisterDoneView, other_page, cats_page, cat_save, PetsListListView, dog_save, \
    dogs_page, pet_delete

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/petslist/', PetsListListView.as_view(), name='pets_list'),
    path('accounts/profile/password/change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', UserLogOutView.as_view(), name='logout'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('catsave/', cat_save, name='cat_save'),
    path('cats/', cats_page, name='cats'),
    path('dogsave/', dog_save, name='dog_save'),
    path('petdelete/', pet_delete, name='pet_delete'),
    path('dogs/', dogs_page, name='dogs'),
    path('<str:page>/', other_page, name='other'),
    # path('test/', include('django.contrib.auth.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
