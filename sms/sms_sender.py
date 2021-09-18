# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

source_phone = '+1XXXXXXXX'
to_phone = '+1XXXXXXXXX'

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello!!!!",
                     from_=source_phone,
                     to=to_phone
                 )

print(message.sid)