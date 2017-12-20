from django.test import TestCase

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from accounts.models import User
import forum.views
import forum.models


class ForumPageTest(TestCase):
    def setUp(self):
        super(ForumPageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('demo123')
        self.user.save()

    def test_page_resolves(self):
        expected = resolve('/forum/')
        self.assertEqual(expected.func, forum.views.forum)

    def test_page_status_code(self):
        page = self.client.get('/forum/')
        self.assertEqual(page.status_code, 200)