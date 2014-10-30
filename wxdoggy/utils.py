#! -*- coding: utf8 -*-

import json
import random

import requests


def random_str(length=8):
    chars = '01234567890abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(length):
        result += random.choice(chars)
    return result


class WeixinException(Exception):
    def __init__(self, code, msg):
        msg = '%s: %s' % (code, msg)
        super(WeixinException, self).__init__(msg)


def _do_http_request(url, method='GET', headers=None, data=None):
    method = method.lower()
    assert method in ('get', 'post'), u'只支持GET和POST请求'
    func = requests.get if method == 'get' else requests.post

    resp = func(url, data=data, headers=headers)
    obj = json.loads(resp.content)
    if 'errcode' in obj:
        raise WeixinException(obj['errcode'], obj['errmsg'])

    return obj


def http_get(url, headers=None):
    return _do_http_request(url, headers=headers)


def http_post(url, headers=None, data=None):
    return _do_http_request(url, 'POST', headers=headers,data=data)
