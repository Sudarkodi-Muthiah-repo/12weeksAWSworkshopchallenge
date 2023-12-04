# Python Challenge
Architecture
## Overview
In this lab, you get hands-on experience testing your Python skills by updating application code for AWS Lambda functions that read and write directly from and to an Amazon DynamoDB table. The table data is added and retrieved through an Amazon Simple Storage Service (Amazon S3) hosted website that has an Amazon API Gateway integration to access the Lambda functions. The Lambda functions perform two of the four create, read, update, delete (CRUD) operations.
## Tasks
* You are challenged to update the Lambda function to retrieve the ID, Firstname, and Lastname from the Lambda event that’s based on   the submitted form from the Amazon S3-hosted website.
* Next, you write the put_item code to save the item into the LabCustomers table. After you write the code, the last step is to use    the AWS Serverless Application Model (AWS SAM) to deploy the updated code for the application.
