import re
import os
import requests
from agents import function_tool
from dotenv import load_dotenv
load_dotenv()
# UltraMsg API Credentials
instance_id = os.getenv('INSTANCE_ID')
api_token = os.getenv('API_TOKEN')
ultra_msg_url = f'https://api.ultramsg.com/{instance_id}/messages/chat?token={api_token}'
if not instance_id and api_token:
    raise ValueError('instance_id and api_token is not set in the env variables..')

# --- Format any phone number to 92XXXXXXXXXX ---
def format_number(input_number):
    cleaned = re.sub(r'\D','', input_number)
    if cleaned.startswith('92') and len(cleaned) == 12:
        return cleaned
    elif cleaned.startswith('03') and len(cleaned) == 11:
        return '92' + cleaned[1:]
    elif cleaned.startswith('+92') and len(cleaned) == 13:
        return cleaned[1:] 
    elif len(cleaned) == 10:
        return '92' + cleaned
    else:
        return None

# --- Send WhatsApp message ---

def send_whatsapp_message(to_number, message):
    payload ={
        'to': to_number,
        'body': message
    }

    responce = requests.post(ultra_msg_url, data=payload)
    return responce.json()
