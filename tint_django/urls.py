"""tint_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
from landing import views as landing_views
from accounts import views as accounts_views
from upload import views as upload_views

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Media
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT, 'show_indexes': True}),

    # Landing
    url(r'^$', landing_views.get_index, name='index'),
    url(r'^faq/$', landing_views.get_faq, name='faq'),
    url(r'^instantquote/$', landing_views.get_instant_quote, name='instantquote'),
    url(r'^customquote/$', landing_views.get_custom_quote, name='customquote'),
    url(r'^customquoteconfirm/$', landing_views.get_custom_quote_confirm, name='customquoteconfirm'),
    url(r'^contact/$', landing_views.get_contact, name='contact'),
    url(r'^contactconfirm/$', landing_views.get_contact_confirm, name='contactconfirm'),

    # Accounts
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^profile/editprofile/$', accounts_views.edit_profile, name='editprofile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),

    # Upload
    url(r'^uploadfiles/$', upload_views.get_upload_file_form, name='uploadfiles'),
]
