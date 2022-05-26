from helpers.rekognition import detect_labels
from helpers.s3 import upload_file

# if upload_file(path='C:\\Users\\jvper\\Documents\\Furb\\imagens_recognition\\willsmith.jpg', name='willsmith'):
#     print('Foi')

detect_labels(photo='willsmith.jpg',bucket='rekognition-images-sistemas-distribuidos')






