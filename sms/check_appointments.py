#!/bin/python3

import os
from twilio.rest import Client
import urllib.request
import json
import time
import sys

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Phone numbers to send the notification
source_phone = sys.argv[1]
to_phone = sys.argv[2]

# URL to check
url = sys.argv[3]

desired_locations = [239, 252, 266, 240, 246, 253, 248]

available = False

while available == False:
    time.sleep(15)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    request = urllib.request.Request(url)

    r = urllib.request.urlopen(request).read()

    answer = r.decode('utf-8')
    little = answer.split('\n')[234].split('= ')[1].replace('[','').replace(']','').replace('\r','')
    lista = list(little.split('},'))
    for index in range(len(lista)):
        if index < len(lista)-1:
            lista[index] += '}'
        location = json.loads(lista[index])
        location_id = location['LocationId']

        if location_id in desired_locations:
            if location['FirstOpenSlot'] != 'No Appointments Available':
                print(f'[{current_time}] Run and take one appointment! {url}/{location_id}')
                message = client.messages \
                    .create(
                        body="Run and take one appointment! " + url,
                        from_=source_phone,
                        to=to_phone
                    )
                available = True
                break
        if index == len(lista)-1:
            print(f'[{current_time}] There are not available appointments yet')
            