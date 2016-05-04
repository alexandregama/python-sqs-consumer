import boto3

# Get the service resource, in this case SQS Resource from boto3 module
sqs = boto3.resource('sqs')

# Create a new queue named test passing a few attributes, in this case just DelaySeconds
queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# We can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
