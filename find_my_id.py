import warnings
from dotenv import load_dotenv
from utils import get_env, Venmo

# Suppress the OpenSSL warning
warnings.filterwarnings("ignore", message=".*OpenSSL.*")

def find_my_id():
    """
    Find your own Venmo user ID using your access token
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the access token from environment variables
    access_token = get_env("VENMO_ACCESS_TOKEN")
    
    # Initialize the Venmo client
    venmo = Venmo(access_token)
    
    print("🔍 Looking up your own Venmo user ID...")
    user_id = venmo.get_my_user_id()
    
    if user_id:
        print(f"✅ Found your Venmo user ID: {user_id}")
        return user_id
    else:
        print("❌ Could not find your Venmo user ID.")
        print("   Make sure your VENMO_ACCESS_TOKEN is valid in your .env file.")
        return None

def main():
    """
    Main function to get your own Venmo user ID
    """
    print("🤖 Efron's Venmo ID Finder")
    print("=" * 30)
    
    user_id = find_my_id()
    
    if user_id:
        print(f"\n🎉 Success! Your Venmo user ID is: {user_id}")
        print("💡 You can use this ID in your .env file or for testing purposes.")
    else:
        print("\n😞 Sorry old sport, couldn't find your ID.")
        print("   Please check your VENMO_ACCESS_TOKEN and try again.")

if __name__ == "__main__":
    main()
