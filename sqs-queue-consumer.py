import boto3

sqs = boto3.resource('sqs')

# Retrieving a queue by its name
queue = sqs.get_queue_by_name(QueueName='test')

# Printint queues informations
print("Queue url retrieved: {0}".format(queue.url))
print("Retrieved queue and its attributes: {0}".format(queue.attributes.get('DelaySeconds')))

# Printing all queues urls that exists in Amazon SQS
print("\nPrinting all queues from Amazon SQS")
for queue in sqs.queues.all():
    print("Queue url: {0}".format(queue.url))
