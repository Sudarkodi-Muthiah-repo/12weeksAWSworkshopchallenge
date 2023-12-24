# Simplifying AWS Lambda Development with Amazon CodeWhisperer

## Flow Diagram
![CodeWhisperer drawio](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/1d277e19-e235-40ce-a526-5ce2742147f6)

## Step by Step guide
Step 1:
Create an AWS CLoud9 environment CodeWhisperereDemo
![cloud9_env1](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/5cab955a-ee42-41a7-90bd-ea998e284358)
Step 2: 
In the Environments section, for the CodeWhispererDemo environment, under Cloud9 IDE, click Open.
The IDE opens in a new browser tab (or window). Keep the current page and browser tab open.
Step 3:
In the Welcome window, review the AWS Cloud9 development environment details.
To close the Welcome window, click the X.
Step 4:
1. In the left side panel, click the AWS Explorer icon.
2. In the AWS Explorer window, click to expand the CodeWhisperer section.
3. For Resume Auto-Suggestions, click the play icon.

- Auto-suggestions provide you with code snippets that can help streamline and speed up the coding process.
![cloud9_env3](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/b50fd3c2-acc8-4242-ad47-ca24b7309cfe)
Step 5:
- In the next steps, you create an AWS Lambda function in Python by using CodeWhisperer.
1. In the left side panel, click the Environment (folder) icon.
2. In the top window, click the plus sign (+) to expand the dropdown menu.
3. Choose New File.
![cloud9_env5](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/865cf55b-e77e-417e-803d-44d9ec2e4ae0)
Step 6:
1. On the top navigation bar, click File to expand the dropdown menu.
2. Choose Save.
![cloud9_env6](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/939227af-b35a-4603-b2d2-de45ea959ac1)
Step 7:
1. In the pop-up box, click Create folder.
2. For NewFolder, type:

**createBucket**

Step 8:
1. Click to select createBucket.
2. For Folder, review to see that createBucket is displayed.
3. For Filename, type:

**addObjects.py**

4. Click Save.
![cloud9_env7](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/77aa4061-c3ee-4600-bb5a-68ad0b252fe9)
Step 9:
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
Step 10:
1. Below line 4, review the CodeWhisperer suggestion, defining a Lambda handler.
2. Choose the suggestion highlighted in green.
![cloud9_env10](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/f3e7e0c4-0229-43ee-b018-5ed05b87d59d)

Step 11:
1. At the end of the lambda_handler statement, press Enter.
2. Review the CodeWhisperer suggestion.
3. Choose the suggestion highlighted in green.

- All the suggestions in this solution might slightly differ from what is displayed in the screenshot examples.
![cloud9_env11](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/2f3ea952-41c7-4fc9-8bec-be162c19a89a)

![cloud9_env12](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/bcbd09d6-5efe-4ae4-8296-ae7d5c035066)

Step 12:
1. At the end of line 9, press Enter, and then type:

else:
      # create 

- Be sure to align the else block with the if block.

2. Review the CodeWhisperer suggestion.
3. Choose the suggestion highlighted in green.

![cloud9_env13](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/8cd7624b-9df2-4487-a769-aaa47bda6110)






   





