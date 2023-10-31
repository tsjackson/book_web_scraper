import requests
import dotenv
import os

dotenv.load_dotenv()

# Assigning the environment variables to variables

user_1_code : str = os.environ.get('USER_1_CODE')
user_2_code : str = os.environ.get('USER_2_CODE')
user_3_code : str = os.environ.get('USER_3_CODE')
user_4_code : str = os.environ.get('USER_4_CODE')

discord_webhook_token : str = os.environ.get('DISCORD_WEBHOOK_TOKEN')
discord_webhook_id : str = os.environ.get('DISCORD_WEBHOOK_ID')

def post_to_discord(user: list, title: str, description: str, username: str = "Probius") -> None:
    # Discord webhook URL where the message will be sent
    url = f"https://discord.com/api/webhooks/{discord_webhook_id}/{discord_webhook_token}?wait=true"
    
    # Dictionary mapping user names to their Discord user IDs
    user_id = {
        'Boozeclues' : user_1_code,
        'Lysandus' : user_2_code,
        'Frost' : user_3_code,
        'Phoenix' : user_4_code
    }

    # Get the Discord user ID based on the provided user name
    # selected_user = user_id[user]
    mention = []

    for person in user:
        selected_user = user_id[person]
        data = f"<@{selected_user}>"
        mention.append(data)

    mention:str = ", ".join(mention)

    # Create an embed object with title, description, and color
    embed = {
        "title": title,
        "description": description,
        "color": 0xffff00,  # Yellow color in hexadecimal
    }

    # Create the payload to send to the Discord webhook
    payload = {
        "content": mention,  # Mention the selected user
        "embeds": [embed],  # Include the embed in the message
        "username": username,  # Set the username for the message sender
    }

    # Send the POST request to the Discord webhook
    response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})

    # Check the response status code to determine if the message was sent successfully
    if response.status_code == 200:
        print("Message sent successfully.")
        return response.json()
    else:
        print(f"An error occurred: {response.status_code}")
        print(response.text)

def delete_message(messageID : str) -> None:
    url = f"https://discord.com/api/webhooks/{discord_webhook_id}/{discord_webhook_token}/messages/{messageID}"
    response = requests.delete(url)
    if response.status_code == 204:
        print("Message deleted successfully.")
    else:
        print(f"An error occurred: {response.status_code}")
        print(response.text)