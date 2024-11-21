from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    #path("", views.book, name="book") 
    #path("",views.student,name="student"),
    #  # Correctly reference the 'book' view
    #path("",views.product,name="product"),
    #path("",views.order,name="order.html"),
    #path("",views.product_details,name="product_details.html"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

]