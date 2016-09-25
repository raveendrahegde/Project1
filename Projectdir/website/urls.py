from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

try:
	from market import views as market_views
	from login import views as login_views
except Exception as e:
	print e


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    url(r'^login$', login_views.loginpage),
    url(r'^dologin$', login_views.doLogin),
    url(r'^logout$', login_views.doLogout),

    url(r'^$', market_views.home),
    url(r'^home$', market_views.home),
    url(r'^valuate$', market_views.valuate),
)
