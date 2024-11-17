import sys
import requests
import json

def print_logo():
    print(r"""
      _______                    _______ __           ____ __         __
     |     __|.----.---.-.----- |_     _|  |--.-----.|    |  |.-----.|  |_
     |__     ||  __|  _  |     |  |   | |     |  -__||       ||  -__||   _|
     |_______||____|___._|__|__|  |___| |__|__|_____||__|____||_____||____|
    """)

def main():
    # Print ASCII logo
    print_logo()

    # Determine how many entries to display (default to max 100)
    max_entries = 100  # Default value

    if len(sys.argv) > 1:
        try:
            max_entries = int(sys.argv[1])  # Get user-defined value from command line
            if max_entries < 1 or max_entries > 100:
                print("Please enter a number between 1 and 100.")
                return  # Exit if the number is out of range
        except ValueError:
            print("Please enter a valid integer.")
            return

    # Perform the request
    try:
        response = requests.get("https://api.scanthe.net/")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response

        # Accessing and printing relevant parts of the JSON
        count = 0  # Counter for the entries displayed
        for packet in data["data"]:
            if count >= max_entries:
                break  # Stop if we reach the maximum entries
            print(f"ID: {packet['id']}")
            print(f"Timestamp: {packet['timestamp']}")
            print(f"Source IP: {packet['source_ip']}")
            print(f"Source Port: {packet['source_port']}")
            print(f"Destination Port: {packet['dest_port']}")
            print(f"Data: {packet['data']}")
            print("----------")
            count += 1

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")

if __name__ == "__main__":
    main()
