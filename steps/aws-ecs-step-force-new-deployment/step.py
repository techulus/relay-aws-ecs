#!/usr/bin/env python
from functools import partial

import boto3
from relay_sdk import Dynamic as D
from relay_sdk import Interface

relay = Interface()

session_token = None
try:
    session_token = relay.get(D.aws.connection.sessionToken)
except:
    pass

sess = boto3.Session(
    aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
    aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey),
    aws_session_token=session_token
)

region = relay.get(D.aws.region)
clusterName = relay.get(D.clusterName)
serviceName = relay.get(D.serviceName)

client = sess.client('ecs', region_name=region)

try:
    response = client.update_service(
        cluster=clusterName,
        service=serviceName,
        forceNewDeployment=True
    )
    print("Operation completed {}".format(serviceName))
except Exception as e:
    print(e)
