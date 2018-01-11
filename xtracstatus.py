# This function is used to implement a general status tracking
# application model. It takes correlated events that contain a status
# state field, and persists the last observed state value for the model
# instance.

# This model will be completely simple minded - no attempts to deal with out
# of order messages, skipped states, etc - it will simple persist the state in
# the model table

import os
import boto3
import time
import uuid

table_name = os.environ['MODEL_INSTANCE_TABLE_NAME']

ddb_client = boto3.client('dynamodb')

current_milli_time = lambda: int(round(time.time() * 1000))

def lambda_handler(event, context):
    print 'xtrac status function called with {}'.format(event)
    txn_id = uuid.uuid4()

    workItem = event['XtracEvent']['WorkItem']
    print workItem

    workItemNo = workItem['WorkItemNo']
    print workItemNo

    status = workItem['Status']
    print status 

    instance_id = workItemNo
    state = status

    response = ddb_client.put_item(
        TableName=table_name,
        Item={
            'instanceId':{'S': instance_id},
            'txnId':{'S': txn_id},
            'state':{'S' : state},
            'timestamp': {'N' : str(current_milli_time())}
        }
    )

    print response


