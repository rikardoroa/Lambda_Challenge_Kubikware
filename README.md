## Kubikware Challenge

###### Lambda Script que tiene como evento una URL, en donde a traves de la cual se genera un Diccionario con clave de Estado y valores del condado asociado al estado

## Instalacion Pycharm , AWS SAM y AWS CLI(Opcional) para ejecutarlo en local

* 1. **__Instalar Pycharm, AWS SAM y AWS CLI__** para ejecutar el script y probarlo en local, comparto la carpeta **__Lambda_app_aws_sam__** con el ambiente de pycharm pre configurado, solo se debe cambiar la region donde se tenga la cuenta, ya que las credenciales se asocian automaticamente a traves de pycharm, la version de AWS SAM que utiliza pycharm es con licencia, pero se puede probar un free trial de 30 dias y ejecutar la solucion, tambien se debe tener instalado docker desktop.

## Instalacion Pycharm o cualquier otro IDE para ejecutar la solucion

* 2. **__Instalar Pycharm, Visual Studio otro IDE y docker__** Si se va ejecutar el script en pycharm u otro IDE se recomienda utilizar docker para dockerizar la imagen de la lambda para desplegarla directamente en la cuenta de AWS, para esto igual es necesario tener las credenciales, las cuales tambien se pueden configurar a traves de AWS CLI, la solucion generica sin implementar AWS SAM y AWS CLI

* 3. Tener las siguientes librerias instaladas: **_pandas, y requests_**

* 4. Las librerias por defecto de Python que son utilizadas en este proyecto son: **_json, time y logging_** 

* 5. no utilize credenciales ya que todo el desarrollo fue aclopado a una Lambda en AWS por lo tanto no fue necesario, ademas que para testearlo en local use AWS SAM y AWS CLI