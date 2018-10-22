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
import boto3
from manager import BotManager

os.environ["AWS_ACCESS_KEY_ID"] = "ANYTHING"
os.environ["AWS_SECRET_ACCESS_KEY"] = "ANYTHING"
if not os.getenv("DYNAMODB_END_POINT_URL"):
    os.environ["DYNAMODB_END_POINT_URL"] = "http://localhost:8083"
os.environ["AWS_DEFAULT_REGION"] = "us-west-2"

TABLE_NAME = "test_table"
KEY_SCHEMA = {'AttributeName': 'username', 'KeyType': 'HASH'}
ATTRIBUTE_DEFINITIONS = {'AttributeName': 'username', 'AttributeType': 'S'}
ITEM = {'username': 'John'}

CHAT_ID = 50997910


################################################################################
class TestUnit (unittest.TestCase):
    # ==========================================================================
    def setUp(self):
        self.dynamodb = boto3.resource(
            'dynamodb', endpoint_url='http://192.168.10.18:8083')

        self.manager = BotManager()

    # ==========================================================================
    def tearDown(self):
        pass

    # ==========================================================================
    def test_100_table_create(self):
        table = self.dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[KEY_SCHEMA],
            AttributeDefinitions=[ATTRIBUTE_DEFINITIONS],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,'WriteCapacityUnits': 5}
        )
        table.meta.client.get_waiter('table_exists').wait(TableName=TABLE_NAME)
        self.assertEqual(table.item_count, 0)

    # ==========================================================================
    def test_101_table_existing(self):
        table = self.dynamodb.Table(TABLE_NAME)
        self.assertTrue(bool(table.creation_date_time))

    # ==========================================================================
    def test_102_put_item(self):
        table = self.dynamodb.Table(TABLE_NAME)
        table.put_item(Item=ITEM)
        self.assertEqual(table.item_count, 1)

    # ==========================================================================
    def test_103_get_item(self):
        table = self.dynamodb.Table(TABLE_NAME)
        response = table.get_item(Key=ITEM)
        self.assertEqual(ITEM, response['Item'])

    # ==========================================================================
    # def test_104_delete_table(self):
    #     table = self.dynamodb.Table(TABLE_NAME)
    #     table.delete()
    #     table.wait_until_not_exists()

    # ==========================================================================
    def test_200_set_enable_bot(self):
        ret = self.manager.set_enable_bot(CHAT_ID, True)

        self.assertTrue(ret)


    def test_210_add_new_account(self):
        ret = self.manager.add_new_account(CHAT_ID, "test", "password123")
        self.assertTrue(ret)


