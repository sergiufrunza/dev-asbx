import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from decouple import config

client = Client(config('TWILIO_ACCOUNT_SID'), config('TWILIO_AUTH_TOKEN'))
verify = client.verify.services(config('TWILIO_VERIFY_SERVICE_SID'))

def test():
    available_phone_numbers = client.available_phone_numbers.list()
    return available_phone_numbers



def send(phone):
    try:
        verify.verifications.create(to=phone, channel='sms')
    except TwilioRestException:
        return False
    return True



def check(phone, code):
    try:
        result = verify.verification_checks.create(to=phone, code=code)
    except TwilioRestException:
        return False
    return result.status == 'approved'