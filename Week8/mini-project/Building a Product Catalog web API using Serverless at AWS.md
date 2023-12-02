# Building a Product Catalog web API using Serverless at AWS
## Overview
you’ll explore a real-world scenario as an experienced engineer hired to help build a scalable, resilient, and fault-tolerant web API that provides data to an ecosystem of microservices. According to the specifications, the web API allows requests only from authorized sources, is responsible for delivering information about all products in the company’s catalog, and allows other services to keep the product catalog updated.

With all this information in mind, you’ve decided to rely on an AWS serverless architecture based on Amazon API Gateway, AWS Lambda and Amazon DynamoDB whereas the products catalog will reside on DynamoDB.
## Solution Architecture
![Architecture](Images/Architecture.png)
### Step 1 create a table in Amazon DynamoDB that will serve as your products catalog database
At the top of the AWS Management Console, in the search bar, search for and choose DynamoDB. On the left navigation menu, choose Tables.
* Choose Create table.
* As your Table name, enter acme_products
* As your Partition key, enter uuid and keep it as a String.
* Leave Sort key field empty.
* Choose  Customize settings
* This will expand more configurations options.
Scroll down to Secondary indexes section and choose Create global index .
From the New global secondary index window, configure the following options:
* Partition key: visible
* Data type: String 
* Sort key: Leave blank
* Index name: 
* visible-index
* Attribute projections:  All
* Choose Create index.
You are taken back to the Create table page. Leave all remaining options with their default values.
Scroll down and choose Create table.

![dynamodb](Images/dynamdb_table6.png)

> Note: It takes a few seconds to provision the table. As soon as it finishes, the table is ready to be used.
> You can select your acme_products table and browse through the navigation tabs to view available configuration options for the table.

🎉Congratulations! You have successfully created a table in Amazon DynamoDB that will serve as your products catalog database.
## AWS Lambda
### CREATE PRODUCT LAMBDA FUNCTION CREATION
* At the top of the DynamoDB Management Console, in the search bar, search for and choose Lambda
* In the left menu, choose Functions.
* Choose Create function .
* Choose  Author from scratch .
* Configure the following options from the Basic information section.
* Function name: acme_create_product
* Runtime: Python 3.9 
* Archictecture:  x86_64
Permissions:
* Expand  Change default execution role.
* Execution role:  Use an existing role
* Existing role: ACMEAPILambdaExecutionRole 
> Note: This role grants this Lambda function and other permissions needed to interact with DynamoDB.
* Choose Create function
![](Images/create_product_lambda4.png)
Scroll down to the Code source section. Copy and paste the code below, replacing the existing code in the lambda_function.py file.
acme_create_product.py
* Choose Deploy
Test the function.
* Choose Test
The Configure test event dialog window opens.
* Configure the following options.
  + Event name: ACMECreateProductTest
  + Event sharing settings:  Private
  + Template - optional: hello-world
  + Event JSON: Copy and paste the code below.
  ```
  {
    "name": "Some Cool Product Name",
    "visible": "1"
  }
  ```
  * Choose Save to finish the test setup.
    Image
  * Choose Test
  It will open a second tab named Execution results and, if the test runs without errors, you will see a Response with a statusCode equals to 200.
![](Images/create_product_lambda9.png)

Take advantage of the test feature and create more products. This will facilitate your tests in the future.

* At the top of the DynamoDB Management Console, in the search bar, search for and choose DynamoDB.
* Choose Tables from the menu on the left.
* Choose the acme_products text link to open the table details.
* Choose Explore table items.
You see items there that were written by your function.
![](Images/create_product_lambda10.png)

### Step 2.2 2.2: GET PRODUCT LAMBDA FUNCTION CREATION
Return to your Lambda functions main screen.
* Choose Create function .
* Choose  Author from scratch .
* Configure the following options from the Basic information section.
* Function name: acme_get_product
* Runtime: Python 3.9 
* Archictecture:  x86_64
Permissions:
* Expand  Change default execution role.
* Execution role:  Use an existing role
* Existing role: ACMEAPILambdaExecutionRole 
* Choose Create function
  ![](Images/get_product_lamda3.png)
* Scroll down to the Code source section.
* Copy and paste the code below, replacing the existing code in the lambda_function.py file.
```
Week8/Code/acme_get_product.py
```
* After pasting the code, choose Deploy
* Choose Test 
The Configure test event dialog window opens.
Configure the following options.
 + Test event action:  Create new event
 + Event name: ACMEGetProductTest
 + Event sharing settings:  Private
 + Template - optional: hello-world
 + Event JSON: Copy and paste the code below.
```
{
    "uuid": "replace_with_a_valid_uuid"
}
```
* Scroll down and choose Save to finish the test setup.
 ![](Images/get_product_lamda7.png)
  
 * Choose Test
It will open a second tab called Execution results and, if the test runs without errors, you will see a Response with an HTTPStatusCode equals to 200 and an Item key with the data related to the product uuid you passed.

 ![](Images/get_product_lamda8.png)

### Step 2.3 UPDATE PRODUCT LAMBDA FUNCTION CREATION
* Return to your Lambda functions main screen.
* Choose Create function 
* Choose  Author from scratch .
* Configure the following options from the Basic information section.
* Function name: acme_update_product
* Runtime: Python 3.9 
* Archictecture:  x86_64
Permissions:
* Expand  Change default execution role.
* Execution role:  Use an existing role
* Existing role: ACMEAPILambdaExecutionRole 
* Choose Create function

