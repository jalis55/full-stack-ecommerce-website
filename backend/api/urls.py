from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from api.views import CategoryViewset,ProductViewset


router = routers.DefaultRouter()

router.register("categories",CategoryViewset)
router.register("products",ProductViewset)

urlpatterns = [
     path("", include(router.urls)),
    
]