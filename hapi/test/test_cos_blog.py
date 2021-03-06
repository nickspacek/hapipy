from __future__ import with_statement
import unittest2
import helper
import logger
from pprint import pprint
import simplejson as json
from nose.plugins.attrib import attr
from datetime import datetime

from hapi.cos_blog import COSBlogClient

class BlogClientTest(unittest2.TestCase):
    """ 
    Unit tests for the HubSpot Blog API Python wrapper (hapipy) client.
    
    This file contains some unittest tests for the Blog API.
    
    Questions, comments, etc: http://docs.hubapi.com/wiki/Discussion_Group
    """
    BLOG_ID = 351076997
    VERSION_ID = 12926383
    
    def setUp(self):
        self.client = COSBlogClient(**helper.get_options())
    
    def tearDown(self):
        pass
    
    # Blogs
    @attr('api')
    def test_get_blogs(self):
        blogs = self.client.get_blogs()
        self.assertTrue(len(blogs))
        pprint(blogs)

    @attr('api')
    def test_get_blog(self):
        blog = self.client.get_blog(self.BLOG_ID)
        self.assertTrue(blog)
        self.assertTrue(blog['id'] == self.BLOG_ID)
        pprint(blog)

    @attr('api')
    def test_get_blog_versions(self):
        versions = self.client.get_blog_versions(self.BLOG_ID)
        self.assertTrue(versions)
        pprint(versions)

    @attr('api')
    def test_get_blog_version(self):
        version = self.client.get_blog_version(self.BLOG_ID, self.VERSION_ID)
        self.assertTrue(version)
        pprint(version)

    # Blog Posts
    @attr('api')
    def test_create_post(self):
        post = self.client.create_post(content_group_id=self.BLOG_ID, name="Test Blog Post")
        pprint(post)
        self.assertTrue(post)

    @attr('api')
    def test_get_posts(self):
        posts = self.client.get_posts(query={'name': 'Demonstration Blog Post'})
        pprint(posts)
        self.assertTrue(posts)

    @attr('api')
    def test_update_post(self):
        post = self.client.update_post(blog_post_id=348109414, name="Updated Test Blog Post")
        pprint(post)
        self.assertTrue(post)

    @attr('api')
    def test_delete_post(self):
        post = self.client.delete_post(blog_post_id=348109414)
        pprint(post)
        self.assertTrue(post)
        post = self.client.undelete_post(blog_post_id=348109414)
        pprint(post)
        self.assertTrue(post)

    @attr('api')
    def test_undelete_post(self):
        post = self.client.undelete_post(blog_post_id=348109414)
        pprint(post)
        self.assertTrue(post)

    @attr('api')
    def test_get_post(self):
        post = self.client.get_post(blog_post_id=348109414)
        pprint(post)
        self.assertTrue(post)

    @attr('api')
    def test_update_auto_save_buffer(self):
        post = self.client.update_auto_save_buffer(blog_post_id=348109414, name="Updated Test Post Buffer")
        pprint(post)
        self.assertTrue(post)

    @attr('api')
    def test_get_auto_save_buffer(self):
        post = self.client.get_auto_save_buffer(blog_post_id=348109414)
        pprint(post)
        self.assertTrue(post)

    @attr('api')
    def test_clone_post(self):
        post = self.client.clone_post(blog_post_id=348109414, name="Cloned Blog Post")
        pprint(post)
        self.assertTrue(post)

    @attr('api')
    def test_get_buffered_changes(self):
        post = self.client.get_buffered_changes(blog_post_id=348109414)
        pprint(post)
        self.assertTrue(post)

    @attr('api')
    def test_publish_post(self):
        post = self.client.publish_post(blog_post_id=348109414, action='schedule-publish')
        pprint(post)
        self.assertTrue(post)
        post = self.client.publish_post(blog_post_id=348109414, action='push-buffer-live')
        pprint(post)
        self.assertTrue(post)
        post = self.client.publish_post(blog_post_id=348109414, action='cancel-publish')
        pprint(post)
        self.assertTrue(post)
        with self.assertRaises(ValueError):
            self.client.publish_post(blog_post_id=348109414, action='invalid-action')

    @attr('api')
    def test_push_buffer_live(self):
        post = self.client.push_buffer_live(blog_post_id=348109414)
        pprint(post)
        self.assertTrue(post)

    @attr('api')
    def test_validate_buffer(self):
        post = self.client.validate_buffer(blog_post_id=348109414)
        pprint(post)
        self.assertTrue(post)

    @attr('api')
    def test_get_post_versions(self):
        response = self.client.get_post_versions(blog_post_id=348109414)
        pprint(response)
        self.assertTrue(response)

        version_id = response[0]['version_id']
        response = self.client.get_post_version(blog_post_id=348109414, version_id=version_id)
        pprint(response)
        self.assertTrue(response)

        response = self.client.restore_post_version(blog_post_id=348109414, version_id=version_id)
        pprint(response)
        self.assertTrue(response)

    @attr('api')
    def test_create_delete_author(self):
        full_name = "Test Author " + datetime.now().strftime('%Y%m%d%H%M%S')
        response = self.client.create_author(email='test@example.com', full_name=full_name)
        pprint(response)
        self.assertTrue(response)

        author_id = response['id']

        response = self.client.update_author(author_id=author_id, email="new-email@example.com")
        pprint(response)
        self.assertTrue(response)

        response = self.client.delete_author(author_id=author_id)
        pprint(response)
        self.assertTrue(response)

        authors = self.client.undelete_author(author_id=author_id)
        pprint(authors)
        self.assertTrue(authors)

        response = self.client.delete_author(author_id=author_id)
        pprint(response)
        self.assertTrue(response)

    @attr('api')
    def test_get_authors(self):
        response = self.client.get_authors(query={'full_name': 'Hub Spot'})
        pprint(response)
        self.assertTrue(response)

        author = self.client.get_author(author_id=response['objects'][0]['id'])
        pprint(author)
        self.assertTrue(author)

    @attr('api')
    def test_get_topics(self):
        response = self.client.get_topics()
        pprint(response)
        self.assertTrue(response)

        topic_id = response['objects'][0]['id']
        response = self.client.get_topic(topic_id=topic_id)
        pprint(response)
        self.assertTrue(response)

    @attr('api')
    def test_create_update_delete_undelete_topic(self):
        name = "Test Topic " + datetime.now().strftime('%Y%m%d%H%M%S')
        response = self.client.create_topic(name=name)
        pprint(response)
        self.assertTrue(response)

        topic_id = response['id']

        name = "New " + name
        response = self.client.update_topic(topic_id=topic_id, name=name)
        pprint(response)
        self.assertTrue(response)

        response = self.client.delete_topic(topic_id=topic_id)
        pprint(response)
        self.assertTrue(response)

        response = self.client.undelete_topic(topic_id=topic_id)
        pprint(response)
        self.assertTrue(response)

        response = self.client.delete_topic(topic_id=topic_id)
        pprint(response)
        self.assertTrue(response)

if __name__ == "__main__":
    unittest2.main()
