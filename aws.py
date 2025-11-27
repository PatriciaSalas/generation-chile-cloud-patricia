import boto3
import json
 
ec2 = boto3.client('ec2')
lab_instances = ec2.describe_instances()
 
instance_id = lab_instances["Reservations"][0]["Instances"][0]["InstanceId"]
print(json.dumps(instance_id, indent=2, default=str))
 
#terminar la instancia
response = ec2.terminate_instances(InstanceIds=[instance_id])
print(json.dumps(response, indent=2, default=str))