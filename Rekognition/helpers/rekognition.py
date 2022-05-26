import boto3


def detect_labels(photo, bucket):
    client = boto3.client('rekognition')
    response = client.recognize_celebrities(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})
    for celebrity in response['CelebrityFaces']:
        print('Name: ' + celebrity['Name'])
        smile = celebrity['Face']['Smile']
        print(f'Smile: {smile["Value"]}')
