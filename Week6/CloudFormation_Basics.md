# AWS Cloud Formation Foundational Concepts 
AWS CloudFormation is a service provided by Amazon Web Services (AWS) that allows you to define and provision your infrastructure resources in a declarative way. It helps you automate the creation, management, and update of your AWS resources in a consistent and efficient manner. Here are some core concepts of AWS CloudFormation:
## Core Concepts
### Template
A CloudFormation template is a JSON or YAML file that describes the desired state of your AWS resources. It defines the resources, their properties, and any dependencies or relationships between them. Templates can be authored manually or generated using AWS CloudFormation Designer or other tools.
### Stack
A stack is a unit of deployment in CloudFormation. It represents a collection of AWS resources that are created, updated, or deleted together. A stack is created based on a CloudFormation template and has a unique name within an AWS region. Stacks provide isolation and management for the resources within them.
### Resource
A resource is an AWS service component that CloudFormation provisions and manages. Examples of resources include Amazon EC2 instances, Amazon S3 buckets, AWS Lambda functions, and more. Each resource is defined in the CloudFormation template and has properties that specify its configuration.
### Parameter
Parameters allow you to customize the behavior and configuration of your CloudFormation stack. They act as inputs to the template and can be used to provide values that vary across deployments, such as instance sizes, passwords, or environment-specific settings. Parameters can be defined in the template and supplied when creating or updating the stack.
### Output
Outputs provide information about the stack and its resources that can be useful to other parts of your AWS infrastructure or external systems. You can specify the outputs you want to expose in the CloudFormation template, and the values will be available once the stack is created. Outputs can be used for cross-stack references, passing information to other AWS services, or retrieving information after stack creation.
### Stack Policy
A stack policy is a JSON document that defines the permissions for updating or deleting resources within a stack. It allows you to control fine-grained access permissions to protect critical resources. By default, CloudFormation allows all updates and deletions, but a stack policy can be applied to restrict or allow specific actions on resources.
### Change Set
A change set is a summary of proposed changes to a CloudFormation stack. It shows the differences between the current stack configuration and the desired stack configuration defined in a template. Change sets provide a way to review and validate changes before applying them to the stack, helping to prevent unintended modifications.
### Intrinsic functions
Intrinsic functions are built-in functions that help you manage your stacks. Use intrinsic functions in your templates to assign values to properties that are not available until runtime. You can use intrinsic functions only in specific parts of a template. Currently, you can use intrinsic functions in resource properties, outputs, metadata attributes, and update policy attributes. You can also use intrinsic functions to conditionally create stack resources.
### Pseudo parameters
Pseudo parameters are parameters that are predefined by AWS CloudFormation. You don't declare them in your template. Use them the same way as you would a parameter, as the argument for the Ref function.
### Mappings
A Mappings section is a top-level section of a CloudFormation template. It is used to define maps, their keys, and values which can be then referenced in your template. The optional Mappings section matches a key to a corresponding set of named values. For example, if you want to set values based on a region, you can create a mapping that uses the region name as a key and contains the values you want to specify for each specific region. You use the Fn::FindInMap intrinsic function to retrieve values in a map.
You can't include parameters, pseudo parameters, or intrinsic functions in the Mappings section.

These concepts form the foundation of AWS CloudFormation and enable you to define, manage, and automate your infrastructure as code. By using CloudFormation, you can provision and maintain your AWS resources consistently and efficiently, and easily manage changes and updates to your infrastructure over time.

