from aws_cdk import (
    aws_ec2 as ec2,
    core,
)

class Ec2InstanceStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #Import VPC ID
        vpc_id = core.Fn.import_value("VPCIDExport")

        #Import Subnets
        subnet1_id = core.Fn.import_value("MyPrivateSubnet1")

        #Create a security group
        security_group = ec2.SecurityGroup(
            self,
            "MySecurityGroup",
            vpc=vpc_id,
            description="EC2 Security Group",
            allow_all_outbound=True
        )

        #Create an EBS volume #1
        ebs_volume1 = ec2.BlockDeviceVolume.ebs(
            volume_size=30,
            delete_on_termination=True
        )

        #Create an instance #1
        instance = ec2.Instance(
            self,
            "EC2Instance1",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.AmazonLinuxImage(),
            vpc=vpc_id,
            security_group=security_group,
            block_devices=[ebs_volume1]
        )

        #Create an EBS volume #2
        ebs_volume2 = ec2.BlockDeviceVolume.ebs(
            volume_size=30,
            delete_on_termination=True
        )

        #Create EC2 instance #2
        instance = ec2.Instance(
            self,
            "EC2Instance1",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=ec2.AmazonLinuxImage(),
            vpc=vpc_id,
            security_group=security_group,
            block_devices=[ebs_volume2]
        )

        #Output Instance ID
        core.CfnOutput(
            self,
            "InstanceId",
            value=instance.instance_id
        )

app = core.App()
Ec2InstanceStack(app, "EC2InstanceStack")
app.synth()