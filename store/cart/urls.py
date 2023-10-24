from django.urls import path

from cart import views

app_name = "cart"
urlpatterns = [

    path('',views.cart_details,name='cart_details'),
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('remove/<int:product_id>/', views.cart_remove, name='remove'),
    path('fullremove/<int:product_id>/', views.full_remove, name='fullremove'),


    ]