import os



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

