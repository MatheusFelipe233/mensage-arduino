from twilio.rest import Client

account_sid = 'AC190a9418d8853a70ae2707247e73aa9b'
auth_token = '06040c26b3a16cb3e0167d66e0163bf0'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Alerta!!! pooooh!!!',
  to='whatsapp:+559295143900'
)

print(message.sid)

#comentário

#segundo comentário