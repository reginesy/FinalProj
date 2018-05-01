from django.urls import path
from . import views

urlpatterns =[
	path('', views.index, name='index'),
	path('items/', views.ItemListView.as_view(), name='items'),
	path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
	path('owners/', views.OwnerListView.as_view(), name='owners'),
	path('owner/<int:pk>', views.OwnerDetailView.as_view(), name='owner-detail'),
	path('myitems/', views.LoanedItemsListView.as_view(), name='my-borrowed'),
]