#!/usr/bin/env python
# coding=utf8

"""
====================================
 :mod: Test case for Config Module
====================================
.. module author:: 임덕규 <hong18s@gmail.com>
.. note:: MIT License
"""

import unittest
import os

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

import lambda_function
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

TEST_EVENT = {
  "message": {
    "chat": {
      "id": CHAT_ID,
      "first_name": "덕규",
      "last_name": "임",
      "type": "private"
    },
    "text": "안녕하세요"
  }
}

TEST_EVENT_START = {
  "message": {
    "chat": {
      "id": CHAT_ID,
      "first_name": "덕규",
      "last_name": "임",
      "type": "private"
    },
    "text": "/start"
  }
}


################################################################################
class TestUnit (unittest.TestCase):
    # ==========================================================================
    def setUp(self):
        pass

    # ==========================================================================
    def tearDown(self):
        pass

    # ==========================================================================
    def test_start(self):
        res = lambda_function.lambda_handler(TEST_EVENT_START, {})



    # ==========================================================================
    def test_stop(self):
        pass

    # ==========================================================================
    def test_new_account(self):
        pass

    # ==========================================================================

    # def test_lambda_handler(self):
    #     context = {}
    #     lambda_function.lambda_handler(TEST_EVENT, context)

