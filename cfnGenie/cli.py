"""Entrypoint for cfnGenie when invoked as a module with python -m cfnGenie"""
import click
import os
from rich.prompt import Prompt


def main():
    set_aws_env()


@click.command()
@click.option('--aws_access_key_id', envvar='AWS_ACCESS_KEY_ID',
              help='Provide the AWS_ACCESS_KEY_ID as environment variable')
@click.option('--aws_secret_access_key', envvar='AWS_SECRET_ACCESS_KEY',
              help='Provide the AWS_SECRET_ACCESS_KEY as environment variable')
@click.option('--aws_session_token', envvar='AWS_SESSION_TOKEN',
              help='Provide the AWS_SESSION_TOKEN as environment variable')
@click.option('--name', required=True, help='Provide the Lambda Function Name')
def set_aws_env(aws_access_key_id, aws_secret_access_key, aws_session_token, name):
    if not aws_access_key_id:
        aws_access_key_id = Prompt.ask('Please enter your AWS Access Key ID', password=True)
        os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id

    if not aws_secret_access_key:
        aws_secret_access_key = Prompt.ask('Please enter your AWS Secret Access Key', password=True)
        os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key

    if not aws_session_token:
        aws_session_token = Prompt.ask('Please enter your AWS Session Token (optional)', password=True)
        os.environ['AWS_SESSION_TOKEN'] = aws_session_token

    click.echo(f'Lambda function name is {name}')
