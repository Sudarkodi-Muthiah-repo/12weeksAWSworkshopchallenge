# Building event-driven architectures on AWS
**Launch the CF template 
![CloudFormation Template](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=aws-event-driven-architectures-workshop&templateURL=https://aws-event-driven-architecture-workshop-assets.s3.amazonaws.com/master-v2.yaml)


## Event-driven with EventBridge
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/a914bb19-ef8a-4786-b6d8-129068ff1914)

Amazon EventBridge is a serverless event bus service that makes it easy to connect your applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your applications, Software-as-a-Service (SaaS) applications, and AWS services and routes that data to targets such as AWS Lambda. You can set up routing rules to determine where to send your data to build application architectures that react in real-time to all of your data sources.
### Concepts
* **Events** - An event indicates a change in an environment. This can be an AWS environment, a SaaS partner service or application, or one of your own custom applications or services.
* **Rules** - A rule matches incoming events and routes them to targets for processing. A single rule can route to multiple targets, all of which are processed in parallel. Rules aren't processed in a particular order. This enables different parts of an organization to look for and process the events that are of interest to them. A rule can customize the JSON sent to the target, by passing only certain parts or by overwriting it with a constant.
* **Targets** - A target processes events. Targets can include Amazon EC2 instances, Lambda functions, Kinesis streams, Amazon ECS tasks, Step Functions state machines, Amazon SNS topics, Amazon SQS queues, and built-in targets. A target receives events in JSON format.
* **Event buses** - An event bus receives events. When you create a rule, you associate it with a specific event bus, and the rule is matched only to events received by that event bus. Your account has one default event bus, which receives events from AWS services. You can create custom event buses to receive events from your custom applications. You can also create partner event buses to receive events from SaaS partner applications.

In this module, you will use EventBridge to learn how to create an event bus, route events to targets using rules, and use scheduling expressions to create recurring events.
## First event bus and targets
![eb_arch_simple_bus](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/db5aed2d-bae4-4b0c-a825-32fb427198a4)

In this module, you will create a custom EventBridge event bus, Orders, and an EventBridge rule, OrderDevRule, which matches all events sent to the Orders event bus and sends the events to a CloudWatch Logs log group, /aws/events/orders. See the diagram above:

The technique of logging all events to CloudWatch Logs is useful when implementing EventBridge rules.
### Step 1 Create a custom event bus
1. On the EventBridge homepage, under Events, select Event buses from the left navigation.
2. Click Create event bus.
3. Name the event bus Orders.
4. Leave Event archive and Schema discovery disabled, Resource-based policy blank.
5. Click Create.
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/e1265eba-fda1-4781-ab54-92d7905e36a5)

### Step 2 Set up Amazon CloudWatch target 
In this workshop, we will scope all events coming from the source com.aws.orders
1. From the left-hand menu, select Rules.
2. From the Event bus dropdown, select the Orders event bus
3. Click Create rule
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/7c7a03cc-e4cd-4a0a-acb4-7a35cfd54b21)
4. Define rule detail:
  + Add OrdersDevRule as the Name of the rule
  + Add Catchall rule for development purposes for Description
  + Select Rule with an event pattern for the Rule type
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/fd598d28-6500-4c33-bde6-22c9c6b405da)
5. In the next step, Build event pattern
  + under Event source, choose Other
  + Under Event pattern, further down the screen, enter the following pattern to catch all events from com.aws.orders:
    ```
    {
   "source": ["com.aws.orders"]
    }
    ```
  + Select next.
6. Select your rule target:
  + From the Target dropdown, select CloudWatch log group
  + Name your log group /aws/events/orders
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/a19691bb-f8b6-4982-a26b-6a81cc5c93f1)
7. Skip through the configure tags section, review your rule configuration and click Create.

### Step 3 Test your dev rule
1. Select the Event buses in the left pane and select Send events to test the newly created event rule.
2. Make sure that the custom event is populated with the following:
   + Event Bus selected to Orders
   + Source should be com.aws.orders
   + In the Detail Type add Order Notification
   + JSON payload for the Event detail should be:
     ```
     {
   "category": "lab-supplies",
   "value": 415,
   "location": "eu-west"
     }
   ```
3. Click **Send**
   ![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/f0853265-a47b-45ee-973c-188709a584cb)
