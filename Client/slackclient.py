import os
from slack_sdk import WebClient
from dotenv import load_dotenv
from pathlib import Path

#load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
slack_token = os.environ["SLACK_BOT_TOKEN"]


class SlackCLient():
    """
    Used to start slack client and hook into api

    chan: 
        (str) the channel we want to load into to start 
    """
    def __init__(self,chan):
        self.client = WebClient(token=slack_token)
        self.chan = chan

    def message(self,message):
        """
        Post message to current channel

        message:
            (str) the message to post 

        return:
            (bool) message delivered
            if not message not string return -1
        """
        if isinstance(message,str):
            return self.client.chat_postMessage(channel=self.chan,text=message)
        else:
            return -1

    def channel(self,chan):
        """
        changes slack channel to post in 

        channel:
            (str) the new channel to post message in 

        return 
            (int) if not a string return -1 
        """
        self.chan = chan