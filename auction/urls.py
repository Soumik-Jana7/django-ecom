from django.urls import path

from . import views

print('request was redirected here---------------------------------')

urlpatterns = [
    path('', views.auction, name='auction'),
    path('/auc_product/<int:myid>', views.auc_product, name='auc_product'),
    path('/user', views.register, name="register")
]