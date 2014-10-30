#!-*- coding: utf8 -*-

class Endpoints(object):
    _uri_mapping = {
        'connect.oauth2.authorize': 'https://open.weixin.qq.com/connect/oauth2/authorize',
        'sns.oauth2.access_token': 'https://api.weixin.qq.com/sns/oauth2/access_token',
        'sns.userinfo': 'https://api.weixin.qq.com/sns/userinfo',
        'cgibin.user.info': 'https://api.weixin.qq.com/cgi-bin/user/info',
    }

    @classmethod
    def get_uri4(cls, func):
        return cls._uri_mapping.get(func)
