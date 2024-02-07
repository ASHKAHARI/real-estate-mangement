from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home_view, name='listing-home'),
    path('detail/<int:id>/', views.listings_detail.as_view(), name='detail'),
    path('update/<int:id>/', views.update_view.as_view(), name='update'),
    path('delete/<int:id>/', views.delete_view.as_view(), name='delete'),
    path('create/', views.ListingCreate.as_view(), name='create'),
    
]
