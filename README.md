# AWS Serverless DevOps for Pipeline & Cost Optimizations

This project demonstrates how to build a fully serverless CI/CD pipeline using AWS services like Lambda, CodeBuild, CodeDeploy, SNS, and CloudWatch Events.

## Key Features
- Serverless CI/CD pipeline
- Blue/Green deployment with AWS CodeDeploy
- Event-driven architecture using AWS Lambda
- Cost reduction & build speed optimization

## Architecture Overview
- **Source:** GitHub or CodeCommit
- **Build:** CodeBuild using `buildspec.yml`
- **Package Upload:** To S3 bucket
- **Deploy:** CodeDeploy triggered via Lambda
- **Notify:** SNS for pipeline success/failure
- **Monitor:** CloudWatch rules for automation

## Setup
1. Deploy the Lambda in `/lambda/trigger_codedeploy.py`
2. Configure your IAM roles and permissions.
3. Update S3 bucket names and Lambda function names in `buildspec.yml`
4. Push code changes to trigger pipeline.

## Folder Structure
```
aws-serverless-cicd/
├── buildspec.yml
├── appspec.yml
├── requirements.txt
├── lambda/
│   └── trigger_codedeploy.py
├── scripts/
│   ├── before_install.sh
│   ├── after_install.sh
│   ├── start_server.sh
│   └── validate_service.sh
└── README.md
```

## Author
Harinath Inturi

## License
MIT
