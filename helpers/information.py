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