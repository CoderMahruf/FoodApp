from django.urls import path
from . import views

app_name = 'foodApp'
urlpatterns = [
    #/food/
    path('',views.index,name="index"),
    #/food/1
    path('<int:item_id>',views.detail,name="detail"),
    path('item/',views.item,name="item"),
]