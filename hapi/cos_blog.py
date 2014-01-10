from base import BaseClient
import simplejson as json
from urllib import urlencode

BLOG_API_VERSION = '2'

class COSBlogClient(BaseClient):
  
    # Blogs
    def _get_path(self, subpath):
        return 'content/api/v%s/%s' % (BLOG_API_VERSION, subpath)

    def get_blogs(self, **options):
        return self._call('blogs', **options)

    def get_blog(self, blog_id, **options):
        return self._call('blogs/%s' % blog_id, **options)

    def get_blog_versions(self, blog_id, **options):
        return self._call('blogs/%s/versions' % blog_id, **options)

    def get_blog_version(self, blog_id, version_id, **options):
        return self._call('blogs/%s/versions/%s' % (blog_id, version_id), **options)

    # Blog Posts
    def create_post(self, content_group_id, name, blog_author_id=None,
                    campaign=None, campaign_name=None, footer_html=None, head_html=None,
                    is_draft=None, meta_description=None, meta_keyworks=None,
                    post_body=None, post_summary=None, publish_date=None,
                    publish_immediately=None, slug=None, topic_ids=None, widgets=None, **options):
        allowed_fields = ('blog_author_id', 'campaign', 'campaign_name', 'content_group_id',
                          'footer_html', 'head_html', 'is_draft', 'meta_description', 'meta_keyworks',
                          'name', 'post_body', 'post_summary', 'publish_date', 'publish_immediately',
                          'slug', 'topic_ids', 'widgets')

        data = {}
        for k in allowed_fields:
            if locals().get(k) is not None:
                data[k] = locals().get(k)
        return self._call('blog-posts', data=json.dumps(data), method='POST',
                          content_type='application/json',**options)

    def get_posts(self, query={}, **options):
        return self._call('blog-posts', query=urlencode(query), **options)

    # Update Blog Post
    # Delete Blog Post
    # Get Blog Post by ID
    # Update Auto-Save Buffer
    # Get Auto-Save Buffer
    # Clone Blog Post
    # Has Auto-Save Buffered Changes
    # Publish/Unpublish Blog Post
    # Push Auto-Save Buffer to Live
    # Undelete Blog Post
    # Validate Auto-Save Buffer Version
    # List Previous Versions of Blog Post
    # Restore Previous Version of Blog Post

    # Blog Authors
    # ------------
    # Create Author
    # List Authors
    # Update Author
    # Delete Author
    # Get Author
    # Undelete Author

    # Topics
    # ------
    # Create Topic
    # List Topics
    # Update Topic
    # Delete Topic
    # Get Topic
    # Undelete Topic
