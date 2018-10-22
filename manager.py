payload = {
        'TableName': 'test'
}

import boto3
import redis
import time

TABLE_CHAT_ID = "chat_id"
TABLE_INSTAGRAM_ACCOUNT = "instagram_account"

class DB:
    def __init__(self, table):
        pass


################################################################################
class BotManager:
    # ==========================================================================
    def __init__(self):
        self.rc = redis.Redis(
            host="localhost")

    # ==========================================================================
    def set_enable_bot(self, chat_id, enable):
        try:
            db = boto3.resource(
                'dynamodb', endpoint_url='http://192.168.10.18:8083')
            table = db.Table(TABLE_CHAT_ID)
            table.put_item(chat_id, enable)
        except Exception as e:
            return False
        return True

    # ==========================================================================
    def add_new_account(self, chat_id, insta_id, insta_password):
        try:
            db = boto3.resource(
                'dynamodb', endpoint_url='http://192.168.10.18:8083')
            table = db.Table(TABLE_INSTAGRAM_ACCOUNT)
            table.put_item(Item={
                "chat_id": chat_id,
                "insta_id": insta_id,
                "insta_password": insta_password,
                "created_date": time.time(),
                "expired_date": time.time() + 5.256e+6,  # 2 months
                "status": False
            })
        except Exception as e:
            return False
        return True

    def get_enable_bot(self, chat_id):
        db = boto3.resource(
            'dynamodb', endpoint_url='http://192.168.10.18:8083')
        table = db.Table(TABLE_CHAT_ID)
        table.get_item(Key={
            'chat_id'
        })
