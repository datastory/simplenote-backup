# coding: utf-8
from time import gmtime, strftime
from credentials import login
import requests
import boto3

headers = {
    'cookie': 'auth=' + login['auth'] + '; email="' + login['email'].replace('@', '\100') + '"; sortby=modifydate; sortorder=False'
}

def lambda_handler(event, context):
    r = requests.get('https://app.simplenote.com/export/download?key=' + login['email'].replace('@', '%40'), headers=headers)

    s3 = boto3.resource('s3')
    bucket = s3.Object(login['bucket'], 'simplenote/bckp_' + strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + '.zip')
    bucket.put(Body=r.content)