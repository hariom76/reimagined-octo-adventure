from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('trans/',views.trans,name='trans'),
    path('confirm/<int:id1>/<int:id2>',views.confirm,name='confirm')
]