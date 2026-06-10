import os
import sys

# List of required environment variables
REQUIRED_VARS = ["API_KEY", "DB_PATH", "LOG_LEVEL"]

def validate_environment():
    missing = [var for var in REQUIRED_VARS if not os.environ.get(var)]
    
    if missing:
        print(f"Error: Missing required environment variables: {', '.join(missing)}")
        sys.exit(1)
    else:
        print("Success: All environment variables are set correctly.")

if __name__ == "__main__":
    validate_environment()