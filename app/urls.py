from django.urls import path
from .import views
urlpatterns=[
    path('',views.base,name="base"),
    path('start/',views.start,name='start'),
    path('transfer/',views.transfer,name='transfer'),
    #path('trans/<int:id>',views.trans,name='trans'),
    #path('confirm/<int:id1>/<int:id2>',views.confirm,name='confirm')
]