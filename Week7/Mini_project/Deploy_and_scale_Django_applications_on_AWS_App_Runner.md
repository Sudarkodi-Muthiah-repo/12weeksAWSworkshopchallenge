# Deploy and scale Django applications on AWS App Runner
This tutorial covers how you can use AWS App Runner to deploy your application to an App Runner service. It shows how to deploy and scale a Django web application on AWS App Runner and how to securely connect to a managed database with Amazon Relational Database Service (Amazon RDS) for PostgreSQL.It walks through configuring the source code and deployment, the service build, and the service runtime.
## Django
Django is a high-level Python web framework that enables developers to build robust, scalable, and secure web applications quickly and efficiently. It follows the model-view-controller (MVC) architectural pattern and emphasizes the principle of "Don't Repeat Yourself" (DRY), promoting clean and reusable code.
Django is an open-source web application framework written in Python. It has many built-in features such as an object-relational mapper (ORM), URL routing, authentication system, templating system, and more, it is a popular choice for developing web applications and APIs.
## AWS App Runner
AWS App Runner makes it easy to deploy Django applications directly from a source code repository or container image. AWS App Runner provisions resources, automatically scales the number of containers up or down to meet the needs of your application, and load balances traffic to ensure high availability.
## Solution Architecture

![](/Week7/images/Project-overview.png)

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

![](/Week7/images/Django-welcome-screen.png)

### Step 2 - Preparing the application for deployment
Let’s install these two packages in our virtual environment: WSGI server such as gunicorn and WhiteNoise as a simple yet scalable option for serving static files.
```
pipenv install gunicorn==20.1.0 whitenoise==6.4.0
```
Output all installed packages in a requirements file:
```
pip freeze > requirements.txt
```
Before you can deploy to AWS App Runner, you need to make some changes to the Django **settings.py** file located in 
**django-apprunner/myproject/myproject/settings.py**
First, we need to update the ALLOWED_HOSTS to allow AWS App Runner to serve the Django application:

**settings.py**
```
ALLOWED_HOSTS = [".awsapprunner.com"]
```
Next, update and add the STATIC_URL and STATIC_ROOT settings for AWS App Runner and define WhiteNoise as staticfiles storage by adjusting the **STORAGES** setting:
```
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
```
Finally, add WhiteNoise to the middleware list:
```
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```
### step 3 - Deploying to AWS App Runner
**Configuring the deployment**
* AWS App Runner enables you to deploy from a GitHub repository or via a Docker image. In this walkthrough, you’ll use the code-based deployment from GitHub.
* In the case of AWS App Runner code-based deployments, you can define deployment configuration in the AWS Management Console or use a configuration file in your source code repository. When choosing the configuration file, any changes to the deployment options are tracked similarly to how changes to the source code are tracked.
* Create an **apprunner.yaml** file in the **django-apprunner/myproject** directory to use the configuration file approach:
  
**apprunner.yaml**
```
version: 1.0
runtime: python3
build:
  commands:
    build:
      - pip install -r requirements.txt
run:
  runtime-version: 3.8.16
  command: sh startup.sh
  network:
    port: 8000
```
To start our application, AWS App Runner must run a number of commands, such as **collectstatic** for serving static files and **gunicorn** for starting the WSGI server. Create a **startup.sh** file in the **django-apprunner/myproject** directory to list these commands:

**startup.sh**
```
#!/bin/bash
python manage.py collectstatic && gunicorn --workers 2 myproject.wsgi
```
Create a .gitignore file in the django-apprunner/myproject directory:

**.gitingnore**
```
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media
staticfiles
```
Initialize a new Git repository in the **django-apprunner/myproject** directory and push it to GitHub. Follow the below link for instructions on working with GitHub.
[](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

**My GitHub repo:** https://github.com/Sudarkodi-Muthiah-repo/Django_on_aws_apprunner





