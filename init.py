import os

from venmo_api import Client
from dotenv import load_dotenv
from notifiers import get_notifier
from datetime import datetime

from utils import get_env, env_vars, get_month, Venmo, Telegram

def main(now):

  """
  The main function which initiates the script.
  """

  # take environment variables from .env
  load_dotenv()
  actualVars = []
  for var in env_vars:
    actualVars.append(get_env(var))

  access_token, chat_id, bot_token, friend_id_1, friend_name_1, friend_id_2, friend_name_2, description, specified_day = actualVars

  # specific day of the month to run the script
  specified_day = specified_day

  if now.day != specified_day:
    print(f"Today is not the specified day ({specified_day}), script will not run.")
    return

  month = get_month(now)
  venmo = Venmo(access_token)
  telegram = Telegram(bot_token, chat_id)

  friends =[
    {
      "name": friend_name_1,
      "id": friend_id_1,
    }
  ]

  successfulRequests = []
  expectedRequests = len(friends)

  for friend in friends:
    name = friend["name"]
    id = friend["id"]
    description = description + " — Sent by Erick's Assistant Efron 🤵🏻‍♂"
    amount = 3.50
    message = f"""Good news old sport!

I have successfully requested money from {name}.

— Efron 🤵🏻‍♂️
    """
    success = venmo.request_money(id, amount, description, telegram.send_message(message))
    if success:
      successfulRequests.append(success)

  if len(successfulRequests) == expectedRequests:
    print("✅ Ran script successfully and sent " + str(expectedRequests) + " Venmo requests.")
  else:
    print("❌ Something went wrong. Only sent " + str(len(successfulRequests)) + "/" + str(expectedRequests) + " venmo requests.")

now = datetime.now()
main(now)
