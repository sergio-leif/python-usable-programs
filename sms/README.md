
# Requirements

Create an account and log in on https://www.twilio.com/referral/20w9Wq. It is necessary to create a phone number and an auth token.

Configure environment variables with your twilio account:

```
    export TWILIO_ACCOUNT_SID=$SID_ACCOUNT
    export TWILIO_AUTH_TOKEN=$AUTH_TOKEN
```

## Required modules
```
    pip install twilio
```

# Running program
```
    python sms_sender.py
```

```
    python check_appointments.py SOURCE_PHONE_NUMBER DESTINATION_PHONE_NUMBER URL_TO_CONSULT
```

For example:
```
    python check_appointments.py +19341234567 +19340987654 https://url.example.com
```