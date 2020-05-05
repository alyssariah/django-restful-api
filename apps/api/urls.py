from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import FoodViewSet, FoodEditSet, PublicFoodSet

router = DefaultRouter()
router.register('food', FoodViewSet, basename='foodlog')

custom_urlpatterns = [
    url(r'^food/(?P<pk>\d+)$', FoodEditSet.as_view(), name='foodedit'),
    url(r'^public/$', PublicFoodSet.as_view(), name='publicfood')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns