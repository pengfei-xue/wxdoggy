#! -*- coding: utf8 -*-

from .utils import http_get
from .endpoints import Endpoints as ep


class AccessToken(object):
    def __init__(self, access_token, expires_in, refresh_token, openid, scope):
        self.access_token = access_token
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.openid = openid
        self.scope = scope

    def refresh(self):
        pass


class WxUser(object):
    def __init__(self, openid):
        self.openid = openid
        self._info = None

    def __getattr__(self, attr):
        if not (self._info and attr in self._info):
            raise AttributeError(attr)

        return self._info.get(attr)

    def get_userinfo(self, at, lang='zh_CN'):
        endpoint = ep.get_uri4('sns.userinfo')

        qs = 'access_token=%s&openid=%s&lang=%s' % (at, self.openid, lang)

        url = '%s?%s' % (endpoint, qs)
        self._info = http_get(url)

    def get_userinfo_w_unionid(self, at, lang='zh_CN'):
        '''
            NOTE: use this after your develop account been authenticated
            http://mp.weixin.qq.com/wiki/index.php?title=网页授权获取用户基本信息
        '''
        endpoint = ep.get_uri4('cgibin.user.info')

        qs = 'access_token=%s&openid=%s&lang=%s' % (at, self.openid, lang)

        url = '%s?%s' % (endpoint, qs)
        self._info = http_get(url)
