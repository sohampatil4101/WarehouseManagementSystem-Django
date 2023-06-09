from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home" ),
    path('about',views.about, name="about" ),
    path('contact',views.contact, name="contact" ),
    path('register',views.register, name="register" ),
    path('login',views.login, name="login" ),
    path('logout',views.logout, name="logout" ),
    path('addwarehouse',views.addwarehouse, name="addwarehouse" ),
    path('deletewarehouse/<str:obj1>/<str:obj2>',views.deletewarehouse, name="deletewarehouse" ),
    path('viewhouse/<str:obj1>/<str:obj2>',views.viewhouse, name="viewhouse" ),
    path('deleteproduct/<str:obj1>/<str:obj2>/<str:obj3>',views.deleteproduct, name="deleteproduct" ),
    path('addproduct/<str:obj1>',views.addproduct, name="addproduct" ),
    path('expiredproduct/<str:obj1>',views.expiredproduct, name="expiredproduct" ),
    path('search/<str:obj1>',views.search, name="search" )
]

if settings.DEBUG :
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# latest 14-03-2023