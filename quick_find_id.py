#!/usr/bin/env python3
import sys
from dotenv import load_dotenv
from utils import get_env, Venmo

if len(sys.argv) != 2:
    print("Usage: python3 quick_find_id.py <username>")
    sys.exit(1)

load_dotenv()
access_token = get_env("VENMO_ACCESS_TOKEN")
venmo = Venmo(access_token)
user_id = venmo.get_user_id_by_username(sys.argv[1])

if user_id:
    print(f"User ID: {user_id}")
else:
    print("User not found")
