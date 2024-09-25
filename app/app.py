import json
import requests
import os


def lambda_handler(event, context):
    print(event)
    # Lets get Environment
    webhook_url = os.environ.get('WEBHOOK_URL') # "https://hooks.slack.com/services/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"
    print("webhook_url" + webhook_url)

    # Build Message
    try:
        message = {
            "alarmName": event['alarmData']['alarmName'],
            "state": event['alarmData']['state']  # json.dumps(event['alarmData']['state'])
        }

        payload = {
            "text": json.dumps(message)
        }
        print(type(payload))
        # Send Message to Slack
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )
        print("Slack response", response)

    except Exception as problem:
        print(f"An error occurred: {problem}")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
