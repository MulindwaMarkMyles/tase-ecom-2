from django.contrib import admin
from django.urls import path
import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('afterlogin/', views.afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='ecom/logout.html'),name='logout'),
    path('aboutus/', views.aboutus_view),
    path('contactus/', views.contactus_view,name='contactus'),
    path('search/', views.search_view,name='search'),
    path('send-feedback/', views.send_feedback_view,name='send-feedback'),
    path('view-feedback/', views.view_feedback_view,name='view-feedback'),

    path('businessclick/', views.businessclick_view),
    path('businesssignup/', views.business_signup_view),
    path('businesslogin/', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),
    path('business-dashboard/', views.business_dashboard_view,name='admin-dashboard'),

    path('view-customer/', views.view_customer_view,name='view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),

    path('business-products/', views.business_products_view,name='admin-products'),
    path('business-add-product/', views.add_product_view,name='admin-add-product'),
    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('update-product/<int:pk>', views.update_product_view,name='update-product'),

    path('business-view-booking/', views.business_view_booking_view,name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
]