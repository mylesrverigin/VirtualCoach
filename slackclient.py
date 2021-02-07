import os
from slack_sdk import WebClient
from dotenv import load_dotenv
from pathlib import Path

#load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
slack_token = os.environ["SLACK_BOT_TOKEN"]


client = WebClient(token=slack_token)

response = client.chat_postMessage(channel=,text=)