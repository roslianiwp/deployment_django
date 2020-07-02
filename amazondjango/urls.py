from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('tv/<int:id>',views.producttv ),
    path('shofa/<int:id>',views.productshofa),
    path('listing-shofa/',views.listingshofa, name='listing'),
    path('listing-tv/',views.listingtv, name='listing-tv'),
    path('search/',views.SearchResultView, name='search'),
]

 
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
