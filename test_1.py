import pytest
import requests
import yaml
from ddt import ddt, data, unpack

import logging
import http.client as http_client

@ddt
class TestPosts:
    @pytest.mark.usefixtures("auth_token")
    @data("Title1", "Title2", "Title3")
    def test_check_post_title(self, auth_token, title):
        with open("config.yaml", 'r') as f:
            config = yaml.safe_load(f)
            
        post_url = f"{config['base_url']}/api/posts"
        headers = {
            "X-Auth-Token": auth_token
        }
        params = {
            "owner": "notMe"
        }
        
        response = requests.get(post_url, headers=headers, params=params)
        posts = response.json()
        
        assert any(post['title'] == title for post in posts), f"Failed to find post with title {title}"

        
http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True




