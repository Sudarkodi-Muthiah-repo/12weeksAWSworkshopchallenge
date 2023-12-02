# Building a Product Catalog web API using Serverless at AWS
## Overview
you’ll explore a real-world scenario as an experienced engineer hired to help build a scalable, resilient, and fault-tolerant web API that provides data to an ecosystem of microservices. According to the specifications, the web API allows requests only from authorized sources, is responsible for delivering information about all products in the company’s catalog, and allows other services to keep the product catalog updated.

With all this information in mind, you’ve decided to rely on an AWS serverless architecture based on Amazon API Gateway, AWS Lambda and Amazon DynamoDB whereas the products catalog will reside on DynamoDB.
## Solution Architecture
image

### Base architecture
** Create an Amazon DynamoDB table to use as your products catalog database
** Start to code using AWS Lambda functions to handle your catalog data (CRUD)
C Create a function that will be able to insert new products into the catalog
R Create two functions, one that will get an item from the catalog and another one to get a list of products
U Create a function that will be in charge of updating products
D Create a function that will delete products from the catalog
Create a new Amazon API Gateway and link it with your functions to expose your database to external applications.
Authorization

After having all methods tested and running, your next challenge is to protect them from public access so, you’ve decided to use AWS Lambda authorizers to validate tokens within requests.

Create an AWS Lambda to work as your token authorizer
Add this authorizer to your API’s methods
Test everything!
