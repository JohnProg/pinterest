from django.conf.urls import patterns, url
from views import logout_user, RegisterFormView, HomeTemplateView, LoginFormView, PasswordResetFormView

urlpatterns = patterns('',
                    url(r'^$', HomeTemplateView.as_view(), name='home'),
                    url(r'^logout/$', logout_user, name='logout'),
                    url(r'^register/$', RegisterFormView.as_view(), name='register'),
                    url(r'^login/$', LoginFormView.as_view(), name='login'),
                    url(r'^reset/$', PasswordResetFormView.as_view(), name='reset'),
)