import boto3

def lambda_handler(event, context):
    codedeploy = boto3.client('codedeploy')
    response = codedeploy.create_deployment(
        applicationName='MyApp',
        deploymentGroupName='MyApp-DeploymentGroup',
        revision={
            'revisionType': 'S3',
            's3Location': {
                'bucket': 'my-s3-bucket',
                'key': 'my-app.zip',
                'bundleType': 'zip'
            }
        },
        deploymentConfigName='CodeDeployDefault.AllAtOnce',
        description='Triggered by Lambda after CodeBuild'
    )
    return response
