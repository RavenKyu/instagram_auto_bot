import json
import os
import urllib3


TOKEN = os.getenv('TOKEN')
if not TOKEN:
    raise ValueError("Telegram bot TOKEN is required.")
BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

# 명령어
CMD_START = '/start'
CMD_NEW_ACCOUNT = '/new'


################################################################################
def lambda_handler(event, context):
    # TODO implement


    message = ""

    user_id = event['message']['chat']['id']
    user_first_name = event['message']['chat']['first_name']
    user_last_name = event['message']['chat']['last_name']
    text = event['message']['text']

    if not text:
        return {"statusCode": 200, "body": json.dumps('No Text')}

    if CMD_START == text:
        users, message = cmd_start(
            user_id, user_first_name, user_last_name, text)

    elif CMD_NEW_ACCOUNT == text:
        return

    else:
        user, message = (user_id, "알 수 없는 명령어 입니다.")

    try:
        for user in users:
            send_message(user, message)
        status = {
            "statusCode": 200,
            "body": json.dumps('Hello from Lambda!' + str(event))
        }

    except Exception as e:
        status = {
            "statusCode": 200,
            "body": json.dumps('Hello from Lambda!' + str(event))
        }
    return status


################################################################################
def cmd_start(chat_id, user_f_name, user_l_name, text):
    users = [chat_id, ]
    message = "안녕하세요. {l_name} 님.".format(**{'l_name': user_l_name})
    return users, message


################################################################################
def cmd_stop(chat_id):
    return


################################################################################
def cmd_new_account(chat_id):
    return


################################################################################
def send_message(chat_id, text, reply_to=None, no_preview=True, keyboard=None):
    """
    :param chat_id:(integer) 메시지를 보낼 채팅 ID
    :param text:(string)  메시지 내용
    :param reply_to:(integer) ~메시지에 대한 답장
    :param no_preview:(boolean) URL 자동 링크(미리보기) 끄기
    :param keyboard:  (list)    커스텀 키보드 지정
    :return:
    """
    params = {
        'chat_id': str(chat_id),
        'text': text,
        # 'text': text.encode('utf-8'),
    }

    if reply_to:
        params['reply_to_message_id'] = reply_to
    if no_preview:
        params['disable_web_page_preview'] = no_preview
    if keyboard:
        reply_markup = json.dumps({
            'keyboard': keyboard,
            'resize_keyboard': True,
            'one_time_keyboard': False,
            'selective': (reply_to != None),
        })
        params['reply_markup'] = reply_markup

    http = urllib3.PoolManager()
    res = http.request(
        'POST',
        BASE_URL + 'sendMessage', fields=params)
    # print(res.url)
    res.close()
#    except Exception as e:
 #       print("error", e)
        # logging.exception(e)