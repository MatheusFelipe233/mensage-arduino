from twilio.rest import Client

account_sid = 'AC499cf50728ad909a813c46d2874777f5'
auth_token = '573ad38ff8032c8c66e913b567d82f84'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='preciso passar em seph porra >_<',
  to='whatsapp:+559282605819'
)

print(message.sid)

#comentário

#segundo comentário