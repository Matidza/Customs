
from django.urls import path
from. import views
from django.contrib.sitemaps.views import sitemap 
from . sitemaps import  ProductSitemap

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
    path('update_password/', views.update_password, name='update_password'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:cat>', views.category, name='category'),
    #path('all/', views.all, name='all'),
    path('search/', views.search, name='search'),
    path('sitemap.xml', sitemap, {'sitemaps': {'product': ProductSitemap}}, name='sitemap'),
]
