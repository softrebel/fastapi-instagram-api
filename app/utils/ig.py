import os
import requests
from datetime import datetime
import json


class LoginFailedException(Exception):
    pass


class InstagramHandler():

    def __init__(self):
        self.csrf_token = None
        self.session_id = None
        self.config_link = 'https://www.instagram.com/data/shared_data/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "X-Xequested-Xith": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "www.instagram.com",
            "Origin": "https://www.instagram.com",
            'x-ig-app-id': '936619743392459',

        }

        self.is_proxy_enabled = os.getenv("IS_PROXY_ENABLED")
        self.login_url = f"https://www.instagram.com/accounts/login/ajax/"
        self.payload = {
            'username': '{username}',
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
            'queryParams': "{}",
            'optIntoOneTap': 'false',
            'stopDeletionNonce': "",
            'trustedDeviceRecords': "{}"
        }
        self.cookies = {}

        self.link_info = 'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}&='

        self.link_follower = 'https://www.instagram.com/api/v1/friendships/{user_id}/followers/?count=12&search_surface=follow_list_page'

    def login(self, username, password):
        time = int(datetime.now().timestamp())
        self.get_csrf_token()

        pyaload = self.payload
        pyaload['username'] = username
        pyaload['enc_password'] = pyaload['enc_password'].format(
            password=password, time=time)

        headers = self.headers
        headers['X-CSRFToken'] = self.csrf_token
        arugments = {'headers': headers}
        if self.is_proxy_enabled:
            arugments['proxies'] = {
                'http': os.getenv("PROXY_HTTP"),
                'https': os.getenv("PROXY_HTTPS"),
            }
        arugments['data'] = pyaload
        response = requests.post(self.login_url, **arugments)
        if response.status_code != 200:
            print(response.text)
            raise Exception("could not login")
        response_json = json.loads(response.text)
        if response_json["authenticated"]:
            print("login successful")
            cookies = response.cookies
            cookie_jar = cookies.get_dict()
            self.csrf_token = cookie_jar['csrftoken']
            print("csrf_token: ", self.csrf_token)
            self.session_id = cookie_jar['sessionid']
            print("session_id: ", self.session_id)
            self.cookies = response.cookies
        else:
            raise LoginFailedException(
                "login information is incorrect", response.text)

    def get_csrf_token(self):
        arugments = {'headers': self.headers}
        if self.is_proxy_enabled:
            arugments['proxies'] = {
                'http': os.getenv("PROXY_HTTP"),
                'https': os.getenv("PROXY_HTTPS"),
            }

        response = requests.get(self.config_link, **arugments)
        config = json.loads(response.text)
        csrf = config['config']['csrf_token']
        self.csrf_token = csrf

    def get_user_info(self, username):
        self.get_csrf_token()
        headers = self.headers
        headers['X-CSRFToken'] = self.csrf_token
        arugments = {'headers': headers}

        if self.is_proxy_enabled:
            arugments['proxies'] = {
                'http': os.getenv("PROXY_HTTP"),
                'https': os.getenv("PROXY_HTTPS"),
            }

        link = self.link_info.format(username=username)
        response = requests.get(link, cookies=self.cookies, **arugments)
        info = json.loads(response.text)
        response.close()
        return info

    def get_followers(self, username):

        info = self.get_user_info(username)
        if not 'data' in info or 'user' not in info['data']:
            raise Exception('data is not available')
        id = info['data']['user']['id']
        url = self.link_follower.format(user_id=id)

        headers = self.headers
        headers['X-CSRFToken'] = self.csrf_token
        arugments = {'headers': headers}

        if self.is_proxy_enabled:
            arugments['proxies'] = {
                'http': os.getenv("PROXY_HTTP"),
                'https': os.getenv("PROXY_HTTPS"),
            }


        response = requests.get(
            url, cookies=self.cookies, **arugments)
        res = json.loads(response.text)
        users = [{"username": item['username']} for item in res['users']]
        return users
