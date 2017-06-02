# -*- encoding: utf-8 -*-

import os
import time
from slackclient import SlackClient

# 재용봇 토큰. 환경변수로 써야 안전할 듯.
SLACK_BOT_TOKEN = 'xoxb-190480237911-JfpWBvKml0P6tnYqHe4RlPrI'

# 재용봇 아이디
BOT_ID = 'W5KH4N47M'

# constants
AT_BOT = "<@" + BOT_ID + ">"
START_COMMAND = "야"

# 슬랙 클라이언트 초기화
slack_client = SlackClient(SLACK_BOT_TOKEN)


def handle_command(command, channel):
    """
        명령어를 읽고 반응한다.
    """
    response = "제가 아무말이나 하고 있는 것 같지만 진짜 아무말이나 하는 거 맞습니다."
    if command.startswith(START_COMMAND):
        response = "왜"
    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        slack output parser
    """
    ret = None, None
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                ret = output['text'].split(AT_BOT)[1].strip().lower(), output['channel']
    return ret


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print("재용봇 실행 성공!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("접속 실패. 토큰 혹은 ID를 확인해 보셈.")