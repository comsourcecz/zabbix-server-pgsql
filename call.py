#!/usr/bin/env python3
import os
import sys
from twilio.rest import Client
import time

# Twilio
ERROR_STATES = ["busy", "failed", "no-answer"]
TERMINAL_STATES = ["completed"] + ERROR_STATES

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
PHONE_NO = os.environ['TWILIO_PHONE_NO']

if len(sys.argv) < 3:
    print("error")
    sys.exit(1)

TO=sys.argv[1]
SUBJECT=sys.argv[2]
BODY=sys.argv[3]

client = Client(ACCOUNT_SID, AUTH_TOKEN)

call = client.calls.create(
                        twiml=f'<Response><Pause length="2"/><Say voice="woman" loop="3">{SUBJECT}: {BODY}</Say></Response>',
                        to=TO,
                        from_=PHONE_NO
                    )

cycle = True
while cycle:
    if call.status in TERMINAL_STATES:
        cycle = False
    else:
        print(call.status)
        time.sleep(2)
        call = call.fetch()

print(call.status)
if call.status in ERROR_STATES:
    exit(1)
