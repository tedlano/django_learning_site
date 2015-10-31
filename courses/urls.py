# ********* Step 15 addition start *********
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.course_list, name='list'),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail, name='step'), # Step 26.2 add
    url(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),  # Step 22.2 add
]
# ********* Step 15 addition end *********