#!/usr/bin/env python 3

#Create a list of services using Python. IE: S3, Lambda, EC2, etc
#1. The list should be empty initially.

aws_services = []
sizeofAWSServices = len(aws_services)

print(aws_services)

#2. Populate the list using append or insert.

for i in ["S3", "EC2", "EKS", "VPC", "CloudFormation", "Lambda"]:
    aws_services.append(i)

#3. Print the list and the length of the list. 

print(aws_services)
print("The length of the AWS Services list is: ", len(aws_services))

#4. Remove two specific services from the list by name or by index.

del aws_services[1:3]

#5. Print the new list and the new length of the list.

print(aws_services)
print("The length of the list using the len() method is: ", len(aws_services))
