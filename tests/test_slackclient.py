from Client.slackclient import SlackCLient

default_channel = '#test'
new_channel = '#general'
message1 = 'This is the first message'
message2 = 'This is a new message'

test_client = SlackCLient(default_channel)
test_client.message(message1)
test_client.message(message2)

test_client.channel(new_channel)
test_client.message(message1)
test_client.message(message2)