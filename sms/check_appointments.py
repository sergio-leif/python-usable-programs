#!/bin/python3

import os
from twilio.rest import Client
import urllib.request
import time

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Phone numbers to send the notification
source_phone = '+1XXXXXXXX'
to_phone = '+1XXXXXXXXX'

# URL to check
url = 'https://url.example.com'

available = False

while available == False:
    time.sleep(30)
    request = urllib.request.Request(url)

    r = urllib.request.urlopen(request).read()

    answer = r.decode('utf-8')
    little = answer.split('\n')[135:180]
    # print(little)
    for line in little:
        if 'Appointments Available' in line:
            if '0 Appointments Available' in line:
                print('There is not available appointments')
                # message = client.messages \
                #     .create(
                #          body="Sorry, no appointments yet " + url,
                #          from_=source_phone,
                #          to=to_phone
                #      )
            else:
                print('Run and take one appointment!')
                message = client.messages \
                    .create(
                        body="Run and take one appointment! " + url,
                        from_=source_phone,
                        to=to_phone
                    )
                available = True
