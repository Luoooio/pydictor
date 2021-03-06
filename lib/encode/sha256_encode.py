#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

import hashlib


def sha256_encode(item):
    """sha-256 message digest algorithm"""
    try:
        return (hashlib.sha256(item.encode("utf-8"))).hexdigest()
    except:
        return ''
