**Instituto Tecnológico de Costa Rica <br>**
**Campus Tecnológico Local San Carlos <br>**
**Principios de Sistemas Operativos - II Semestre 2021 <br>**

**Proyecto creado por:**
- Jose Ignacio Alfaro Solano <a href="https://github.com/jalfaros">GitHub<a/>
- Warner Fidel Hurtado Laguna <a href="https://github.com/warnerHurtado">GitHub<a/>
 
 
# Procesamiento de imágenes utilizando Azure Cognitive Services mediante Pyhon

<p>Mediante los servicios brindados por Microsoft llamados <strong>Azure Cognitive Services</strong> se implementaron algoritmos que permiten el procesamiento 
de imágenes, con el fin de mostrar diferentes resultados al usuario mediante el reconocimiento de ciertas características que las imágenes procesadas tienen en
común.</p>

Para el procesamiento de las imágenes se utilizaron dos servicios que se encuentran dentro de la tecnología de <strong>Azure Cognitive Services</strong> los cuales
son los siguientes: <br>

- **Computer Vision:** implementado para el reconocimiento del entorno de la imágen (multitud, concierto, ciudad), también se realiza la identificación de 
contenido explícito (racista, adulto, sexual y sangriento), además del reconocimiento de caras y su edad promedio.

- **Face API:** utilizado principalmente para el reconocimiento de emociones en imágenes que poseían rostros de persona, brindando así información característica
como emociones, edad, género y otros rasgos físicos que el servicio logra identificar.


# Puntos a considerar durante el proceso de desarollo

El punto principal a considerar es que los servicios brindados por Microsoft son de pago, por lo que el plan gratuito tiene limitaciones, principalmente en la 
cantidad de peticiones que se pueden realizar por minuto, por lo que para optar por una cartera más amplia de peticiones se debe de contratar un plan de pago. De esta manera se pueda tener una cantidad mayor de peticiones por minuto y así poder abarcar una cantidad mayor de imágenes.

# Aplicación de la solución

Para la aplicación de los servicios previamente expuestos se utilizó el lenguaje de programación Python, el cual mediante la librería **requests** se permite
realizar la petición a través de Internet mediante el protocolo HTTP y así consumir el API de Azure para realizar la petición del procesamiento de las imágene.

Para el envío de las imágenes se deben enviar codificadas en base 64 o también conocido como: **octet stream** para que así sean correctamente procesadas por 
los diferentes servicios.

Por lo que en el proceso de desarrollo se utilizó el método: 

```python
imageConverter()
```

la función principal de este método es tomar todas las imágenes de la ruta especificada que tienen extensión **.jpg** y convertirlas a base 64 para posteriormente
retornar una colección de imágenes listas para ser procesadas por Azure. Por último, con la colección de imágenes lista se procede al consumo de los dos servicios
implementados:

```python
computerVision()
faceAttributes()
```

