import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='test')

while 1:
    messages = queue.receive_messages(WaitTimeSeconds=5)
    for message in messages:
        print("Message received: {0}".format(message.body))
        message.delete()
