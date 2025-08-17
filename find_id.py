import sys
import warnings
from dotenv import load_dotenv
from utils import get_env, env_vars, Venmo

# Suppress the OpenSSL warning
warnings.filterwarnings("ignore", message=".*OpenSSL.*")

def find_id(username):
    """
    Find a Venmo user ID by username
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the access token from environment variables
    access_token = get_env("VENMO_ACCESS_TOKEN")
    
    # Initialize the Venmo client
    venmo = Venmo(access_token)
    
    user_id = venmo.get_user_id_by_username(username)
    
    if user_id:
        print(f"✅ Found user ID for '{username}': {user_id}")
        return user_id
    else:
        print(f"❌ Could not find user ID for '{username}'.")
        print("   If you're looking for your own ID, run 'python3 find_my_id.py' instead.")
        return None

def main():
    """
    Main function to handle command line arguments
    """
    if len(sys.argv) != 2:
        print("Usage: python3 find_id.py <username>")
        print("Example: python3 find_id.py jordan-mishlove")
        print("")
        print("To find your own ID, use: python3 find_my_id.py")
        sys.exit(1)
    
    username = sys.argv[1]
    print(f"🔍 Looking up Venmo user ID for: {username}")
    
    user_id = find_id(username)
    
    if user_id:
        print(f"\nUser ID: {user_id}")
        print("You can use this ID in your .env file for FRIEND_ID_1")

if __name__ == "__main__":
    main()