4. Open the CloudWatch.
5. Choose Log groups in the left navigation and select the /aws/events/orders log group.
![](https://static.us-east-1.prod.workshops.aws/public/ad443b13-59e4-41b7-983d-cfbe6bf18983/static/images/eb_cwl_groups.png)
6. Select the Log stream
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/48b513b7-49bb-4047-b1bf-8b6b2badbd8a)
7. Toggle the log event to verify that you received the event.
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/14659cf7-5d29-421d-9c8c-e29eb29359fd)
### Step 4 Review Event structure
Due to the OrdersDevRule that you created in this section, all events to the Orders event bus will be sent to CloudWatch Logs, which you can use to view sample data to implement and troubleshoot rules matching logic.
```
{
    "version": "0",
    "id": "c04cc8c1-283c-425e-8cf6-878bbc67a628",
    "detail-type": "Order Notification",
    "source": "com.aws.orders",
    "account": "111111111111",
    "time": "2020-02-20T23:10:29Z",
    "region": "us-west-2",
    "resources": [],
    "detail": {
        "category": "lab-supplies",
        "value": 415,
        "location": "eu-west"
    }
}
```
we have our first target configured successfully. let's configure some more targets for our Orders event bus.

## Working with EventBridge rules
Rules match incoming events and routes them to targets for processing. A single rule can route to multiple targets, all of which are processed in parallel. Rules aren't processed in a particular order. A rule can customize the JSON sent to the target, by passing only certain parts or by overwriting it with a constant. EventBridge supports 28+ AWS service targets!

![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/9dee468f-4489-434b-adb9-843ddfad25a4)

In this lab, we create an Orders event bus rule to match an event with a com.aws.orders source and to send the event to an Amazon API Gateway endpoint, invoke an AWS Step Function, and send events to an Amazon Simple Notification Service (Amazon SNS) topic.
Rules use event patterns to select events and route them to targets. A pattern either matches an event or it doesn't. Event patterns are represented as JSON objects with a structure that is similar to that of events. 
### API destination target
**Task:** Process all events for source com.aws.orders via an Amazon EventBridge API Destination.
### Step 1 Identify the API URL
1. You can Find the API URL for this challenge in the **Outputs** of the CloudFormation Stack with a name containing **ApiUrl**.
### Step 2 Configure the EventBridge API Destination with basic auth security
1. On the EventBridge homepage, select API destinations from the left navigation.
2. On the API destinations page, select Create API destination.
3. On the Create API destination page
   + Enter api-destination as the Name
   + Enter the API URL identified in Step 1 as the API destination endpoint
   + Select POST as the HTTP method
   + Select Create a new connection for the Connection
   + Enter basic-auth-connection as the Connection name
   + Select Basic (Username/Password) as the Authorization type
   + Enter myUsername as the Username
   + Enter myPassword as the Password
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/72883c72-f819-4205-9e4a-543c9155ed1d)
4. Click Create
### Step 3 Configure an EventBridge Rule to target the EventBridge API Destination
1. From the left-hand menu, select Rules.
2. From the Event bus dropdown, select the Orders event bus.
3. Click Create rule
4. On the Define rule detail page
  + Enter OrdersEventsRule as the Name of the rule
  + Enter Send com.aws.orders source events to API Destination for Description
5. Under Build event pattern
    - Choose Other for your Event source
    - Copy and paste the following into the Event pattern, and select Next to specify your target:
  ```
      {
    "source": [
        "com.aws.orders"
    ]
      }
  ```
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/0cfc5eef-bc93-4eef-9db5-2821e19696cb)
6. Select your rule target:
    - Select EventBridge API destination as the target type.
    - Select api-destination from the list of existing API destinations
    
  ![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/be67f7ed-7e9c-4930-9f65-d663d2d7a5ef)
7. Click Next and finish walking through the rest of the walk-through to create the rule.
### Step 4 Send test Orders event
Using the Send events function, send the following Order Notification events from the source com.aws.orders:
```
{ "category": "lab-supplies", "value": 415, "location": "us-east" }
```
### Step 5 Verify API Destination
If the event sent to the Orders event bus matches the pattern in your rule, then the event will be sent to an API Gateway REST API endpoint.

1. Go to CloudWatch Log Groups.
2. Select the Log group with an API-Gateway-Execution-Logs prefix.
   ![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/02c3588e-8c44-408f-9d88-69e09bcebd56)

3. Select the Log stream.
4. Toggle the log event to verify the basic authorization was successful and the API responds with a 200 status.
   ![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/94ce5758-5e5d-451d-bb02-5d49606b0953)

