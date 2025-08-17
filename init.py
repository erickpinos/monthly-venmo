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
    # Load environment variables from .env
    load_dotenv()
    
    # Get all environment variables
    actualVars = []
    for var in env_vars:
        actualVars.append(get_env(var))

    # Unpack the variables
    access_token, chat_id, bot_token, friend_id_1, friend_name_1, send_or_request_1, amount_1, description_1, specified_day_1, funding_id_1, friend_id_2, friend_name_2, send_or_request_2, amount_2, description_2, specified_day_2, funding_id_2 = actualVars

    # Convert specified days to integers
    specified_day_1 = int(specified_day_1)
    specified_day_2 = int(specified_day_2)

    # Initialize Venmo and Telegram clients
    venmo = Venmo(access_token)
    telegram = Telegram(bot_token, chat_id)
    
    # Define friends with their configurations
    friends = [
        {
            "name": friend_name_1,
            "id": friend_id_1,
            "send_or_request": send_or_request_1,
            "amount": float(amount_1),
            "description": description_1,
            "specified_day": specified_day_1,
            "funding_id": funding_id_1
        },
        {
            "name": friend_name_2,
            "id": friend_id_2,
            "send_or_request": send_or_request_2,
            "amount": float(amount_2),
            "description": description_2,
            "specified_day": specified_day_2,
            "funding_id": funding_id_2
        }
    ]

    successfulRequests = []
    expectedRequests = 0

    # Check each friend's specified day
    for i, friend in enumerate(friends, 1):
        if now.day == friend["specified_day"]:
            print(f"🎯 Today is day {now.day}, processing friend {i}: {friend['name']}")
            expectedRequests += 1
            
            # Process the transaction for this friend
            success = process_friend_transaction(venmo, telegram, friend, i)
            if success:
                successfulRequests.append(success)
        else:
            print(f"⏰ Today is day {now.day}, not day {friend['specified_day']} for friend {i}: {friend['name']}")

    # Report results
    if expectedRequests == 0:
        print(f"📅 Today is day {now.day}, no transactions scheduled for today.")
    elif len(successfulRequests) == expectedRequests:
        print(f"✅ Ran script successfully and completed {expectedRequests} Venmo transactions.")
    else:
        print(f"❌ Something went wrong. Completed {len(successfulRequests)}/{expectedRequests} transactions.")

def process_friend_transaction(venmo, telegram, friend, friend_number):
    """
    Process a transaction for a specific friend
    """
    name = friend["name"]
    friend_id = friend["id"]
    send_or_request = friend["send_or_request"]
    amount = friend["amount"]
    description = friend["description"] + " — Sent by Erick's assistant Efron 🤵🏻‍♂"
    funding_id = friend["funding_id"]
    
    message = f"""Good news old sport!

I have successfully completed action {send_or_request} ${amount} to {name}.

"{description}"

— Efron 🤵🏻‍♂
    """

    try:
        if send_or_request == "Send":
            success = venmo.send_money(friend_id, amount, description, funding_id)
        elif send_or_request == "Request":
            success = venmo.request_money(friend_id, amount, description)
        else:
            raise ValueError(f"Invalid value for send_or_request_{friend_number}. Expected 'Send' or 'Request'.")

        if success:
            telegram.send_message(message)
            print(f"✅ Successfully {send_or_request.lower()}ed ${amount} to {name}")
            return True
        else:
            print(f"❌ Failed to {send_or_request.lower()} ${amount} to {name}")
            return False
            
    except Exception as e:
        print(f"❌ An error occurred for {name}: {e}")
        return False

now = datetime.now()
main(now)
