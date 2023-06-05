from django.urls import path

from apps.reception import views

urlpatterns = [
    path('inc_doc', views.IncDocListView.as_view(), name='inc_doc'),
    path('inc_doc_update/<int:pk>', views.IncDocUpdateView.as_view(), name='inc_doc_update'),
    path('inc_doc_delete/<int:pk>', views.IncDocDeleteView.as_view(), name='inc_doc_delete'),
    path('out_doc', views.OutDocListView.as_view(), name='out_doc'),
    path('out_doc_update/<int:pk>', views.OutDocUpdateView.as_view(), name='out_doc_update'),
    path('out_doc_delete/<int:pk>', views.OutDocDeleteView.as_view(), name='out_doc_delete'),
    path('order', views.OrderListView.as_view(), name='order'),
    path('order_update/<int:pk>', views.OrderUpdateView.as_view(), name='order_update'),
    path('order_delete/<int:pk>', views.OrderDeleteView.as_view(), name='order_delete'),
    path('receipt', views.ReceiptListView.as_view(), name='receipt')
]