**Congratulations!** You have successfully created your first custom event.
## Step Functions Target
### Step 1 Implement an EventBridge rule to target Step Functions
On the EventBridge concole:
1. Add a rule to the Orders event bus with the name EUOrdersRule
2. Define an event pattern to match events with a detail location in eu-west or eu-east
3. Target the OrderProcessing Step Functions state machine
### Step 2 Send test EU Orders events
Using the Send events function, send the following Order Notification events from the source com.aws.orders:
```
{ "category": "office-supplies", "value": 300, "location": "eu-west" }
```
```
{ "category": "tech-supplies", "value": 3000, "location": "eu-east" }
```
### Step 3 Verify Step Functions workflow execution
If the event sent to the Orders event bus matches the pattern in your rule, then the event will be sent to the OrderProcessing Step Functions state machine for execution.
1. Open the AWS Management Console for Step Functions.
2. On the Step Functions homepage, open the left hand navigation and select State machines.
3. Enter OrderProcessing in the Search for state machines box and verify the state machine execution has succeeded.
The Step Functions state machine will publish an OrderProcessed event back to the Orders event bus, using a new Service Integration for EventBridge which provides a simpler solution for producing events during a workflow execution.

**Congratulations!** You have completed the Step Functions Challenge.

## SNS target
**Task:** Process only orders from US locations (us-west or us-east) that are lab-supplies using a Amazon SNS target (Orders). Similar to the previous use case, but using SNS.
### Step 1 Implement an EventBridge rule to target SNS
Use the EventBridge Console to:
1. Add a rule to the Orders event bus with the name USLabSupplyRule
2. With an event pattern to match events with a detail location in us-west or us-east, and a detail category with lab-supplies.
3. Target the Orders SNS topic

### Step 2 Send test US Orders events
Using the Send events function, send the following Order Notification events from the source com.aws.orders:
```
{ "category": "lab-supplies", "value": 415, "location": "us-east" }
```
```
{ "category": "office-supplies", "value": 1050, "location": "us-west", "signature": [ "John Doe" ] }
```
### Step 3 Verify SNS topic
If the event sent to the Orders event bus matches the pattern in your rule, then the event will be sent to the Orders SQS Queue (via Orders SNS Topic).

1. Open the AWS Management Console for SQS
2. On the SQS homepage, select the Orders queue.
3. Select the Send and receive messages button.
4. Select Poll for Messages and verify the first message was delivered and the second was not.
5. To clean up, select the event, select the Delete button, and select the Delete button again on the Delete Messages confirmation dialog.
**Congratulations!** You have completed the SNS Challenge.  

## Event-driven with Lambda
When a function is invoked asynchronously, Lambda sends the event to an internal queue. A separate process reads events from the queue and executes your Lambda function.
A common event-driven architectural pattern is to use a queue or message bus for communication. This helps with resilience and scalability. Lambda asynchronous invocations can put an event or message on Amazon Simple Notification Service (SNS), Amazon Simple Queue Service (SQS), or Amazon EventBridge for further processing.With Destinations, you can route asynchronous function results as an execution record to a destination resource without writing additional code.

## AWS Lambda destinations

![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/d7fc9ce1-7408-4149-854c-1302c2f1ddb2)

This module extends the AWS Step Functions challenge completed in Working with EventBridge rules.
### Step 1 Configure the inventory bus
Configure the Inventory event bus as a successful Lambda Destination on InventoryFunction Lambda function

1. Open the AWS Management Console for Lambda
2. Select Functions in the left navigation.
3. Enter InventoryFunction in the Lambda function filter. And select the function name filter when it shows up.
4. Select the Lambda function from the list of functions.
5. In the Lambda function Designer, choose Add destination.
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/1f7505cc-ebf3-42e7-bb7f-f5ce68b668d1)

6. In the Add destination dialogue box:
   - For Condition, select On success.
   - For Destination type, select EventBridge event bus.
   - For Destination, select Inventory.

![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/b8fd3f02-3b07-47ef-8007-3089b5517780)
7. Choose Save.
The On Success Destination is displayed.
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/ec115da0-0e44-4f77-ac91-6ca6acbce330)

### Step 2 Create the "Order Processed" rule for the inventory function
The Inventory function subscribes to events that signal the processing of the order has been completed successfully. The OrderProcessed event is published by the Step Function created in the AWS Step Functions challenge.
1. Create a rule on the Orders event bus called OrderProcessingRule
2. Add a description: Handles orders successfully processed by the Order Processing state machine
3. Define a rule pattern.
```
{
    "source": [
        "com.aws.orders"
    ],
    "detail-type": [
        "Order Processed"
    ]
}
```
4. Configure the rule target to point to the Inventory function.
### Step 3 Testing the end-to-end functionality
To test the end-to-end functionality, you will publish a message to the Orders EventBridge event bus with an EU location. This will trigger the following sequence of event-driven actions:
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/e1d08db0-4d96-487b-bc26-9c952697ab9b)
* JSON payload for the Event detail should be:
```
{
  "category": "office-supplies",
  "value": 1200,
  "location": "eu-west",
  "OrderDetails": "completed"      
}
```
* Click Send
* Open the CloudWatch console
* Choose Log groups in the left navigation.
* Enter /aws/events/inventory in the Log Group Filter and choose /aws/events/inventory log group.
* In the list of Log Streams, choose the Log Stream.
* Expand the Log Stream record to verify success and explore the event schema.
  ![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/c6c08738-0701-469b-8c5e-de99497ff5cd)
