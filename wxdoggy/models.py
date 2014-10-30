#!-*- coding: utf8 -*-


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
    def __init__(self, openid, nickname, sex, subscribe,
        city, province, headimgurl, unionid, **kwargs):
        self.openid = openid
        self.nickname = nickname
        self.sex = sex
        self.subscribe = subscribe
        self.city = city
        self.province = province
        self.headimgurl = headimgurl
        self.unionid = unionid
        self._otherinfo = kwargs
