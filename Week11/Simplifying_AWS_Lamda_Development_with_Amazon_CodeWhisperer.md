# Simplifying AWS Lambda Development with Amazon CodeWhisperer

## Flow Diagram
![CodeWhisperer drawio](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/1d277e19-e235-40ce-a526-5ce2742147f6)

## Step by Step guide
### Step 1:
Create an AWS CLoud9 environment CodeWhisperereDemo
![cloud9_env1](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/5cab955a-ee42-41a7-90bd-ea998e284358)

### Step 2: 
In the Environments section, for the CodeWhispererDemo environment, under Cloud9 IDE, click Open.
The IDE opens in a new browser tab (or window). Keep the current page and browser tab open.

### Step 3:
In the Welcome window, review the AWS Cloud9 development environment details.
To close the Welcome window, click the X.

### Step 4:
1. In the left side panel, click the AWS Explorer icon.
2. In the AWS Explorer window, click to expand the CodeWhisperer section.
3. For Resume Auto-Suggestions, click the play icon.
- Auto-suggestions provide you with code snippets that can help streamline and speed up the coding process.
![cloud9_env3](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/b50fd3c2-acc8-4242-ad47-ca24b7309cfe)

### Step 5:
- In the next steps, you create an AWS Lambda function in Python by using CodeWhisperer.
1. In the left side panel, click the Environment (folder) icon.
2. In the top window, click the plus sign (+) to expand the dropdown menu.
3. Choose New File.
![cloud9_env5](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/865cf55b-e77e-417e-803d-44d9ec2e4ae0)
### Step 6:
1. On the top navigation bar, click File to expand the dropdown menu.
2. Choose Save.
![cloud9_env6](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/939227af-b35a-4603-b2d2-de45ea959ac1)
### Step 7:
1. In the pop-up box, click Create folder.
2. For NewFolder, type:

**createBucket**

