# Centralized Secret Management System Using AWS Secrets Manager and IAM Policies

## Project Overview

This project implements a centralized secret management solution using AWS Secrets Manager and IAM Roles to eliminate hardcoded credentials from application source code.

A Python application deployed on an AWS EC2 instance retrieves database credentials securely and dynamically from AWS Secrets Manager using the Boto3 SDK.

The implementation follows AWS security best practices by using IAM Roles and least-privilege permissions without storing AWS access keys on the EC2 instance.

## Problem Statement

During a security audit, it was identified that database credentials were stored directly inside application configuration files.

This creates security risks such as:
- Unauthorized access to sensitive information.
- Credential exposure through GitHub repositories.
- Difficulty managing and updating passwords.
- Increased security risks when credentials are compromised.

## Project Objectives

- Eliminate hardcoded database credentials.
- Store secrets centrally using AWS Secrets Manager.
- Retrieve credentials dynamically using Python Boto3.
- Implement IAM Roles for secure authentication.
- Apply least-privilege access policies.
- Validate secure application connectivity.

## Technologies Used

| Technology | Purpose |
|---|---|
| AWS EC2 | Application hosting |
| AWS Secrets Manager | Secure credential storage |
| AWS IAM | Access control |
| Python | Application development |
| Boto3 | AWS SDK |
| Linux | Operating system |
| Git & GitHub | Version control |

## Architecture Diagram

![AWS Architecture](architecture-diagram.png)

## Project Workflow

1. Launch an EC2 Linux instance.
2. Install Python and Boto3.
3. Create a secret in AWS Secrets Manager.
4. Create an IAM role for EC2.
5. Attach a least-privilege IAM policy.
6. Attach the IAM role to the EC2 instance.
7. Develop a Python application using Boto3.
8. Retrieve database credentials dynamically.
9. Connect the application to the database.
10. Validate secure access and permissions.

## Project Structure

```text
centralized-secret-management-aws/
│
├── app/
│   └── app.py
│
├── config/
│   └── iam-policy.json
│
├── screenshots/
│   ├── 01-ec2-instance.png
│   ├── 02-secrets-manager.png
│   ├── 03-iam-role.png
│   ├── 04-iam-policy.png
│   ├── 05-secret-retrieval.png
│   └── 06-application-output.png
│
├── architecture-diagram.png
├── requirements.txt
├── .gitignore
└── README.md
```

## Security Implementation

### Before Implementation
- Database username and password stored in application code.
- Credentials exposed to developers accessing the source code.
- Manual credential management.

### After Implementation
- Credentials stored securely in AWS Secrets Manager.
- Application retrieves secrets dynamically.
- IAM Role provides temporary AWS credentials.
- Least-privilege access restricts secret retrieval.
- No hardcoded AWS access keys on EC2.

## Security Validation

The following tests are performed:

- Verify successful secret retrieval.
- Verify successful database authentication.
- Confirm no AWS access keys are configured on EC2.
- Test unauthorized access to the secret.
- Verify IAM permissions are restricted to the required secret.

## Why Secret Rotation Matters

Secret rotation periodically changes database passwords and helps reduce the impact of compromised credentials.

Benefits:
- Reduces the lifetime of exposed credentials.
- Improves security.
- Supports compliance requirements.
- Reduces manual password management.

Automatic rotation is an optional enhancement that requires a configured rotation mechanism.

## Future Enhancements

- Enable automatic secret rotation.
- Integrate Amazon RDS.
- Implement AWS CloudTrail auditing.
- Configure CloudWatch monitoring.
- Integrate secret management into CI/CD pipelines.

## Conclusion

Successfully implemented a centralized secret management solution using AWS Secrets Manager, IAM Roles, EC2 and Python Boto3.

This project demonstrates secure credential management, IAM-based access control and DevSecOps security practices.

**Author:** Bhushan Jagtap

**Role:** Aspiring AWS Cloud / DevOps Engineer
