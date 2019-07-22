# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC96b8f85325af280e038622314a88629a'
auth_token = 'e0514dfbc1dada56a857b8ad859405df'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18329091548',
                     to='+12818060701'
                 )

print(message.sid)
