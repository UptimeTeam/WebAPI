from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from userss import views as users_views
from postss import views as posts_views

router = routers.DefaultRouter()
router.register(r'users', users_views.UserViewSet)
router.register(r'posts', posts_views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
