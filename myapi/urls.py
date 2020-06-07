from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token



# router = routers.DefaultRouter()
# router.register(r'ciscorest', views.CiscoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('create', views.api_create_cisco_view, name='rest-create'),
    path('register', views.registration_view, name='rest-register'),
    path('login', obtain_auth_token, name='rest-login'),
    path('<sapid>', views.api_detail_cisco_view, name='rest-detail'),
    path('update/<sapid>', views.api_update_cisco_view, name='rest-update'),
    path('delete/<sapid>', views.api_delete_cisco_view, name='rest-delete'),


    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]