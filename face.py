import  os, requests

from helpers.videoProcessor import videoProcessor
from helpers.information import informationGetterFace

from dotenv import load_dotenv
load_dotenv()

subscription_key = os.getenv('KEY_FACE')

face_api_url =  os.getenv('ENDPOINT_FACE') + '/face/v1.0/detect'

headers = dict()
headers['Ocp-Apim-Subscription-Key'] = subscription_key
headers['Content-Type'] = 'application/octet-stream'

params = {
    #'detectionModel': 'detection_03',
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceRectangle': 'false',
    'returnFaceAttributes': 'age, gender, smile, glasses, emotion'
    #facialHair, hair y otros también se pueden agregar
}


def binaryImageConverter( imagesFolderPath ):

    binaryImages: bytes = dict()

    for image_filename in os.listdir( imagesFolderPath ):

        if ( image_filename.endswith(".jpg") ):
            image_relative_path = os.path.join( imagesFolderPath, image_filename )
            imageFile = open( image_relative_path, 'rb' )        
            try:
                data = imageFile.read()
                binaryImages[ image_filename ] = data
            except: 
                print( 'An error occurred opening the image file' )
            finally:
                imageFile.close()

    return {} if len( binaryImages ) == 0 else binaryImages

def computerVisionImageAnalyzer( binaryImages, headers, params ):

    images_data_analysys = dict()
    try:
        if ( len( binaryImages ) != 0 ):       
            for data in binaryImages:
                response = requests.post(face_api_url, headers=headers, params=params, data = binaryImages[data])
                images_data_analysys[ data ] = response.json() 

            return images_data_analysys
        else:
            print("Binary images dictionary empty")
            return False
    except:
        print("Error")
        return False

video_path = 'D:\TEC\SO\SecondProject\cartoons.mp4'

if ( videoProcessor( video_path ) ):
    
    binaryImages = binaryImageConverter( r'.\\video_images\\cartoons' )
    analysys_response = computerVisionImageAnalyzer( binaryImages, headers, params )
    informationGetterFace( analysys_response )

