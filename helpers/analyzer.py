import requests


def imageAnalyzer ( analyze_url,binaryImages, headers, params ):

    images_data_analysys = dict()
    try:
        if ( len( binaryImages ) != 0 ):       
            for data in binaryImages:
                response = requests.post(analyze_url, headers=headers, params=params, data = binaryImages[data])
                images_data_analysys[ data ] = response.json() 

            return images_data_analysys
        else:
            print("Binary images dictionary empty")
            return False
    except:
        print("Error")
        return False