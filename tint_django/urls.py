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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from paypal.standard.ipn import urls as paypal_urls
from .settings import MEDIA_ROOT
from landing import views as landing_views
from accounts import views as accounts_views
from upload import views as upload_views
from paypal_store import views as paypal_views
from forum import views as forum_views

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
    url(r'^transcriptdetails', upload_views.get_transcript_detail_form, name='transcriptdetails'),
    url(r'^removefile/(?P<upload_id>\d+)/$', upload_views.remove_file, name='removefile'),
    url(r'^orderreview', upload_views.get_order_review, name='orderreview'),
    url(r'^save-order-for-later/(?P<detail_id>\d+)/$', upload_views.save_order_for_later, name='save_order_for_later'),
    url(r'^saved-for-later/$', upload_views.get_saved_for_later, name='saved_for_later'),
    url(r'^transcript-tracker/$', upload_views.get_transcript_tracker, name='transcript_tracker'),
    url(r'^transcript-tracker/new/(?P<detail_id>\d+)/$', upload_views.new_review, name='new_review'),
    url(r'^transcript-tracker/edit/(?P<detail_id>\d+)/(?P<review_id>\d+)/$', upload_views.edit_review, name='edit_review'),

    # Paypal Store
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return, name='paypal-return'),
    url(r'^paypal-cancel', paypal_views.paypal_cancel, name='paypal-cancel'),

    # Forum
    url(r'^forum/$', forum_views.forum, name='forum'),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name="delete_post"),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),
]
