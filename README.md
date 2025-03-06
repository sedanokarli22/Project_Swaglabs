 # Proyecto Swag Labs - Automatización de Pruebas

## Descripción

**Swag Labs** es una aplicación web demo diseñada para que los ingenieros de pruebas puedan automatizar pruebas o crear pruebas manuales e incluirlas en sus repositorios de código. El propósito de este proyecto es proporcionar un entorno de pruebas funcional donde se puedan realizar diversas acciones, como el inicio de sesión y la interacción con productos, en una aplicación de comercio electrónico.

En este repositorio, se implementan pruebas automatizadas utilizando **Selenium** y **pytest** para validar el flujo básico de inicio de sesión y agregar productos al carrito de compras.

## Tecnologías Utilizadas

- **Selenium**: Herramienta para la automatización de pruebas de aplicaciones web. Selenium interactúa con los elementos de la interfaz de usuario de la aplicación, simula acciones de usuario y valida los resultados esperados.
  
- **pytest**: Framework de pruebas para Python que permite la ejecución de pruebas unitarias y de integración. Es fácil de usar, rápido y permite la ejecución de pruebas en paralelo.

## Flujo de la Prueba

Este proyecto cubre un flujo básico de interacción con la aplicación Swag Labs:

1. **Inicio de sesión**:
   - Se ingresan las credenciales de usuario en los campos correspondientes.
   - Se valida que el inicio de sesión sea exitoso y que se redirija a la página de productos.

2. **Agregar productos al carrito**:
   - Se seleccionan dos productos de la lista de artículos disponibles.
   - Los productos seleccionados se agregan al carrito de compras.

## Requisitos

Para ejecutar las pruebas en este proyecto, necesitarás:

- **Python 3.x**
- **pip** (gestor de paquetes de Python)
- **Google Chrome** o un navegador compatible para Selenium WebDriver.
- **Chromedriver** (si se utiliza Chrome, debe ser compatible con la versión de tu navegador).

### Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/swag-labs.git
   cd swag-labs
   Instalar dependencias:

2. **Asegúrate de tener instalado pip y luego instala las dependencias necesarias**:

bash
Copiar
pip install -r requirements.txt
Las dependencias incluyen:

selenium
pytest
Instalar Chromedriver (si estás utilizando Google Chrome):

- Descarga la versión de Chromedriver compatible con tu versión de Chrome desde: https://sites.google.com/a/chromium.org/chromedriver/downloads.
- Agrega el archivo chromedriver a tu PATH o coloca el archivo en el directorio del proyecto.
  
3. **Ejecución de las Pruebas**

Una vez que hayas instalado todas las dependencias, puedes ejecutar las pruebas utilizando pytest. Las pruebas se ejecutan de la siguiente manera:

- bash
- Copiar
- pytest

Este comando ejecutará todas las pruebas definidas en los archivos del proyecto. Si todo está configurado correctamente, las pruebas de automatización se ejecutarán sin problemas y verificarán el flujo de inicio de sesión y la adición de productos al carrito.

**Descripción del Flujo de Pruebas**
El flujo de pruebas cubierto en este proyecto se lleva a cabo en los siguientes pasos:

- Inicio de sesión:

Acción: Ingresar un nombre de usuario y contraseña válidos.
Verificación: Asegurar que el nombre de usuario sea visible en la página después de un inicio de sesión exitoso.

- Agregar productos al carrito:

Acción: Agregar dos productos del inventario al carrito de compras.
Verificación: Confirmar que los productos hayan sido correctamente añadidos al carrito

 
