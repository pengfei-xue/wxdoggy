#!-*- coding: utf8 -*-

import requests

from .endpoints import Endpoints as ep
from .models import AccessToken, WxUser


class WeixinException(Exception):
    def __init__(self, code, msg):
        msg = '%s: %s' % (code, msg)
        super(WeixinException, self).__init__(msg)


class Weixin(object):
    def __init__(self, appid, appsecret, token):
        self.appid = appid
        self.appsecret = appsecret
        self.token = token

    def _do_http_request(self, url, method='GET', headers=None, data=None):
        method = method.lower()
        assert method in ('get', 'post'), u'只支持GET和POST请求'
        func = requests.get if method == 'get' else requests.post

        resp = func(url, data=data, headers=headers)
        obj = resp.json()
        if 'errcode' in obj:
            raise WeixinException(obj['errcode'], obj['errmsg'])

        return obj

    def _do_http_get(self, url, headers=None):
        return self._do_http_request(url, headers=headers)

    def _do_http_post(self, url, headers=None, data=None):
        return self._do_http_request(url, 'POST', headers=headers,data=data)

    def get_authorize_url(self, redirect_uri, state=None,
        response_type='code', scope='snsapi_userinfo'):
        endpoint = ep.get_uri4('connect.oauth2.authorize')

        qs = 'appid=%s&redirect_uri=%s&response_type=%s&scope=%s'
        qs = qs % (self.appid, redirect_uri, response_type, scope)
        if state: qs += '&state=%s' % state

        url = '%s?%s#wechat_redirect' % (endpoint, qs)
        return url

    def get_access_token(self, code, grant_type='authorization_code'):
        '''
            http://mp.weixin.qq.com/wiki/index.php?title=网页授权获取用户基本信息
        '''
        endpoint = ep.get_uri4('sns.oauth2.access_token')

        qs = 'appid=%s&secret=%s&code=%s&grant_type=%s' % (self.appid,
            self.appsecret, code, grant_type)

        url = '%s?%s' % (endpoint, qs)
        resp = self._do_http_get(url)
        return AccessToken(**resp)

    def get_userinfo(self, at, openid):
        '''
            http://mp.weixin.qq.com/wiki/index.php?title=获取用户基本信息(UnionID机制)
        '''
        endpoint = ep.get_uri4('sns.userinfo')

        qs = 'access_token=%s&openid=%s&lang=zh_CN' % (at, openid)

        url = '%s?%s' % (endpoint, qs)
        resp = self._do_http_get(url)
        return WxUser(**resp)
