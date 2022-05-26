import boto3


# upload to s3 bucket
def upload_file(path: str, name: str) -> bool:
    s3 = boto3.client('s3')

    if s3.upload_file(path, 'rekognition-images-sistemas-distribuidos',f'{name}.jpg'):
        return True

    return False
