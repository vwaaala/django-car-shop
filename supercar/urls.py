from django.urls import path
from .views import (
    HomeView,
    ItemDetailView,
    CheckoutView,
    OrderSummaryView,
    add_to_cart,
    AddCouponView,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)
app_name = 'supercar'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>,', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('<slug>', ItemDetailView.as_view(), name='item-detail'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')

]
