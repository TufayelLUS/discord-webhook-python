import requests
import json

webhook_id = 123456789 # place webhook id
webhook_token = "abcdefghi" # place webhook token
webhook_link = f"https://discordapp.com/api/webhooks/{webhook_id}/{webhook_token}"


def sendToDiscord(title, description, item_link, image_link):
    headers = {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
    }
    data = {
        # "username": "Sender Name",
        "avatar_url": "",
        "embeds": [
            {
                "title": title,
                "description": description,
                "url": item_link,
                "image": {
                    "url": image_link,
                    "height": 400,
                    "width": 400
                }
            }
        ]
    }
    try:
        requests.post(webhook_link, headers=headers, data=json.dumps(data))
    except:
        print("Failed to make request to discord api")
        return
    print("Sent to discord ...")

if __name__ == "__main__":
    sendToDiscord("Some Title", "This is my message", "https://github.com/TufayelLUS/discord-webhook-python", None)
