# Building event-driven architectures on AWS
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






 
 



    






