# Building a Product Catalog web API using Serverless at AWS
## Overview
you’ll explore a real-world scenario as an experienced engineer hired to help build a scalable, resilient, and fault-tolerant web API that provides data to an ecosystem of microservices. According to the specifications, the web API allows requests only from authorized sources, is responsible for delivering information about all products in the company’s catalog, and allows other services to keep the product catalog updated.

With all this information in mind, you’ve decided to rely on an AWS serverless architecture based on Amazon API Gateway, AWS Lambda and Amazon DynamoDB whereas the products catalog will reside on DynamoDB.
## Solution Architecture
image
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

Table Inage
> Note: It takes a few seconds to provision the table. As soon as it finishes, the table is ready to be used.
> You can select your acme_products table and browse through the navigation tabs to view available configuration options for the table.
🎉Congratulations! You have successfully created a table in Amazon DynamoDB that will serve as your products catalog database.
