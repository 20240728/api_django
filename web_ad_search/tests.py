from django.test import TestCase
import requests
import json
import pytest
from api_django.qxb_web.config import data
from api_django.qxb_web.lib.func import BaseFunc as BF


# Create your tests here.

class TestAdSearch:
    ad = BF()

    @pytest.fixture(scope="function", autouse=True)
    def init(self, get_env):
        # 判断用例执行环境，返回URL和cookie
        if get_env == 'SIT':
            self.url = data.SIT_URL
            self.cookie = data.SIT_COOKIE
        elif get_env == 'UAT':
            self.url = data.UAT_URL
            self.cookie = data.UAT_COOKIE
        elif get_env == 'PRD':
            self.url = data.PRD_URL
            self.cookie = data.PRD_COOKIE

    def test_search_01(self):
        r = TestAdSearch.ad.web_post(url=self.url, data=data.key_word, headers=data.headers, cookies=self.cookie)
        # print(r.json())
        assert r.status_code == 200
        assert r.json()['totalNum'] != 0

    def test_search_02(self):
        r = self.ad.web_post(url=self.url, data=data.key_word, headers=data.headers, cookies=self.cookie)
        # print(r.json())
        assert r.status_code == 200
        assert r.json()['totalNum'] != 0


if __name__ == '__main__':
    pytest.main(['-s', '-v', './tests.py'])
