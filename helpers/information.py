import matplotlib.pyplot as plt


def graphicsBar(male, female, adult, young, sexual, bloody):

    left = [1, 2, 3, 4, 5, 6]
    height = [male, female, adult, young, bloody, sexual]
    tick_label = ['Hombre', 'Mujer', 'Mayor de edad',
                  'Menor de edad', 'Sangriento', 'Contenido sexual']

    plt.bar(left, height, tick_label=tick_label,
            width=0.8, color=['red', 'green'])

    plt.xlabel('Variables de cantidad')
    plt.ylabel('Total de datos en las imágenes')
    plt.title('Analísis obtenido')
    plt.show()

def graphicsFace(smile,glasses,contempt,anger,disgust,fear,happines,neutral,sadness,surprise,total):
    left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    height = [smile,glasses,contempt,anger,disgust,fear,happines,neutral,sadness,surprise]
    tick_label = ['Sonriendo', 'Anteojos', 'Desprecio', 'Enojado', 'Disgustado', 'Temor', 'Felicidad', 'Neutral', 'Tristeza', 'Sorpreza']
    
    plt.bar(left, height, tick_label=tick_label,
            width=0.8, color=['red', 'green'])

    plt.xlabel('Variables de cantidad')
    plt.ylabel('Total de personas en las imágenes: ' + str(total))
    plt.title('Analísis obtenido')
    plt.show()



def informationGetter(analysis_response):
    male = 0
    female = 0
    adult = 0
    young = 0
    sexual = 0
    bloody = 0

    for img_data in analysis_response:

        img_json_data = analysis_response[img_data]

        if (img_json_data['adult']['isAdultContent']):
            sexual += 1
        if (img_json_data['adult']['isGoryContent']):
            bloody += 1

        
        if (len(img_json_data['faces']) != 0):

            faces_array = img_json_data['faces']
            for i in range (len(faces_array)):
                
                if (faces_array[i]['age'] >= 18):
                    adult += 1
                else:
                    young += 1

                if(faces_array[i]['gender'] == "Male"):
                    male += 1
                else:
                    female += 1
    
    graphicsBar( male, female, adult, young, sexual, bloody )


def informationGetterFace( analysis_response ):

    smile = 0
    glasses = 0
    contempt = 0
    anger = 0
    disgust = 0
    fear = 0
    happiness = 0
    neutral = 0
    sadness = 0
    surprise = 0

    total = 0
    for img_data in analysis_response:
        img_json_data = analysis_response[img_data]

        
        for attributes in range( 0, len(img_json_data) ):
            total += 1

            if(img_json_data[attributes]['faceAttributes']['smile'] == 1.0):
                smile +=1
            if(img_json_data[attributes]['faceAttributes']['glasses'] != "NoGlasses"):
                glasses +=1
            if(img_json_data[attributes]['faceAttributes']['emotion']['contempt'] > 0.05):
                contempt +=1
            if(img_json_data[attributes]['faceAttributes']['emotion']['anger'] > 0.05):
                anger +=1
            if(img_json_data[attributes]['faceAttributes']['emotion']['disgust'] > 0.05):
                disgust +=1
            if(img_json_data[attributes]['faceAttributes']['emotion']['fear'] > 0.05):
                fear +=1              
            if(img_json_data[attributes]['faceAttributes']['emotion']['happiness'] > 0.05):
                happiness +=1              
            if(img_json_data[attributes]['faceAttributes']['emotion']['neutral'] > 0.05):
                neutral +=1              
            if(img_json_data[attributes]['faceAttributes']['emotion']['sadness'] > 0.05):
                sadness +=1              
            if(img_json_data[attributes]['faceAttributes']['emotion']['surprise'] > 0.05):
                surprise +=1

    print(total)
    graphicsFace((smile * 100 )/total ,(glasses * 100) / total ,(contempt * 100) / total ,(anger * 100) / total ,(disgust * 100) / total, (fear * 100) / total ,(happiness * 100) / total ,(neutral * 100) / total ,(sadness * 100) / total ,(surprise *100) / total , total)
                
