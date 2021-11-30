from django.urls import path, include

from main.views import index, UserLoginView

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]