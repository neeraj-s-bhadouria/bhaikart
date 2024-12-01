from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login
from .views.profile import logout, show_cart, check_out, order

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout),
    path('cart', show_cart),
    path('checkout', check_out),
    path('orders', order),
]