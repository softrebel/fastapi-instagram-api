import os,requests
from datetime import datetime
import json
class LoginFailedException(Exception):
    pass

class InstagramHandler():

    def __init__(self):
        self.csrf_token = None
        self.session_id = None
        self.csrf_link = 'https://www.instagram.com/api/v1/web/qp/batch_fetch_web/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "X-Xequested-Xith": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "www.instagram.com",
            "Origin": "https://www.instagram.com"
        }

        self.is_proxy_enabled = os.getenv("IS_PROXY_ENABLED")
        self.login_url = f"https://www.instagram.com/accounts/login/ajax/"
        self.payload = {
            'username': '{username}',
            'enc_password': 'PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
            'queryParams': "{}",
            'optIntoOneTap': 'false',
            'stopDeletionNonce': "",
            'trustedDeviceRecords': "{}"
        }

    def login(self,username, password):
        time = int(datetime.now().timestamp())
        self.get_csrf_token()

        pyaload=self.payload
        pyaload['username']=username
        pyaload['enc_password']=pyaload['enc_password'].format(password=password,time=time)

        headers=self.headers
        headers['X-CSRFToken']=self.csrf_token
        arugments = {'headers': headers}
        if self.is_proxy_enabled:
            arugments['proxies'] = {
                'http': os.getenv("PROXY_HTTP"),
                'https': os.getenv("PROXY_HTTPS"),
            }
        arugments['data']=pyaload
        response = requests.post(self.login_url,**arugments)
        if response.status_code != 200:
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
        else:
            raise LoginFailedException("login information is incorrect", response.text)

    def get_csrf_token(self):
        arugments = {'headers': self.headers}
        if self.is_proxy_enabled:
            arugments['proxies'] = {
                'http': os.getenv("PROXY_HTTP"),
                'https': os.getenv("PROXY_HTTPS"),
            }

        response = requests.get(self.csrf_link, **arugments)
        self.csrf_token = response.cookies['csrftoken']

