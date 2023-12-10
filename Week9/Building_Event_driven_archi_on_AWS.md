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

T
he technique of logging all events to CloudWatch Logs is useful when implementing EventBridge rules.
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
    