**Congratulations!** You have successfully used Lambda Destinations to send a message to the Inventory EventBridge event bus, following message processing through EventBridge, Step Functions, and SNS.
## Event-driven with SNS
In addition to Amazon EventBridge, event-driven applications can also be developed using Amazon Simple Notification Service (SNS). Amazon SNS is recommended when you want to build an application that reacts to high throughput or low latency messages published by other applications or microservices (as Amazon SNS provides nearly unlimited throughput), or for applications that need very high fan-out (thousands or millions of endpoints). Messages are unstructured and can be in any format.
In this lab, we  build on a simple pub/sub implementation using Amazon SNS as our publishing service and Amazon SQS as a subscriber (you will use the queue to validate message delivery)
### Simple pub/sub
An Amazon SNS topic will be used to publish events to an Amazon SQS queue subscriber. This will allow you to easily verify the successful delivery of your messages. An Amazon SNS topic is a logical access point that acts as a communication channel. A topic lets you group multiple endpoints (such as AWS Lambda, Amazon SQS, HTTP/S, or an email address).
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/5e8949ee-188e-48b4-9640-52011808b079)
### Step 1 Create the Orders SQS queue
Create an Amazon SQS queue, also called Orders, to durably store Order messages.
1. Open the SQS on consolw
2. click Create queue at the top of your queue list.
3. Enter a queue name OrdersQueue
4. Select Standard Queue for the type of queue you want to configure.
5. Choose Create queue
6. The OrdersQueue queue is created and selected in the queue list.
### Step 2 Subscribe the OrdersQueue SQS queue to the OrderQueue SNS topic
To receive messages published to a topic, you must subscribe an endpoint to the topic.When you subscribe an endpoint to a topic, the endpoint begins to receive messages published to the associated topic.
1. From the list of queues, choose the OrdersQueue queue to which to subscribe to the Orders Amazon SNS topic.
2. From Queue Actions, select Subscribe Queue to SNS Topic.
3. From the Specify an Amazon SNS topic drop-down list, select the Orders topic to which to subscribe the OrdersQueue queue, and then choose Save.

![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/debe3e94-2d16-4b7f-8ca1-9f78acc7f826)
4. Verify that the OrdersQueue SQS queue is successfully subscribed to the Orders and is displayed in SNS Subscriptions tab.
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/d022faf6-0e1a-4970-9ced-91ba3ede8376)
The queue is subscribed to the topic. Note that the Access policy tab displays the SQS Policy that was added, allowing access for the Orders SNS topic to send messages to the OrdersQueue SQS queue.
### Step 3 Publish a test message using the Publish message functionality
To verify the result of the subscription, you will use the Publish Message functionality to publish to the topic and then view the message that the topic sends to the queue.
1. Select Topics in the left pane of the Amazon SNS service, select Orders topics from the list of Topics and click on Publish message.
2. Enter Test message in the Message body
3. Choose Publish message to publish the message to the Orders SNS topic.
   ![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/60912f05-69e3-4615-97d3-646f0a37752e)
### Step 4 Verify message delivery
1. Open SQS window
2. From the list of queues, choose the OrdersQueue queue. Note the OrdersQueue queue now shows the value 1 in the Messages Available column in the list. This means the Orders SNS topic has successfully sent the message to the queue.

![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/01a2b47c-6fea-41ac-9900-8ef8464bba24)
3. select Send and receive messages.
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/d69559e5-2d49-4508-8778-212464addc65)
4. On details screen, choose Poll for messages.
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/fe1039e3-288c-4ede-ba0d-35a2cefe9016)
Amazon SQS begins to poll the messages in the queue. The dialog box displays a message from the queue. A progress bar at the bottom of the dialog box displays the status of the message's visibility timeout.
The following example shows the ID, Sent, Size and Receive Count columns.
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/2dca957f-46b9-4aee-af24-0f358e593774)
5. Before the visibility timeout expires, select the message that you want to delete and then choose Delete 1 Message.
6. The selected message is deleted.
![image](https://github.com/Sudarkodi-Muthiah-repo/12weeksAWSworkshopchallenge/assets/101267167/ee324546-97d3-4723-a5a5-5ee605ae6b76)

**Congratulations!** You have successfully published a message to an SNS topic and verified that it was sent to the SQS queue subscription. 













 
 



    






