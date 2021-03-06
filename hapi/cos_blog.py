from base import BaseClient
import simplejson as json
from urllib import urlencode

BLOG_API_VERSION = '2'

class COSBlogClient(BaseClient):
  
    # Blogs
    def _get_path(self, subpath):
        return 'content/api/v%s/%s' % (BLOG_API_VERSION, subpath)

    def get_blogs(self, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blogs'''
        return self._call('blogs', **options)

    def get_blog(self, blog_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blogs_blog_id'''
        return self._call('blogs/%s' % blog_id, **options)

    def get_blog_versions(self, blog_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blogs_blog_id_versions'''
        return self._call('blogs/%s/versions' % blog_id, **options)

    def get_blog_version(self, blog_id, version_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blogs_blog_id_versions_version_id'''
        return self._call('blogs/%s/versions/%s' % (blog_id, version_id), **options)

    # Blog Posts
    @staticmethod
    def _args_to_dict(allowed_fields, **kwargs):
        data = {}
        for k in allowed_fields:
            if kwargs.get(k) is not None:
                data[k] = kwargs.get(k)
        return data

    @classmethod
    def _post_data(cls, **kwargs):
        allowed_fields = ('blog_author_id', 'campaign', 'campaign_name', 'content_group_id',
                          'footer_html', 'head_html', 'is_draft', 'meta_description', 'meta_keywords',
                          'name', 'post_body', 'post_summary', 'publish_date', 'publish_immediately',
                          'slug', 'topic_ids', 'widgets')
        return cls._args_to_dict(allowed_fields, **kwargs)

    def create_post(self, content_group_id, name, blog_author_id=None,
                    campaign=None, campaign_name=None, footer_html=None, head_html=None,
                    is_draft=None, meta_description=None, meta_keywords=None,
                    post_body=None, post_summary=None, publish_date=None,
                    publish_immediately=None, slug=None, topic_ids=None, widgets=None, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/post_blog_posts'''
        data = self._post_data(**locals())
        return self._call('blog-posts', data=json.dumps(data), method='POST',
                          content_type='application/json',**options)

    def get_posts(self, query={}, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blog_posts'''
        return self._call('blog-posts', query=urlencode(query), **options)

    def update_post(self, blog_post_id, content_group_id=None, name=None, blog_author_id=None,
                    campaign=None, campaign_name=None, footer_html=None, head_html=None,
                    is_draft=None, meta_description=None, meta_keywords=None,
                    post_body=None, post_summary=None, publish_date=None,
                    publish_immediately=None, slug=None, topic_ids=None, widgets=None, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/put_blog_posts_blog_post_id'''
        data = self._post_data(**locals())
        return self._call('blog-posts/%s' % blog_post_id, data=json.dumps(data), method='PUT',
                          content_type='application/json',**options)

    def delete_post(self, blog_post_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/delete_blog_posts_blog_post_id'''
        return self._call('blog-posts/%s' % blog_post_id, method='DELETE', **options)

    def get_post(self, blog_post_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blog_posts_blog_post_id'''
        return self._call('blog-posts/%s' % blog_post_id, **options)

    def update_auto_save_buffer(self, blog_post_id, content_group_id=None, name=None, blog_author_id=None,
                                campaign=None, campaign_name=None, footer_html=None, head_html=None,
                                is_draft=None, meta_description=None, meta_keywords=None,
                                post_body=None, post_summary=None, publish_date=None,
                                publish_immediately=None, slug=None, topic_ids=None, widgets=None, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/put_blog_posts_blog_post_id_buffer'''
        data = self._post_data(**locals())
        return self._call('blog-posts/%s/buffer' % blog_post_id, data=json.dumps(data), method='PUT',
                          content_type='application/json',**options)

    def get_auto_save_buffer(self, blog_post_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blog_posts_blog_post_id_buffer'''
        return self._call('blog-posts/%s/buffer' % blog_post_id, **options)

    def clone_post(self, blog_post_id, content_group_id=None, name=None, blog_author_id=None,
                   campaign=None, campaign_name=None, footer_html=None, head_html=None,
                   is_draft=None, meta_description=None, meta_keywords=None,
                   post_body=None, post_summary=None, publish_date=None,
                   publish_immediately=None, slug=None, topic_ids=None, widgets=None, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/post_blog_posts_blog_post_id_clone'''
        data = self._post_data(**locals())
        return self._call('blog-posts/%s/clone' % blog_post_id, data=json.dumps(data), method='POST',
                          content_type='application/json',**options)

    def get_buffered_changes(self, blog_post_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blog_posts_blog_post_id_has_buffered_changes'''
        return self._call('blog-posts/%s/has-buffered-changes' % blog_post_id, **options)

    def publish_post(self, blog_post_id, action, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/post_blog_posts_blog_post_id_publish_action'''
        if action not in ('push-buffer-live', 'schedule-publish', 'cancel-publish'):
            raise ValueError('%s is not a valid action' % action)
        data = {'action': action}
        return self._call('blog-posts/%s/publish-action' % blog_post_id, data=json.dumps(data), method='POST', **options)

    def push_buffer_live(self, blog_post_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/post_blog_posts_blog_post_id_push_buffer_live'''
        return self._call('blog-posts/%s/push-buffer-live' % blog_post_id, method='POST', **options)

    def undelete_post(self, blog_post_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/post_blog_posts_blog_post_id_restore_deleted'''
        return self._call('blog-posts/%s/restore-deleted' % blog_post_id, method='POST', **options)

    def validate_buffer(self, blog_post_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/post_blog_posts_blog_post_id_validate_buffer'''
        return self._call('blog-posts/%s/validate-buffer' % blog_post_id, method='POST', **options)

    def get_post_versions(self, blog_post_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blog_posts_blog_post_id_versions'''
        return self._call('blog-posts/%s/versions' % blog_post_id, **options)

    def get_post_version(self, blog_post_id, version_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blog_posts_blog_post_id_versions_version_id'''
        return self._call('blog-posts/%s/versions/%s' % (blog_post_id, version_id), **options)

    def restore_post_version(self, blog_post_id, version_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/post_blog_posts_blog_post_id_versions_restore'''
        data = {'version_id': version_id}
        return self._call('blog-posts/%s/versions/restore' % blog_post_id, data=json.dumps(data), method='POST', **options)


    # Blog Authors
    def create_author(self, email, full_name, user_id=None, username=None, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/post_blog_authors'''
        data = {
            'email': email,
            'full_name': full_name,
            'user_id': user_id,
            'username': username
        }
        return self._call('blog-authors', data=json.dumps(data), method='POST', content_type='application/json', **options)

    def get_authors(self, query={}, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blog_authors'''
        return self._call('blog-authors', query=urlencode(query), **options)

    def update_author(self, author_id, email=None, full_name=None, user_id=None, username=None, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/put_blog_authors_blog_author_id'''
        data = self._args_to_dict(('email', 'full_name', 'user_id', 'username'), **locals())
        return self._call('blog-authors/%s' % author_id, data=json.dumps(data),
                          method='PUT', content_type='application/json', **options)

    def delete_author(self, author_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/delete_blog_authors_blog_author_id'''
        return self._call('blog-authors/%s' % author_id, method='DELETE', **options)

    def get_author(self, author_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_blog_authors_blog_author_id'''
        return self._call('blog-authors/%s' % author_id, **options)

    def undelete_author(self, author_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/post_blog_authors_blog_author_id_restore_deleted'''
        return self._call('blog-authors/%s/restore-deleted' % author_id, method='POST', **options)

    # Topics
    def create_topic(self, name, slug=None, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/post_topics'''
        data = {'name': name}
        if slug:
            data['slug'] = slug
        return self._call('topics', data=json.dumps(data), method='POST', **options)

    def get_topics(self, query={}, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_topics'''
        return self._call('topics', query=urlencode(query), **options)

    def update_topic(self, topic_id, name=None, slug=None, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/put_topics_topic_id'''
        data = self._args_to_dict(('name', 'slug'), **locals())
        return self._call('topics/%s' % topic_id, data=json.dumps(data),
                          method='PUT', content_type='application/json', **options)

    def delete_topic(self, topic_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/delete_topics_topic_id'''
        return self._call('topics/%s' % topic_id, method='DELETE', **options)

    def get_topic(self, topic_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/get_topics_topic_id'''
        return self._call('topics/%s' % topic_id, **options)

    def undelete_topic(self, topic_id, **options):
        '''https://developers.hubspot.com/docs/methods/blogv2/post_topics_topic_id_restore_deleted'''
        return self._call('topics/%s/restore-deleted' % topic_id, method='POST', **options)