![Lambda Image](Images/update_product_lambda3.png)
* Scroll down to the Code source section.
* Copy and paste the code below, replacing the existing code in the lambda_function.py file.
  ![](Week8/Code/acme_update_product.py)
  
* After pasting the code choose Deploy
his function is going to be used to update one product by its uuid.
* Choose Test
The Configure test event dialog window opens.
* Configure the following options.
* Test event action:  Create new event
* Event name: ACMEUpdateProductTest
* Event sharing settings:  Private
* Template - optional: hello-world
* Event JSON: Copy and paste the code below.
  ```
  {
    "uuid": "replace_with_a_valid_uuid",
    "visible": "1",
    "name": "Some UPDATED Product Name"
  }
  ```
  > Caution: You have to get a valid uuid in your DynamoDB table items to test.
  
Scroll down and choose Save to finish the test setup.
* Choose Test  
It will open a second tab called Execution results and, if the test runs without errors, you will see a Response with an HTTPStatusCode equals to 200 and the Attributes key with the updated data related to the product uuid you passed.


![Lambda Image](Images/update_product_lambda8.png)

>  Note: If you want to double check the updated data, you can go back to DynamoDB and browse items there.

## Step 2.4 DELETE PRODUCT LAMBDA FUNCTION CREATION
* Back to your Lambda functions main screen.
* Choose Create function .
* Choose  Author from scratch .
Configure the following options from the Basic information section.
* Function name: acme_delete_product
* Runtime: Python 3.9 
* Architecture:  x86_64
Permissions:
* Expand  Change default execution role.
* Execution role:  Use an existing role
* Existing role: ACMEAPILambdaExecutionRole 
* Choose Create function

  
![Lambda Image](Images/delete_product_lambda3.png)

* Scroll down to the Code source section.
* Copy and paste the code below, replacing the existing code in the lambda_function.py file.
![acme_delete_product.py](/Week8/Code/acme_delete_product.py)
* After pasting the code, choose Deploy
This function is going to be used to delete a product by its uuid.
* Choose Test 
The Configure test event dialog window opens.
Configure the following options.
* Test event action:  Create new event
* Event name: ACMEDeleteProductTest
* Event sharing settings:  Private
* Template - optional: hello-world
* Event JSON: Copy and paste the code below.
```
{
    "uuid": "replace_with_a_valid_uuid"
}
```
 > Caution: You have to get a valid uuid in your DynamoDB table items to test.
* Scroll down and choose Save to finish the test setup.
* Choose Test  
It will open a second tab called Execution results and, if the test runs without errors, you see a Response with an HTTPStatusCode equal to 200.
The data related to the uuid you passed was deleted from DynamoDB.

![Lambda Image](Images/delete_product_lambda8.png)

## Step 2.5 LIST PRODUCTS LAMBDA FUNCTION CREATION
* Back to your Lambda functions main screen.
* Choose Create function .
* Choose  Author from scratch .
* Configure the following options from the Basic information section.
* Function name: acme_list_products
* Runtime: Python 3.9 
* Architecture:  x86_64
Permissions:
* Expand  Change default execution role.
* Execution role:  Use an existing role
* Existing role: ACMEAPILambdaExecutionRole 
* Choose Create function
  
  ![Lambda Image](Images/list_product_lambda3.png)
  
* Scroll down to the Code source section.
* Copy and paste the code below, replacing the existing code in the lambda_function.py file.
  ![acme_list_products.py](/Week8/Code/acme_list_products.py)
* Choose the Deploy
This function is going to be used to retrieve all visible products from our DynamoDB table. You can test it creating a test just like you did before. It is not necessary to send any payload as this function doesn’t need any extra information.
* Choose Test
The Configure test event dialog window opens.
Configure the following options.
* Test event action:  Create new event
* Event name: ACMEListProductsTest
* Event sharing settings:  Private
* Template - optional: hello-world
* Event JSON: Copy and paste the code below.
```
{}
```
It is an empty JSON as this function doesn’t need to receive any extra information.

* Scroll down and choose Save to finish the test setup.
* Choose Test
  
It will open a second tab called Execution results and, if the test runs flawlessly, you will see a Response with a HTTPStatusCode equals to 200.
You will also see in this response an array of Items that corresponds to all items you have inside your DynamoDB table.


  ![Lambda Image](Images/list_product_lambda8.png)
Test ok!

From this moment on, you have 5 working Lambda functions as follows:
+ acme_create_product
+ acme_get_product
+ acme_update_product
+ acme_delete_product
+ acme_list_products
  
🎉Congratulations! You have successfully created the required Lambda functions.
## Step 3 API Gateway
### Step 3.1 CREATE API GATEWAY
* At the top of the AWS Management Console, in the search bar, search for and choose API Gateway in a new browser tab.
* Choose APIs in your left navigation menu.
* In Choose an API type step, choose Build inside the REST API (NOT Private) box.
* Your API setup:
* Create new API:  New API.
* API name: ACME Products API
* Description: Products API that connects a web endpoint to several Lambda functions
* Regional 
* Choose Create API .
Your Amazon API Gateway is ready to be configured.
### Step 3.2: CREATE API GATEWAY RESOURCE
In this task you will create the products resource for your API Gateway.
* Click Create Resource option.
* Now in the Create Resource screen, enter the following values:
* Resource Name: products
* CORS (Cross Origin Resource Sharing): Leave checkbox de-selected.
* Choose Create resource .
Your next step is to create the methods and link them with your functions.
