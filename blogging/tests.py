from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post, Category
import datetime


# Create your tests here.


class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json',]

    def setup(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CatalogTestCase(TestCase):

    def test_string_representation(self):
        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)

class FrontEndTestCase(TestCase):

    fixtures = ['blogging_test_fixture.json']

    def setup(self):
        self.now = datetime.datetime.now()
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count, text = "foo", author = author)

            if count < 6:
                pubdate = self.now - self.timedelta * count
                post.published = pubdate
            post.save()

    def test_list_only_published(self):
        resp = self.client.get('/')
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("Recent Posts" in resp_text)
        for count in range(1, 11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)



