from django.urls import path  
from . import views    

urlpatterns =[
    path('', views.index , name='index'),
    path('one', views.one , name='one'),
    path('two', views.two, name='two'),
    path('three', views.three , name='three'),
    path('four', views.four, name='four'),
    path('resultA', views.resultA , name='resultA'),
    path('resultB', views.resultB , name='resultB'),
    path('resultC', views.resultC , name='resultC'),
    path('resultD', views.resultD , name='resultD'),
    



]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
