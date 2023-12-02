def lambda_handler(event, context):
    auth = 'Deny'
    if (event['authorizationToken'] == '123'):
        auth = 'Allow'
    authResponse = {
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": ["execute-api:Invoke"],
                    "Effect": auth,
                    "Resource": "arn:aws:execute-api:*:ACCOUNTID:APIID/*"
                }
            ]
        }
    }
    return authResponse
