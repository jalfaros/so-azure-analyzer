from helpers.videoProcessor import videoProcessor
from helpers.imageConverter import binaryImageConverter
from helpers.analyzer import imageAnalyzer
from helpers.information import informationGetter, informationGetterFace
from dotenv import load_dotenv
import os


load_dotenv()

ENDPOINT_VISION = os.getenv('ENDPOINT_VISION')
ENDPOINT_FACE = os.getenv('ENDPOINT_FACE')
subscription_key_vision = os.getenv('KEY_VISION')
subscription_key_face = os.getenv('KEY_FACE')
headers_vision = dict()
headers_face = dict()
headers_vision['Content-Type'] = 'application/octet-stream'
headers_face['Content-Type'] = 'application/octet-stream'
headers_vision['Ocp-Apim-Subscription-Key'] = subscription_key_vision
headers_face['Ocp-Apim-Subscription-Key'] = subscription_key_face


params_vision = {'visualFeatures': 'Adult,Categories,Description,Faces', 'language' : 'es', 'model-version':'latest'}
params_face = {
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceRectangle': 'false',
    'returnFaceAttributes': 'age, gender, smile, glasses, emotion'
}




def computerVision( video_image_path ):
    binaryImages = binaryImageConverter( video_image_path )
    analysis_response = imageAnalyzer( ENDPOINT_VISION, binaryImages, headers_vision, params_vision )
    informationGetter(analysis_response)    


def faceAttributes( video_image_path ):
    binaryImages = binaryImageConverter( video_image_path )
    analysis_response = imageAnalyzer( ENDPOINT_FACE, binaryImages, headers_face, params_face )
    informationGetterFace(analysis_response)   
    
if __name__ == "__main__":
    
    # videoProcessor('./videos/faces.mp4') 
    # videoProcessor('./videos/shot_at_the_night.mp4') 
    computerVision('./video_images/faces')
    faceAttributes('./video_images/faces')