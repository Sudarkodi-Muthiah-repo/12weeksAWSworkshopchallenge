# Moving to Amazon API Gateway
## Lab Overiview
This lab demonstrates how to create the Amazon DynamoDB table and the Amazon API Gateway hosted API that’s used by the application.

The lab starts by guiding you through the process of creating a DynamoDB table that will be used to store the uniqueGridId data sent to the API. API Gateway acts as a frontend for the Lambda functions. You then update the Lambda function to store the mapping from uniqueGridId to an Amazon Simple Storage (Amazon S3) object by using a PUT operation.

After the AWS Lambda functions are updated, you deploy the application. Then, you create the API Gateway resource and add routes to the Lambda functions to copy images and create the grid image. API Gateway can then act as an initiator for the Lambda functions.

Finally, the lab guides you through the process of testing the functionality of the API by invoking it through API Gateway and verifying the results. You can observe how API Gateway activates the Lambda functions. You can also see how the Lambda functions perform the intended operations on the S3 bucket by creating a new grid image, creating an S3 presigned URL, and populating uniqueGridId data in the DynamoDB table.
## Objectives
* Create a DynamoDB table.
* Update the application to save the mapping from uniqueGridId to an S3 object by using dynamodb.put_item.
* Deploy the application.
* Create an API by using API Gateway.
* Run the API to create the grid image and an S3 presigned URL.
### Task 1 Create a DynamoDB table
To create a DynamoDB table named GridBuilder, run the following AWS Command Line Interface (AWS CLI) command:
```
aws dynamodb create-table \
  --table-name GridBuilder \
  --attribute-definitions \
      AttributeName=uniqueGridId,AttributeType=S \
      AttributeName=s3Key,AttributeType=S \
  --key-schema \
      AttributeName=uniqueGridId,KeyType=HASH \
      AttributeName=s3Key,KeyType=RANGE \
  --provisioned-throughput \
      ReadCapacityUnits=5,WriteCapacityUnits=5
```
Image

**Congratulations!** You have successfully created the GridBuilder DynamoDB table.
### Task 2 UPDATE THE APPLICATION TO USE DYNAMODB
In this task, you update the application so it uses DynamoDB to store the images that it needs to create the grid image.
* Open the file tree and then open the /api-backend-manual/add_image/app.py file.
* Update the dynamodb.put_item method to save the mapping from uniqueGridId to an S3 object.
  
**Solution**
```python
import os
import json
import boto3
import base64

s3 = boto3.client("s3")
dynamodb = boto3.client("dynamodb")
table_name = "GridBuilder"
source_bucket = os.getenv('SOURCE_BUCKET')


def lambda_handler(event, context):
    event_body = base64.b64decode(
        event["body"]) if event["isBase64Encoded"] else event["body"]
    uniqueGridId = event["queryStringParameters"]["uniqueGridId"]

    # save the s3 object with a random name
    object_key = os.urandom(16).hex() + ".jpg"
    print(f"Saving to bucket: {source_bucket} key: {object_key}")
    s3.put_object(
        Bucket=source_bucket,
        Key=object_key,
        Body=event_body,
        ContentType='image/jpg'
    )

    # save the mapping from uniqueGridId to s3 object
    dynamodb.put_item(
        TableName=table_name,
        # CHALLENGE-A BEGIN
        Item={
            "uniqueGridId": {"S": uniqueGridId},
            "s3Key": {"S": object_key}
        }
        # CHALLENGE-A END
    )

    return {
        "statusCode": 200,
        "headers": {"access-control-allow-origin": "*"},
        "body": json.dumps({
            "message": "image saved",
            "image_size": len(event_body)
        }),
    }
```

* To create a compressed .zip deployment package of the application and its dependencies, run the following command:
  
```
cd ~/environment/api-backend-manual/add_image ; zip ~/environment/api-backend-manual/add_image app.py
```

image
### CREATE A LAMBDA FUNCTION
In this task, you create the add_image Lambda function based on the deployment package that you just created.
* To create the add_image Lambda function by using the deployment package, run the following command:
```
aws lambda create-function \
--function-name add_image \
--runtime python3.9 \
--timeout 30 \
--handler app.lambda_handler \
--role $LAMBDA_ROLE \
--environment Variables={SOURCE_BUCKET=$SOURCE_BUCKET} \
--zip-file fileb://~/environment/api-backend-manual/add_image.zip
```
Image

**Congratulations!** You successfully updated the application, created a deployment package, and used it to create the add_image Lambda function.
### Task 3 Create an API by using API Gateway
* At the top of the AWS Management Console, in the search bar, search for and choose API Gateway, then choose Open Link in New Tab.
* On the Choose an API type page, in the HTTP API section, choose Build .
* On the Create an API page, in the Create and configure integrations section:
* Choose Add integration
* For Integrations, choose Lambda.
* For AWS Region, choose the region value that’s specified in the lab details at the left of this screen.
* For Lambda function, choose the function name that ends with function:add_image.
* Choose Add integration.
* For Integrations, choose Lambda.
* For AWS Region, choose the region value that’s specified in the lab details to the left of this screen.
* For Lambda function, choose the function name that ends with function:generate_grid.
* For API name, enter generate-grid
* Choose Next .
* On the Configure routes page, in the Configure routes section:
* For both entries that are listed, for the HTTP Method, choose POST.
* Choose Next.
* On the Define stages page, keep the default values and choose Next
* On the Review and create page, choose Create
  Image
* On the left navigation pane, choose Stages.
* Choose the $default stage.
* Copy the invoke URL to an editor. It should look similar to https://vf3acap6h0.execute-api.us-west-2.amazonaws.com.
You use the invoke URL in a later step.
**Congratulations!** You have successfully created an API by using API Gateway. This API can receive POST HTTP methods from the add_image and generate_grid Lambda functions.



