from aws_cdk import (
    aws_ec2 as ec2,
    core,
)

class VpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Create a VPC
        vpc = ec2.Vpc(
            self,
            "VPC",
            cidr="10.0.0.0/16",
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE,
                    cidr_mask=24,
                ),
            ],
        )

        #Output VPC ID
        core.CfnOutput(
            self,
            "VpcId",
            value=vpc.vpc_id,
            export_name="VPCIDExport",
        )

        #Output Subnet IDs
        for index, subnet in enumerate(vpc.private_subnets):
            core.CfnOutput(
                self,
                f"PrivateSubnet{index + 1}Output",
                value=subnet.subnet_id,
                export_name=f"MyPrivateSubnet{index + 1}",
            )

app = core.App()
VpcStack(app, "VPCStack")
app.synth()