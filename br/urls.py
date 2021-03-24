from django.urls import re_path

from br.views import accounts as accounts_views
from br.views import requirement as requirement_views

urlpatterns = [
    re_path(r'^sign-in/$', accounts_views.sign_in, name='sign-in'),
    re_path(r'^login/$', accounts_views.log_in, name='login'),
    re_path(r'^logout/$', accounts_views.log_out, name='logout'),
]

urlpatterns += [
    re_path(r'^requirement/edit/$', requirement_views.requirement, name='requirement-edit'),
]
