"""karibupay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app import views
from karibupay import settings
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.landingpage, name='index'),
    url(r'^home/', views.homepage, name='home'),
    url(r'^login_user/', views.loginuser, name='login'),
    url(r'^register_user/', views.save_user, name='register'),
    url(r'^remove_from_cart/', views.remove_from_cart, name='register'),
    url(r'^add_to_cart/', views.add_to_cart, name='add_to_cart'),
    url(r'^checkout/', views.get_cart, name='add_to_cart'),
    url(r'^proceed_to_pay/', views.request_payment, name='request_payment'),
    url(r'^process_orders/', views.process_order, name='process_orders'),
    url(r'^how_it_works/', views.howitworks, name='process_orders'),
    url(r'^b/', views.barcode, name='process_orders'),
    url(r'^enquiries/', views.send_equiry, name='enquiries'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^(?P<slug>[\w\-]+)/$', views.view_more, name="view more"),
    url(r'^images/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),

]
