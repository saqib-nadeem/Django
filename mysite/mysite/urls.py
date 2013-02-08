from django.conf.urls.defaults import *
from mysite.views import *

urlpatterns = patterns('',
                      (r'^time/$', current_datetime),
					  ('^$', my_homepage_view),
					  (r'^sample-page/$', sample_page_view),
)