### Step 8:
1. Click to select createBucket.
2. For Folder, review to see that createBucket is displayed.
3. For Filename, type:
**addObjects.py**
4. Click Save.
![cloud9_env7](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/77aa4061-c3ee-4600-bb5a-68ad0b252fe9)
### Step 9:
1. In the top addObjects.py window, replacing YOUR_BUCKET_NAME with a unique bucket name, type:
```
#Lambda function to check if the bucket with the name <YOUR_BUCKET_NAME> exists
```
and press Enter.
- Be sure to include the comment hash symbol (#) at the beginning.
- You are using the us-east-1 region.
2. In the suggestion highlighted in green, hover the mouse over the suggestion to view it in full.
- CodeWhisperer displays suggestions to select from in a pop-up box.
3. Review the suggestion displayed by CodeWhisperer.
4. Choose the suggestion highlighted in green.
![cloud9_env8](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/dc96c2d6-fa2c-4774-bc8b-fb213e6bbf6c)

![cloud9_env9](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/732a8522-d230-4cef-b0bb-f831a240d9f5)
### Step 10:
1. Below line 4, review the CodeWhisperer suggestion, defining a Lambda handler.
2. Choose the suggestion highlighted in green.
![cloud9_env10](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/f3e7e0c4-0229-43ee-b018-5ed05b87d59d)

### Step 11:
1. At the end of the lambda_handler statement, press Enter.
2. Review the CodeWhisperer suggestion.
3. Choose the suggestion highlighted in green.
- All the suggestions in this solution might slightly differ from what is displayed in the screenshot examples.
![cloud9_env11](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/2f3ea952-41c7-4fc9-8bec-be162c19a89a)

![cloud9_env12](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/bcbd09d6-5efe-4ae4-8296-ae7d5c035066)

### Step 12:
1. At the end of line 9, press Enter, and then type:
```
else:
      #create
```
- Be sure to align the else block with the if block.
2. Review the CodeWhisperer suggestion.
3. Choose the suggestion highlighted in green.

![cloud9_env13](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/8cd7624b-9df2-4487-a769-aaa47bda6110)

### Step 13:
1. At the end of line 11, press Enter.
2. Review the CodeWhisperer suggestion.
3. Choose the suggestion highlighted in green.
![cloud9_env14](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/312eeabf-7c31-44cc-9f1c-9c814f221cd9)
### Step 14:
1. For Bucket, to replace 'XXXXX', paste your unique bucket name.
2. Review the code generated to create an S3 bucket.

- The bucket is created in Amazon Simple Storage Service (Amazon S3).

3. On the top navigation bar, click File to expand the dropdown menu.
4. Choose Save.
![cloud9_env15](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/1855f3bf-4cf1-4d39-bbb2-3c41caabe120)

![cloud9_env16](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/e85ea016-50df-41e7-8dd4-f4746fc51ef6)

### Step 15:
In the next steps, you create a text file to upload to the S3 bucket.

1. In the top window, click the plus sign (+) to expand the dropdown menu.
2. Choose New File.
![cloud9_env17](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/b706dbf0-3645-42bf-babc-ac4c6516c681)
### Step 16:
1. In the new Untitled window, type:
```
Testing Amazon CodeWhisperer in AWS Cloud9
```
2. On the top navigation bar, click File to expand the dropdown menu.
3. Choose Save.
![cloud9_env18](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/8028445e-dfe3-40d3-92f5-d0eaf97563ae)

### Step 17:
1. In the pop-up box, 1. Click to select createBucket.
2. For Folder, review to see that createBucket is displayed.
3. For Filename, type:

**test.txt**

4. Click Save.
![cloud9_env19](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/9cf08466-5afe-4abb-b91c-7ed79b82a8d7)
### Step 18:
- In the next steps, you update the addObjects.py file to upload the test.txt file to the S3 bucket.

1. In the top window, click the addObjects.py tab.
2. Below the S3 bucket creation command, type:
```
#upload test.
```
3. Review the CodeWhisperer suggestion to complete the comment.
4. Choose the suggestion highlighted in green.
![cloud9_env20](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/c9e57b54-520e-4802-926c-40fa9c7cbe7c)
### Step 19:
1. At the end of the upload comment, press Enter.
2. Review the CodeWhisperer suggestion to upload a file to the S3 bucket.
- In general, you should review the parameters in a suggestion and modify as needed based on your requirements.
3. Choose the suggestion highlighted in green.
![cloud9_env21](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/0cd068eb-a592-410d-b76c-62b8ebd474d6)

![cloud9_env22](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/53f14133-da63-4ae1-bf07-bdca731a322b)
### Step 20:
- In the next few steps, you will add a comment to add a new object in the bucket.
1. Below the upload file command, type:
```
#create a new
```
2. Review the suggestion provided by CodeWhisperer.
- The comment is for creating a new object in the S3 bucket.
3. Choose the suggestion highlighted in green.
  
![cloud9_env23](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/a6c8ae0a-6f53-4024-829d-97ddb9930988)
### Step 21:
1. At the end of the create new object in the bucket comment, press Enter.
2. Review the CodeWhisperer suggestion for put object command.
3. Choose the suggestion highlighted in green.
![cloud9_env24](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/2ea76ff3-7fe8-4f5d-9b79-06196467aa90)
### Step 22:
1. For Bucket, to replace 'XXXXX', paste your unique bucket name.
- The Key value (object name) might differ from the screenshot example.
2. Review the upload_file and put_object commands for S3.
3. On the top navigation bar, click File to expand the dropdown menu.
4. Choose Save.
- On your keyboard, you can also press Ctrl+S (Windows) or Cmd+S (Mac) to save an active file.
![cloud9_env25](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/ec07bb60-2721-4231-8940-947174307476)

### Step 23:
- In the next steps, you create a scripts.py file to create all the commands needed to upload the Lambda function to the AWS Management Console.

1. In the top window, click the plus sign (+) to expand the dropdown menu.
2. Choose New File.
![cloud9_env26](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/f4e51c3e-8078-4cdb-b929-3e9543f754c8)

### Step 24:
1. On the top navigation bar, click File to expand the dropdown menu.
2. Choose Save.
### Step 25:
1. In the pop-up box, for Filename, type:
**scripts.py**
- Saving the file with a .py extension will allow CodeWhisperer to provide suggestions.
2. Click Save.
![cloud9_env27](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/655c198b-e4b3-4bea-a641-464a08a0aa9e)
### Step 26:
1. In the top scripts.py window, type:
```
#command to zip files addObjects.py and test.txt
```
2. Review the CodeWhisperer suggestion to zip the files requested.
3. Choose the highlighted suggestion in green.
![cloud9_env28](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/e706d31f-5e9c-4e3b-a981-4ee42a26b9ad)
### Step 27:
1. Below the zip command, type:
```
#aws cli command to query for iam role arn with name LambdaDeploymentRole
```
- If a suggestion doesn't appear, press Enter.
- LambdaDeploymentRole was created as part of the lab prebuild process with permissions needed by the Lambda function to create an S3 bucket, upload objects to the bucket, and delete an object from the bucket.
2. Review the CodeWhisperer suggestion to get the IAM role with the provided name.
3. Choose the highlighted suggestion in green.
![cloud9_env29](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/e960493f-f30d-4da9-90be-1f42d57ae77a)
### Step 28:
1. On line 5, at the end of the CodeWhisperer suggestion, press the space bar.
2. Review the CodeWhisperer suggestion.
3. Choose the highlighted suggestion in green.
![cloud9_env30](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/0b71b213-4b38-4e59-acec-c7c42bbd6b79)
### Step 29:
- In this step, you run the commands in the AWS Cloud9 bash terminal to create a zip file.
1. In the terminal window, at the command prompt, run (type the command and press Enter):
```
cd createBucket
```
2. In the top scripts.py window, select (highlight) and copy the command to zip the files in the createBucket folder.
- Be sure not to copy the comment hash symbol (#) at the beginning.
3. Paste the command in the bottom terminal, and then press Enter.
4. Review the files added to the addObjects.zip file.
![cloud9_env31](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/520af42a-7afb-474e-b25b-0b7bb99e35fc)
### Step 30:
- In this step, you generate an AWS Command Line Interface (AWS CLI) command for uploading the Lambda function to the console.
1. In the top scripts.py window, type:
```
#aws cli command to upload a lambda function addObjects.zip file to the console with runtime 3.10
```
and press Enter.
2. In the pop-up box, review the CodeWhisperer suggestion to create the Lambda function.
- You can scroll to the right to view the entire suggestion.
3. Choose the highlighted suggestion in green.
![cloud9_env32](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/365084dd-f1dd-4cd8-a847-19aec49c81a5)
### Step 31:
1. In the top scripts.py window, select (highlight) and copy the command to get the IAM role ARN for the LambdaDeploymentRole.
2. In the bottom terminal, paste the command, and then press Enter.
3. Highlight and copy the role ARN output of the command.
- The output displays the ARN of the LambdaDeploymentRole. This value will be used in the create-function command in the next step.
![cloud9_env33](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/6a83a7ce-25e1-47f4-9fd4-6e9b70f2ba86)
### Step 32:
1. In the top scripts.py window, to replace the role ARN in the create-function command, after --role, paste the ARN that you just copied.
- You will have to scroll to the right to replace the complete command.
2. Copy the updated create-function command.
3. In the bottom terminal, paste the command, and then press Enter.
![cloud9_env34](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/29062bf9-ac3d-48ca-a7ea-7e06bc1efd32)
### Step 33:
1. Review the output of the create-function command.
- The StateReason and StateReasonCode parameter values provide the status of the creation process.
- The FunctionArn provides the ARN of the addObjects Lambda function.
2. At the colon symbol, press Enter until you see (END).
3. Review (END), and then press Ctrl+C to end the command.
![cloud9_env36](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/71d7d9fe-411b-490b-a836-ad870189d690)
### Step 34:
1. Go to the service Lambda.
2. In the Functions section, click addObjects.
![cloud9_env37](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/8ad79ead-78d2-4c00-aa1e-924a052ed326)
### Step 35:
1. In the Function overview section, review the addObjects function details.
2. Scroll down to the Code source section.
3. In the Environment window, under addObjects, review the displayed files.
4. In the addObjects.py window, review the code.
![cloud9_env38](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/c36e23e4-315b-4831-9439-e3bf0fd62eea)
### Step 36:
1. Click the Configuration tab.
2. In the General configuration section, under Timeout, review the default value.
3. To change the Timeout value, click Edit.
4. In the Edit basic settings window, scroll down to Timeout.
5. For min, type:**1**
6. Click Save.
### Step 37:
1. Review the success message alert.
2. Click the Test tab.
3. In the Test event section, for Test event action, choose Create new event.
4. For Event name, type:
**test**
5. For Event sharing settings, choose Private.
6. Scroll down to review the remaining settings.
7. At the top of the section, click Save.
![cloud9_env39](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/eda4e513-b356-4ea0-9c91-9e94fae44e7b)
### Step 38:
1. In the success alert, review the message.
2. To test the Lambda function, click Test.
### Step 39:
1. Review the Executing function:succeeded message.
- The executing function status changes from in progress to succeeded once the Lambda function runs successfully.
2. In the Executing function: succeeded section, click to expand Details.
3. Review the ResponseMetaData details.
![cloud9_env40](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/cd43610d-0818-4792-a440-84630e16b231)
### Step 40:
1. Go to the service S3.
2. In the Buckets section, review the details for the bucket name that starts with lab-bucket-.
3. Click the bucket name.
![cloud9_env41](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/9673fd8e-45cd-4d85-a012-7302b94a1646)
### Step 41
1. On the Objects tab, review the two objects that were created.
![cloud9_env42](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/9b88ef58-7342-4091-aaa0-a9e2aafd3ad2)
### Step 42:
- In this step, you activate CodeWhisperer for the AWS Lambda console. When activated, CodeWhisperer can make code recommendations on demand in the Lambda code editor as you develop your function.
1. Navigate to the addObjects function page on the AWS Lambda console.
2. On the Code tab, on the Code source navigation bar, click Tools to expand the dropdown menu.
3. Choose Amazon CodeWhisperer Code Suggestions.
![cloud9_env43](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/e24996d2-b3ad-4b89-8a91-be7323c0f7ff)
### Step 43:
- The LambdaDeploymentRole has codewhisperer:GenerateRecommendations permission attached to it.
1. In the addObjects.py window, below the s3.put_object command, type:
```
# delete an object from lab-bucket
```
and press Enter.
2. On the Code source navigation bar, click Tools to expand the dropdown menu.
3. Choose Suggest Code Snippet.
![cloud9_env44](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/d2a1e8ba-c48d-4a83-ba56-6a7cc35194d4)
### Step 44:
1. Review the suggestion provided by CodeWhisperer to delete the test.txt file.
2. Press Enter to accept the suggestion.
3. For Bucket, to replace 'XXXXX', paste your unique bucket name.
4. To deploy the updated function code, click Deploy.
![cloud9_env45](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/9f64202d-20ef-4f3d-99cc-9d0a8f8ad505)

### Step 45:
1. In the success alert, review the message.
2. Review the function code with the delete_object method.
3. To run the updated function code, click Test.
4. In the Execution results window, review the Status:Succeeded and the results.
![cloud9_env46](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/650bced8-4e59-40d1-905f-1ad513df872e)
### Step 46:
1. Navigate to the lab-bucket page on the Amazon S3 console.
2. On the Objects tab, review to see that the test.txt object was deleted
### Step 47:
1. Add a comment to enable versioning for the bucket
```
# enable versioning for the bucket
```
and press Enter.
2. On the Code source navigation bar, click Tools to expand the dropdown menu.
3. Choose Suggest Code Snippet.
![cloud9_env47](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/a3eb5750-4126-4a90-bd6e-2f91101d2a75)
### Step 48:
1. Review the suggestion provided by CodeWhisperer.
2. Press Enter to accept the suggestion.
3. Update the bucket name, and then update the Versioning configuration status value to "Enabled"
4. To deploy the updated function code, click Deploy.
![cloud9_env48](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/ca60569a-5224-4b54-a100-6861492693c9)
### Step 49:
1. In the success alert, review the message.
2. Review the function code.
3. To run the updated function code, click Test.
4. In the Execution results window, review the Status: Succeeded and the results.
### Step 50:
1. Go to S3 bucket.
2. Review Versioning under the properties tab.

**Congratulations!** We have successfully developed a Lambda function with Amazon CodeWhisperer.






















   





