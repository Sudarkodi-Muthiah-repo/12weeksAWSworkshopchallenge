# Integrating DynamoDB
The primary focus of this lab is to provide hands-on experience in retrieving data from and populating data to a DynamoDB table by using a Python script. Using DynamoDB can both enhance your understanding of DynamoDB operations and familiarize you with the AWS SDK for Python (Boto3).
## Tasks
* Examine the preloaded Python code to understand how it functions through the AWS Cloud9 instance that you use to edit the Python script.
* Review the LanguagesTable by using the DynamoDB console and the AWS Command Line Interface (AWS CLI).
* Update the existing Python code so that you can insert an item into the LanguagesTable.
* Update the current Python code so that you can query the LanguagesTable by using a specific key.
* Test the Python script’s overall functionality to update the LanguagesTable and read from it.

Find the detailed steps here: ![Link](https://reinvent.labs.awsevents.com/lab/arn%3Aaws%3Alearningcontent%3Aus-east-1%3A470679935125%3Ablueprintversion%2FSPL-BE-100-CEIADD-1%3A1.0.1-3aa82e11/en-US)
## Connect to the AWS CLOUD9 environment
you connect to the AWS Cloud9 environment that’s provisioned as part of this lab and preloaded with the Python script that you’re challenged with updating.
## DynamoDB table
The LanguagesTable has already been created and pre-populated for your use in this lab. Else, You can create a LanuagesTable in your account using the SAM template
In this task, you open the DynamoDB console and review that the LanguagesTable exists and is populated.
* At the top of the AWS Management Console, in the search bar, search for DynamoDB and open the DynamoDB console in a new browser tab.
* From the navigation pane to the left, choose Tables.
* In the list of tables, choose the LanguagesTable link.
* To review the contents of the table, choose Explore table items.
image
One quick method to verify that the table exists and is populated is to run an AWS CLI command and return the results after they are formatted by using the Linux tool, awk.
```
echo -e "Language\tCode" && echo -e "--------\t----" && aws dynamodb scan --table-name LanguagesTable --query "Items[*].[Language.S, Code.S]" --output text | awk '{printf "%-15s %-5s\n", $1, $2}'
```
image
## REVIEW THE PYTHON SCRIPT
In this task, you review the Python script, and learn about the main sections and what they are intended to do. You also identify the sections you are challenged to update.

```
import boto3
dynamo = boto3.client('dynamodb')

#####
# Challenge 1: Put the entry for Danish into the LanguagesTable
#   "Language": "Danish"
#   "Code": "da"
#####
dynamo.put_item(
    TableName="????",
    Item={?????
          })

#####
# Challenge 2: Retrieve the entry for Danish
#####
response = dynamo.get_item(
    TableName="????",
    Key={?????})

print("")  # adds a blank line to format output
print(response['Item'])
print("")  # adds a blank line to format output
```
This Python code uses the boto3 library, which is the AWS SDK for Python, to interact with a DynamoDB database.
The first part of the code (Challenge 1) puts an item into a DynamoDB table. The item represents a language, with Code as da and Language as Danish. However, the table name and the specific item details are left as question marks (???), and you are tasked with completing the details.

The second part of the code (Challenge 2), retrieves the item that represents the Danish language from the DynamoDB table. Again, the table name and the key details are left as question marks (???), and you are challenged with filling in those missing details.

Finally, the code prints the retrieved item. The response from the get_item operation is a dictionary, and Item is the key in this dictionary that contains the retrieved item.


