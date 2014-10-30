#!-*- coding: utf8 -*-

import random


def random_str(length=8):
    chars = '01234567890abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(length):
        result += random.choice(chars)
    return result
