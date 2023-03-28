# Fundrivo

[![Python Version](https://img.shields.io/badge/python-3.9-blue)]()
[![Django Version](https://img.shields.io/badge/django-4.1.7-brightgreen)]()


Fundrivo es un proyecto personal que pretende ser una aplicación web para el control de finanzas personales con el uso/ayuda de Machine Learning. Actualmente se encuentra en **fase de desarrollo**.

## Aplicaciones

### Users

Esta aplicación es una extensión del modelo de users que por defecto tiene Django. La aplicación contiene los siguiente modelos:

|   Nombre  |   Descripción |
|-----------|---------------|
|   CustomUser  |   Este modelo hereda del [AbstractUser](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/) de Django. Se le añadieron los siguientes campos: birthdate, country y app_permission  |

### Transactions

En esta aplicación se realiza el proceso de ingreso de transacciones (ingresos, gastos o transferencias) por parte del usuario. La aplicación contiene los siguiente modelos:

|   Nombre  |   Descripción |
|-----------|---------------|
|   Currency    |   Monedas utilizadas en las diferentes transacciones. Su código de tres digitos (`code`) debe estar en [ISO 4217](https://es.wikipedia.org/wiki/ISO_4217). Al realizar la primera migración, se crean por defecto las monedas soportadas actualmente en el proyecto: COP y USD.  |
|   AccountCategory |   Este modelo es la representación de los tipos de cuenta que los usuarios pueden tener. Por ejemplo: cuenta de ahorros, tarjetas de crédito, activos, pasivos. Este modelo solo será accesible para el administrador de la aplicación. **Los usuarios no podrán crear** categorías de cuenta.

## Variables de Entorno

Para que el proyecto funcione de manera local, se debe crear un archivo `.env` en la ruta principal del proyecto. El archivo debe contener las siguientes variables:

|   Nombre  |   Descripción |
|-----------|---------------|
|   SECRET_KEY  |   Llave secreta que genera Django por defecto en el archivo `settings.py` |
|   PSQL_USER   |   Usuario de pgAdmin  |
|   PSQL_PASSWORD   |   Contraseña de pgAdmin   |
|   PSQL_NAME   |   Nombre de la base de datos del proyecto. Definida de manera local en pgAdmin    |
<!---|   CURRENCY_API_KEY    |   API Key brindada por [Open Exchange Rates](https://openexchangerates.org/signup)     |-->

