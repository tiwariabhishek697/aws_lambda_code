import boto3
import uuid


def lambda_handler(event, context):
    # this will create dynamodb resource object and
    # here dynamodb is resource name
    client = boto3.resource('dynamodb')
    # this will search for dynamoDB table
    # your table name may be different
    table = client.Table("for_deletion")
    print(table.table_status)
    table.put_item(Item={'user': '10415210016', 'name': 'himanshu', 'uuid': str(uuid.uuid4())})
    table.put_item(Item={'user': '10415210034', 'name': 'rahul', 'uuid': str(uuid.uuid4())})
    table.put_item(Item={'user': '10415210004', 'name': 'kapil', 'uuid': str(uuid.uuid4())})
    table.put_item(Item={'user': '10415210045', 'name': 'negi'})
    # table.update_item(
    # Key = {
    #   'Id' : '10415210016',
    # },
    # UpdateExpression='SET Age = :val1',
    # ExpressionAttributeValues={
    #   ':val1': '6'
    # }
    # )
    response = table.get_item(Key={'user': '10415210016'})
    item = response['Item']
    print(item)

