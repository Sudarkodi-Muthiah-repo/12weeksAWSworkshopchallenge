# Deploy and scale Django applications on AWS App Runner
This tutorial covers how you can use AWS App Runner to deploy your application to an App Runner service. It shows how to deploy and scale a Django web application on AWS App Runner and how to securely connect to a managed database with Amazon Relational Database Service (Amazon RDS) for PostgreSQL.It walks through configuring the source code and deployment, the service build, and the service runtime.
## Django
Django is a high-level Python web framework that enables developers to build robust, scalable, and secure web applications quickly and efficiently. It follows the model-view-controller (MVC) architectural pattern and emphasizes the principle of "Don't Repeat Yourself" (DRY), promoting clean and reusable code.
Django is an open-source web application framework written in Python. It has many built-in features such as an object-relational mapper (ORM), URL routing, authentication system, templating system, and more, it is a popular choice for developing web applications and APIs.
## AWS App Runner
AWS App Runner makes it easy to deploy Django applications directly from a source code repository or container image. AWS App Runner provisions resources, automatically scales the number of containers up or down to meet the needs of your application, and load balances traffic to ensure high availability.
## Solution Architecture
Image

The solution you are going to set up as part of this walkthrough comprises the following elements as shown in the architecture diagram:
* An AWS App Runner service running your Django application in an AWS-managed VPC.
* An RDS for PostgreSQL database instance running in your own customer-managed VPC. App Runner privately connects to the RDS instance using AWS PrivateLink.
* AWS Secrets Manager to securely store and access the database secret from App Runner.
* A GitHub repository from which the Django application source code will be deployed.

## Walkthrough
### Step 1 - Setting up a sample Django project
As a first step, create a project directory and set up a Python virtual environment using the pipenv.
```
mkdir django-apprunner
cd django-apprunner
pipenv install
```
Next, activate the virtual environment and install Django:
```
pipenv shell
pipenv install django
```
start a new Django project using the django-admin.
```
django-admin startproject myproject
cd myproject
```
Let’s test if our application runs correctly:
```
python manage.py runserver
```
If you visit http://127.0.0.1:8000 in a web browser, then you’ll see the default Django welcome screen:
Image



