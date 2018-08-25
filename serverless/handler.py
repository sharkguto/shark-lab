import json
import os

json_return = os.getenv("PROPERTIES")


def main(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        'json_return': json_return
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
