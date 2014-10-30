#! -*- coding: utf8 -*-

from .endpoints import Endpoints as ep
from .models import AccessToken, WxUser
from .utils import http_get


class Weixin(object):
    def __init__(self, appid, appsecret, token):
        self.appid = appid
        self.appsecret = appsecret
        self.token = token

    def get_authorize_url(self, redirect_uri, state=None,
        response_type='code', scope='snsapi_userinfo'):
        endpoint = ep.get_uri4('connect.oauth2.authorize')

        qs = 'appid=%s&redirect_uri=%s&response_type=%s&scope=%s'
        qs = qs % (self.appid, redirect_uri, response_type, scope)
        if state: qs += '&state=%s' % state

        url = '%s?%s#wechat_redirect' % (endpoint, qs)
        return url

    def get_access_token(self, code, grant_type='authorization_code'):
        endpoint = ep.get_uri4('sns.oauth2.access_token')

        qs = 'appid=%s&secret=%s&code=%s&grant_type=%s' % (self.appid,
            self.appsecret, code, grant_type)

        url = '%s?%s' % (endpoint, qs)
        resp = http_get(url)
        return AccessToken(**resp)

    def get_userinfo(self, at, openid):
        u = WxUser(openid)
        u.get_userinfo(at)
        return u
