import json as JSON, os, requests

#Importaciones para los graficos
import matplotlib.pyplot as plt
#import pyplot as plt

ENDPOINT = "https://so-computer-vision-warner-ignacio.cognitiveservices.azure.com/" #Agregar el endpoint
analyze_url = ENDPOINT +  "vision/v3.1/analyze" #Si cambiamos el analyze por detect me devulve las cordenadas de ese objeto
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



binaryImages = binaryImageConverter( r'./video_images/cartoons' )

def statistics(male, female, mayor, menor, sexual, sangriento):
    # x-coordinates of left sides of bars
    left = [1, 2, 3, 4, 5, 6]

        # heights of bars
    height = [male, female, mayor, menor, sangriento, sexual]

    # labels for bars
    tick_label = ['Hombre', 'Mujer', 'Edad>18', 'edad<18', 'Sangriento', 'Sexual']

    # plotting a bar chart
    plt.bar(left, height, tick_label = tick_label,
            width = 0.8, color = ['red', 'green'])

    # # naming the x-axis
    plt.xlabel('Variables de cantidad')
    # naming the y-axis
    plt.ylabel('Total de datos en las imagenes')
    # plot title
    plt.title('Estadisticas de resultados!')

    # function to show the plot
    plt.show()
    #***s


def computerVisionImageAnalyzer( binaryImages, headers, params ):
    
    male = 0
    female = 0
    mayor = 0
    menor = 0
    sexual = 0
    sangriento =0
    try:
        if ( len( binaryImages ) != 0 ):
            for data in binaryImages:
                response = requests.post(analyze_url, headers=headers, params=params, data = binaryImages[data])

                if((response.json()['adult'])['isAdultContent']):
                    sexual += 1
                
                if((response.json()['adult'])['isGoryContent']):
                    sangriento += 1

                if( len(response.json()['faces']) > 0 ):
                    
                    for i in  range(0, len(response.json()['faces']) ):
                        #print( ((response.json()['faces'])[i])['age'] )
                        if(((response.json()['faces'])[i])['age'] < 18 ):
                            menor += 1

                        if(((response.json()['faces'])[i])['age'] >= 18 ):
                            mayor += 1

                        if(((response.json()['faces'])[i])['gender'] == "Male"):
                            male += 1
                        
                        if(((response.json()['faces'])[i])['gender'] == "Female" ):
                            female += 1

            statistics(male, female, mayor, menor, sexual, sangriento)

        else:
            print("Binary dictionary empty")
    except:
        print("Error")



computerVisionImageAnalyzer( binaryImages, headers, params )





