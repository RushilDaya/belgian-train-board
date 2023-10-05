
import boto3

PROFILE = 'personal'
BUCKET = 'nmbs-live-tracker'
FILE_NAME = 'index.html'

def update_webpage(view: str) -> None:
    '''
    create an index.html file with the view
    and upload it to s3 bucket
    '''
    session = boto3.Session(profile_name=PROFILE)
    s3 = session.resource('s3')
    s3.Bucket(BUCKET).put_object(Key=FILE_NAME, Body=view, ContentType='text/html')