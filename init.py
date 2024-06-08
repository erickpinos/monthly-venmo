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

  access_token, chat_id, bot_token, friend_id_1, friend_name_1, send_or_request, amount, description, specified_day, funding_id = actualVars

  # specific day of the month to run the script
  specified_day = int(specified_day)

  if now.day != specified_day:
    print(f"Today is ({now.day}), not the specified day ({specified_day}), script will not run.")
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
    description = description + " — Sent by Erick's assistant Efron 🤵🏻‍♂"
    amount = float(amount)
    message = f"""Good news old sport!
    

I have successfully completed action {send_or_request} ${amount} for {name}.

{description}

— Efron 🤵🏻‍♂
    """
    send_or_request = os.getenv("SEND_OR_REQUEST")

    try:
      if send_or_request == "Send":
        success = venmo.send_money(id, amount, description, funding_id)
      elif send_or_request == "Request":
        success = venmo.request_money(id, amount, description)
      else:
        raise ValueError("Invalid value for send_or_request. Expected 'Send' or 'Request'.")

      if success:
        telegram.send_message(message)
        successfulRequests.append(success)
    except Exception as e:
      print(f"An error occured: {e}")

  if len(successfulRequests) == expectedRequests:
    print("✅ Ran script successfully and sent " + str(expectedRequests) + " Venmo " + send_or_request +".")
  else:
    print("❌ Something went wrong. Sent " + str(len(successfulRequests)) + "/" + str(expectedRequests) + " venmo requests.")

now = datetime.now()
main(now)
