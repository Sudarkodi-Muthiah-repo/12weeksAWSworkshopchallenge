# Integrating DynamoDB
The primary focus of this lab is to provide hands-on experience in retrieving data from and populating data to a DynamoDB table by using a Python script. Using DynamoDB can both enhance your understanding of DynamoDB operations and familiarize you with the AWS SDK for Python (Boto3).
## Tasks
* Examine the preloaded Python code to understand how it functions through the AWS Cloud9 instance that you use to edit the Python script.
* Review the LanguagesTable by using the DynamoDB console and the AWS Command Line Interface (AWS CLI).
* Update the existing Python code so that you can insert an item into the LanguagesTable.
* Update the current Python code so that you can query the LanguagesTable by using a specific key.
* Test the Python script’s overall functionality to update the LanguagesTable and read from it.

Find the detailed steps here: ![Link](https://reinvent.labs.awsevents.com/lab/arn%3Aaws%3Alearningcontent%3Aus-east-1%3A470679935125%3Ablueprintversion%2FSPL-BE-100-CEIADD-1%3A1.0.1-3aa82e11/en-US)
## DynamoDB table
The LanguagesTable has already been created and pre-populated for your use in this lab. Else, You can create a LanuagesTable in your account using the SAM template
In this task, you open the DynamoDB console and review that the LanguagesTable exists and is populated.
* At the top of the AWS Management Console, in the search bar, search for DynamoDB and open the DynamoDB console in a new browser tab.
* From the navigation pane to the left, choose Tables.
* In the list of tables, choose the LanguagesTable link.
* To review the contents of the table, choose Explore table items.
