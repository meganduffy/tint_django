# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from accounts.models import User
import accounts.views
import accounts.models

"""
I have NO content tests due to the bootstrap tags conflict
"""


class RegisterPageTest(TestCase):
    def setUp(self):
        super(RegisterPageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('demo123')
        self.user.save()

    def test_page_resolves(self):
        expected = resolve('/register/')
        self.assertEqual(expected.func, accounts.views.register)

    def test_page_status_code(self):
        page = self.client.get('/register/')
        self.assertEqual(page.status_code, 200)


class ProfilePageTest(TestCase):
    def setUp(self):
        super(ProfilePageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('demo123')
        self.user.save()

    def test_page_resolves(self):
        expected = resolve('/profile/')
        self.assertEqual(expected.func, accounts.views.profile)

    def test_page_status_code(self):
        page = self.client.get('/profile/')
        self.assertEqual(page.status_code, 302)

    def test_page_logged_in_content(self):
        self.client.login(username='testuser', password='demo123')
        page = self.client.get('/profile/')
        page_template_output = render_to_response("profile.html", {'user': self.user}).content
        self.assertEqual(page.content, page_template_output)

    def test_page_logged_status_code(self):
        self.client.login(username='testuser', password='demo123')
        page = self.client.get('/profile/')
        self.assertEqual(page.status_code, 200)


class EditProfilePageTest(TestCase):
    def setUp(self):
        super(EditProfilePageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('demo123')
        self.user.save()

    def test_page_resolves(self):
        expected = resolve('/profile/editprofile/')
        self.assertEqual(expected.func, accounts.views.edit_profile)

    def test_page_status_code(self):
        page = self.client.get('/profile/editprofile/')
        self.assertEqual(page.status_code, 302)

    def test_paged_logged_in_code(self):
        self.client.login(username='testuser', password='demo123')
        page = self.client.get('/profile/editprofile/')
        self.assertEqual(page.status_code, 200)


class LoginPageTest(TestCase):
    def setUp(self):
        super(LoginPageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('demo123')
        self.user.save()

    def test_page_resolves(self):
        expected = resolve('/login/')
        self.assertEqual(expected.func, accounts.views.login)

    def test_page_status_code(self):
        page = self.client.get('/login/')
        self.assertEqual(page.status_code, 200)

    def test_paged_logged_status_in_code(self):
        self.client.login(username='testuser', password='demo123')
        page = self.client.get('/login/')
        self.assertEqual(page.status_code, 200)


class LogoutPageTest(TestCase):
    def setUp(self):
        super(LogoutPageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('demo123')
        self.user.save()

    def test_page_resolves(self):
        expected = resolve('/logout/')
        self.assertEqual(expected.func, accounts.views.logout)

    def test_page_status_code(self):
        page = self.client.get('/logout/')
        self.assertEqual(page.status_code, 302)

    def test_paged_logged_status_code(self):
        self.client.login(username='testuser', password='demo123')
        page = self.client.get('/logout/')
        self.assertEqual(page.status_code, 302)
