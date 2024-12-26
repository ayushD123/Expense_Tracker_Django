
from django.urls import path
from tracker.views import index,delete_transaction

urlpatterns = [
    path('', index),
    path('deleteTrans/<uuid:uuid>/', delete_transaction, name='delete_transaction'),
]
