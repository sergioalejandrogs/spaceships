# Solución Reto SofkaU Inventario de Naves Espaciales

Esta es mi solución al reto técnico de SofkaU para ingresar a la training league en automatización de pruebas.

### Importante: 
Antes de iniciar la aplicación web es necesario importar la base de datos alojada en la carpeta raíz del proyecto ‘127_0_0_1.sql’ dentro del de bases de datos de MySQL, sugiero utilizar XAMPP, ya que fue el mismo que yo utilicé. 

Recordar revisar los datos alojados en el archivo `settings.py` para asegurarse que la configuración de la conexión a la base de datos sea correcta (esto en caso de que se manejen usuarios, hosts, passwords, puertos, etc., distintos a los proveídos por defecto por XAMPP).

### Configuración de entorno:

Este aplicativo se desarrolló usando Python 3.8.10, por lo que se sugieren esta o versiones más actualizadas para su ejecución.

Con Python instalado, abriendo una terminal cmd dentro de la carpeta raíz del proyecto, ejecutar el siguiente comando:

"""pip install -r requirements.txt"""

Al finalizar, para desplegar la aplicación en servidor local ejecutar el comando:

"""python manage.py runserver"""
