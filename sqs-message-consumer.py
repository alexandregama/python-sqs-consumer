import boto3

# Choosing the resource from boto3 module
sqs = boto3.resource('sqs')

# Get the queue named test
queue = sqs.get_queue_by_name(QueueName='test')

# Process messages by printing out body from test Amazon SQS Queue
for message in queue.receive_messages():
    print('Hello, {0}'.format(message.body))
    message.delete()
