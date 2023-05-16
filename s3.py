from aws_cdk import (
    aws_s3 as s3,
    core,
)


class S3BucketStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Create an S3 bucket
        bucket = s3.Bucket(
            self,
            "MyBucket",
            bucket_name="example-bucket-intuitive-cloud",  # Replace with your desired bucket name
            versioned=True,  # Enable versioning
            removal_policy=core.RemovalPolicy.DESTROY,  # Destroy the bucket when the stack is deleted
        )

        # Output the bucket name and ID
        core.CfnOutput(self, "BucketName", value=bucket.bucket_name)
        core.CfnOutput(self, "BucketARN", value=bucket.bucket_arn)

app = core.App()
S3BucketStack(app, "S3Stack")
app.synth()