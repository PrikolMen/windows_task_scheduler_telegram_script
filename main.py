import requests
import re



# Config Start

# Telegram Bot
CHAT = "CHAT_ID_HERE"
TOKEN = "BOT_TOCKEN_HERE"

# File
PATH_TO_FILE = "Audit/query_ID4740.txt"
LINES = [ 24, 27 ]

# Config End



# Send Function
def send( text ):
    requests.get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT}&text={text}')

# Reading
File = open( PATH_TO_FILE, 'r' )
Lines = File.readlines()

# Building Message
Count = 0
Message = "Blocked User:\n"
for line in Lines:
    Count += 1
    if Count in LINES:
        Message += "    " + re.sub(r"^\s+", "", line)

# Print in console
# print( Message )

# Sending in Telegram
send( Message )