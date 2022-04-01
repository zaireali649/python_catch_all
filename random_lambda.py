import json
import boto3 as AWS
import random as randomboiboiclaude

def lambda_handler(event, context):
    # TODO implement
    
    try:
        start = int(event['random_start'])
    except:
        start = 0
        
    try:
        end = int(event['random_end'])
    except:
        end = 100
    
    if(start > end):
        start = end
        
    print(start, end)
    
    number = randomboiboiclaude.randint(start, end)
    print(number)
    
    return {
        'statusCode': 200,
        'body': json.dumps(str(number))
    }
