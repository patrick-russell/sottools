import os
import click
import flask_s3
from app import app

@click.command()
def upload_assets():
    flask_s3.create_all(app)

if __name__ == '__main__':
    upload_assets()

