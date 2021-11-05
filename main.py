import json as JSON, os, requests



ENDPOINT = "https://so-computer-vision-warner-ignacio.cognitiveservices.azure.com/" #Agregar el endpoint
analyze_url = ENDPOINT +  "vision/v3.1/analyze"
subscription_key = "c77ecfa86d394c9389dd239aac13b6b7" #Agregar el key para el endpoint 
headers = dict()
headers['Ocp-Apim-Subscription-Key'] = subscription_key
headers['Content-Type'] = 'application/octet-stream'
params = {'visualFeatures': 'Adult,Categories,Description,Faces', 'language' : 'es', 'model-version':'latest'}



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



binaryImages = binaryImageConverter( r'./video_images/shot_at_the_night' )




def computerVisionImageAnalyzer( binaryImages, headers, params ):

    images_data_analysys = dict()
    try:
        if ( len( binaryImages ) != 0 ):       
            for data in binaryImages:
                response = requests.post(analyze_url, headers=headers, params=params, data = binaryImages[data])
                images_data_analysys[ data ] = response.json()
        else:
            print("Binary dictionary empty")
    except:
        print("Error")




computerVisionImageAnalyzer( binaryImages, headers, params )





