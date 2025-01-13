from django.urls import path, include
# from . import views
from rest_framework import routers
from .views import BatHighlightsViewSet, get_highlights, get_and_store_new_highlights, delete_first_n_highlights, highlight_list


router = routers.DefaultRouter()
router.register('all_highlights', BatHighlightsViewSet)


urlpatterns = [
    path('highlights/', highlight_list, name='highlight_list'),
    path("get_highlights/", view= get_highlights),
    path("store_new_highlights/", view= get_and_store_new_highlights),
    path("delete_first_n_highlights/", delete_first_n_highlights, name="delete_first_n_highlights"),
    path('', include(router.urls))
]
