import boto3

# first example

# creating the connection
ec2 = boto3.resource('ec2')

# launch new instance

ec2.create_instances(ImageId='ami-487a3920', InstanceType="t1.micro", MinCount=1, MaxCount=1)



