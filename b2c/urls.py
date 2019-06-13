from django.conf.urls import include, url
from django.contrib import admin
from myadmin import views as v
urlpatterns = [
    # Examples:
    # url(r'^$', 'b2c.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/',v.index),
    url(r'^login/',v.login),
    url(r'^register/',v.register),
    url(r'^logout/',v.index),
    url(r'^formtest/',v.index),
    url(r'^captcha/', include('captcha.urls')),
]
