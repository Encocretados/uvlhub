# Documentación del Proyecto: UVLHub Encocretados


	Grupo: G3
	Nombre del grupo: cocreta-hub-1
	Tutor: Belén Ramos
	Curso Escolar: 2024/2025
	Asignatura: Evolución y Gestión de la Configuración


## Índice

[Miembros](#miembros)

[Indicadores del Proyecto](#indicadores-del-proyecto)

[Integración con otros equipos](#integración-con-otros-equipos)

[Resumen Ejecutivo (800 palabras)](#resumen-ejecutivo-\(800-palabras\))

[Descripción del sistema (1500 palabras)](#descripción-del-sistema-\(1500-palabras\))

[Visión global del proceso de desarrollo (1500 palabras)](#visión-global-del-proceso-de-desarrollo-\(1500-palabras\))

[Entorno de desarrollo (800 palabras)](#entorno-de-desarrollo-\(800-palabras\))

[Ejercicio de propuesta de cambio](#ejercicio-de-propuesta-de-cambio)

[Conclusiones y trabajo futuro](#conclusiones-y-trabajo-futuro)

# Miembros <!--{#miembros}-->

| **Nombre Completo**            	| **UVUS** | **Email**                   	|
|------------------------------------|----------|---------------------------------|
|Miret Martín, José Manuel | josmirmar2  | josmirmar2@alum.us.es  	|
| Vergara Garrido, Ramon      	|ramvergar| ramvergar@alum.us.es      	|
| Nicolalde Bravo, Alejandro       	| alenicbra  | alenicbra@alum.us.es    	|
| Aguilera Camino, Celia          	| celagucam| celagucam@alum.us.es   	|
| Ruiz Delgado, Victoria del Carmen        	| vicruidel1| vicruidel1@alum.us.es  	|
| Toro Romero, Raúl         	| rautorrom| rautorrom@alum.us.es 	|


# Indicadores del Proyecto <!--{#indicadores-del-proyecto}-->

| Miembro del equipo | Horas | Commits | LoC | Test | Issues | Work Item |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Miret Martín, José Manuel|  |  |  |  |  | Download all datasets|
| Vergara Garrido, Ramon  |  |  |  |  |  | Advance filtering |
| Nicolalde Bravo, Alejandro   |  |  |  |  |  | Create Communities|
| Aguilera Camino, Celia   |  |  |  |  |  | Improve UI |
| Ruiz Delgado, Victoria del Carmen  |  |  |  |  |  | View user profile|
| Toro Romero, Raúl  	|  |  |  |  |  | Sign up Validation|

| **TOTAL** |  |  |  |  |  |  |

 - **HIGH**:
    	- **Create Communities** *(Asignada a Nicolalde Bravo, Alejandro)*: Permite a los usuarios gestionar comunidades dentro de la plataforma, incluyendo la creación de nuevas comunidades, la exploración de una lista de comunidades existentes y sus datasets públicos, así como la posibilidad de unirse o abandonar comunidades. Además, los miembros de una comunidad pueden acceder a una nueva metodología para visualizar datasets públicos exclusivos, mientras que los usuarios también tienen la opción de gestionar la visibilidad de sus datasets.
    	- **Advance filtering** *(Asignada a Vergara Garrido, Ramon)*: Es un filtros avanzados que mejora la búsqueda y organización de datos en la plataforma, permitiendo a los usuarios aplicar múltiples criterios de filtrado simultáneamente, como rango de fechas, atributos específicos de datasets o palabras clave. Esto permite obtener resultados más precisos y relevantes de manera rápida, con actualizaciones instantáneas en la interfaz.
	- **MEDIUM**:
    	- **Improve UI** *(Asignada a Aguilera Camino, Celia)*: Se trata de modificar la interfaz de usuario para mejorar la experiencia y usabilidad en la visualización de datasets. Estas mejoras incluyen ajustes visuales, espaciado, tipografía y otros elementos gráficos que el integrante del equipo de desarrollo responsable de este WI ha considerado necesarios.
    	- **Download all datasets** *(Asignada a Miret Martín, José Manuel)*: Se implementará un botón en la pantalla inicial que permitirá descargar todos los datasets del sistema. Esto incluye ajustes en el funcionamiento interno de la aplicación para comprimir automáticamente todos los datasets en un archivo ZIP, facilitando su descarga de manera eficiente y centralizada para los usuarios.
	- **LOW**:
    	- **View user profile** *(Asignada a Ruiz Delgado, Victoria del Carmen)*: Mediante este WI los usuarios podrán visualizar su perfil dentro de la plataforma. Esta vista incluirá información básica como el nombre, el correo electrónico y otros datos relevantes asociados a la cuenta del usuario, proporcionando un acceso fácil y rápido a la información personal y mejorando la experiencia de uso en la plataforma.
    	- **Sign up Validation** *(Asignada a Toro Romero, Raúl)*: Se trata de implementar un sistema de validación de correo electrónico que requerirá que los usuarios verifiquen su dirección de correo tanto al registrarse como al iniciar sesión. Este sistema enviará un código de verificación al correo electrónico proporcionado, que los usuarios deberán ingresar en la plataforma para completar el proceso de registro o acceso.


# Integración con otros equipos <!--{#integración-con-otros-equipos}-->
# Integración entre Cocreta-Hub1 y Cocreta-Hub2

La integración entre los proyectos **Cocreta-Hub1** y **Cocreta-Hub2** fue un aspecto clave del desarrollo, y para garantizar su correcto funcionamiento se implementó un enfoque estructurado y colaborativo. Este enfoque se centró en la calidad del código, la prevención de errores y la comunicación eficiente entre los equipos.

## Flujo de trabajo para la integración

Cada grupo era responsable de desarrollar y validar su propio conjunto de funcionalidades antes de integrarlas al branch principal (`main`). Para ello, se siguió un procedimiento riguroso que garantizaba que únicamente se incorporaran cambios completos, correctos y probados al repositorio principal. Este proceso consistió en:

1. **Validación de funcionalidades**: Antes de realizar cualquier contribución al branch principal, los equipos verificaban que sus desarrollos cumplían con los siguientes criterios:
   - La funcionalidad debía estar completamente implementada.
   - El código debía haber pasado todas las pruebas unitarias y funcionales correspondientes.
   - Cualquier error detectado durante el proceso debía ser corregido antes de intentar la integración.

2. **Uso de pull requests revisadas**: Las contribuciones al branch principal se realizaban exclusivamente mediante **pull requests**. Este enfoque tenía dos objetivos principales:
   - Garantizar que los cambios fueran revisados por otros miembros del equipo, asegurando un control de calidad adicional.
   - Fomentar la colaboración y la detección temprana de posibles conflictos o problemas de integración.

Cada pull request era revisada cuidadosamente, y únicamente se aprobaban aquellas que cumplían con los estándares establecidos. Esto aseguraba que todo lo que llegaba al branch principal estuviera en condiciones óptimas, minimizando la probabilidad de introducir errores.

## Comunicación efectiva

La comunicación desempeñó un papel crucial en el éxito de la integración. Para abordar dudas, resolver conflictos y garantizar un entendimiento común entre los equipos, se establecieron las siguientes prácticas:

1. **Reuniones periódicas**: Se realizaron reuniones regulares para discutir el progreso, aclarar dudas y coordinar las tareas de integración. Estas sesiones sirvieron como un espacio para alinear expectativas y resolver problemas antes de que se convirtieran en bloqueos significativos.

2. **Comunicación continua sobre errores**: Durante el desarrollo, los equipos mantuvieron un canal abierto de comunicación para reportar errores, compartir soluciones y colaborar en la resolución de problemas de manera ágil. Este intercambio constante permitió abordar incidentes de forma rápida y efectiva, reduciendo los tiempos de resolución y mejorando la calidad del producto final.

## Prevención de errores

Gracias a este flujo de trabajo bien definido, se logró minimizar la introducción de errores en el branch principal. Al asegurarse de que cada cambio estaba completamente probado y revisado antes de integrarse, se redujeron significativamente las incidencias y se garantizó un código más estable desde el principio. Este enfoque preventivo no solo mejoró la calidad del software, sino que también contribuyó a un proceso de desarrollo más eficiente y organizado.

En conclusión, la integración entre **Cocreta-Hub1** y **Cocreta-Hub2** fue exitosa gracias a un enfoque meticuloso que combinó buenas prácticas técnicas con una comunicación efectiva. Este modelo de trabajo fomentó un desarrollo colaborativo y garantizó que el branch principal permaneciera estable y libre de errores.


# Resumen Ejecutivo *(800 palabras)* <!--{#resumen-ejecutivo-(800-palabras)}-->

El proyecto ha sido desarrollado como parte del curso universitario EGC por el grupo **Cocreta-Hub**, compuesto por los subgrupos **Cocreta-Hub-1** y **Cocreta-Hub-2**. El objetivo principal de este proyecto ha sido la mejora del sistema **UVLHub**, añadiendo nuevas características y asegurando la implementación de prácticas de integración continua (CI) y despliegue continuo (CD). Se ha puesto un enfoque especial en la gestión del código y su evolución para garantizar una mejora continua en el proyecto.

Esta aplicación es un **fork** de la versión original de **UVLHub**, a la que se le han integrado mejoras importantes y nuevas funcionalidades, sin perder las características esenciales. Las mejoras están orientadas a optimizar la experiencia del usuario, aumentando la flexibilidad, funcionalidad y comodidad del sistema.

A continuación se describe el alcance de las tareas realizadas por cada subgrupo:

El subgrupo **Cocreta-Hub-1** ha trabajado en las siguientes funcionalidades:

- **Crear Comunidades**: Esta funcionalidad permite a los usuarios gestionar comunidades dentro de la plataforma. Los usuarios pueden crear nuevas comunidades, explorar comunidades existentes y unirse o abandonar comunidades. Además, los miembros de una comunidad pueden visualizar datasets exclusivos, y tienen la opción de gestionar la visibilidad de sus propios datasets.
 
- **Filtrado Avanzado**: Se ha añadido un sistema de filtrado avanzado que mejora la búsqueda y organización de los datos. Los usuarios pueden aplicar múltiples criterios de filtrado, como rangos de fechas, atributos específicos de los datasets o palabras clave, lo que facilita la obtención de resultados más precisos y relevantes.
 
- **Mejora de la Interfaz de Usuario (UI)**: Se han realizado ajustes en la interfaz de usuario para mejorar la experiencia visual y la usabilidad, especialmente en la visualización de datasets. Estos cambios incluyen modificaciones en el espaciado, tipografía y otros elementos gráficos.
 
- **Descargar Todos los Datasets**: Se ha implementado un botón en la pantalla principal que permite a los usuarios descargar todos los datasets disponibles. Esta funcionalidad incluye la compresión automática de los datasets en un archivo ZIP para facilitar una descarga centralizada y eficiente.

- **Ver Perfil de Usuario**: Los usuarios ahora pueden ver su perfil en la plataforma, que muestra información básica como su nombre, correo electrónico y otros datos relevantes asociados a su cuenta.

- **Validación de Registro**: Se ha implementado un sistema de validación de correo electrónico durante el registro y la autenticación de usuarios. Los usuarios deben verificar su dirección de correo electrónico mediante un código de confirmación.


El subgrupo **Cocreta-Hub-2** ha trabajado en las siguientes funcionalidades:
- **IA Integration**: Este work item se centra en la integración de inteligencia artificial (IA) en el sistema. Implica la incorporación de modelos de IA, como chatbots, procesamiento de lenguaje natural (NLP), o cualquier otra tecnología de IA que optimice los procesos del sistema, brindando funcionalidades avanzadas o automatización.

- **Generate API Token**:Este work item aborda la creación y gestión de tokens de autenticación API. Los tokens permiten la autenticación segura entre sistemas y usuarios mediante la generación de claves únicas que se usan para acceder a recursos protegidos a través de la API del sistema.

- **Staging Area**: se define una zona de pruebas o área de staging donde las nuevas características y funcionalidades se prueban antes de ser implementadas en producción. Es una parte clave para asegurar que los cambios no afecten el entorno de producción y funcionen correctamente en un entorno controlado.

- **Register Developer**:Este work item se refiere a la creación de un proceso para registrar a nuevos desarrolladores en el sistema. Puede incluir la configuración de roles, permisos y autenticación para que los desarrolladores puedan acceder a las herramientas necesarias, colaborar en el proyecto y gestionar sus contribuciones de manera adecuada.

- **Dashboard**: crea una página principal que centraliza información clave del sistema.
 
- **Rating dataset**: permite a los usuarios valorar datasets mediante un sistema de puntuación.

## Descripción del sistema *(1500 palabras)* <!--{#descripción-del-sistema-(1500-palabras)}-->

*Se explicará el sistema desarrollado desde un punto de vista funcional y arquitectónico. Se hará una descripción tanto funcional como técnica de sus componentes y su relación con el resto de subsistemas. Habrá una sección que enumere explícitamente cuáles son los cambios que se han desarrollado para el proyecto.*

## Visión global del proceso de desarrollo *(1500 palabras)* <!--{#visión-global-del-proceso-de-desarrollo-(1500-palabras)}-->

*Debe dar una visión general del proceso que ha seguido enlazándolo con las herramientas que ha utilizado. Ponga un ejemplo de un cambio que se proponga al sistema y cómo abordaría todo el ciclo hasta tener ese cambio en producción. Los detalles de cómo hacer el cambio vendrán en el apartado correspondiente.*

## Entorno de desarrollo *(800 palabras)*  <!--{#entorno-de-desarrollo-(800-palabras)}-->

# Entorno de Desarrollo

En esta sección se describen los entornos utilizados durante el desarrollo del proyecto, las versiones de las herramientas empleadas y los pasos necesarios para instalar tanto el sistema principal como los subsistemas asociados. Se explica la installación manual:
## Herramientas empleadas

Todos los miembros del equipo trabajaron principalmente con Visual Studio Code, seleccionado por su versatilidad y por ofrecer una gran cantidad de extensiones útiles.

Las versiones de las dependencias y herramientas esenciales están documentadas en el archivo `requirements.txt` del proyecto.

## Métodos de instalación

El proyecto está diseñado para garantizar su funcionamiento en sistemas Linux. Aunque los usuarios de Windows o macOS pueden probar las opciones de instalación descritas, no se asegura compatibilidad total. A continuación, se explican los tres métodos de instalación disponibles:

### 1. Instalación manual

#### Clonar el repositorio:

Primero, clona el proyecto desde su repositorio oficial:

```bash
git clone https://github.com/davidgonmar/uvlhub-egc.git
cd uvlhub-egc
```

#### Instalar MariaDB:

MariaDB es el sistema de base de datos requerido. Para instalarlo en Ubuntu, ejecuta:

```bash
sudo apt install mariadb-server -y
```

#### Configurar MariaDB:

Después de la instalación, ejecuta el script de configuración para establecer los parámetros básicos de seguridad:

```bash
sudo mysql_secure_installation
```

Durante la configuración, responde a las siguientes preguntas según esta guía:

- Deja el campo de contraseña inicial vacío y presiona Enter.
- Habilita la autenticación por socket (y).
- Cambia la contraseña de root y utiliza: `uvlhubdb_root_password`.
- Elimina usuarios anónimos y bases de datos de prueba, y recarga las tablas de privilegios.

#### Crear bases de datos y usuarios:

Accede a MariaDB con:

```bash
sudo mysql -u root -p
```

Usa la contraseña `uvlhubdb_root_password`. Luego, ejecuta los siguientes comandos:

```sql
CREATE DATABASE uvlhubdb;
CREATE DATABASE uvlhubdb_test;
CREATE USER 'uvlhubdb_user'@'localhost' IDENTIFIED BY 'uvlhubdb_password';
GRANT ALL PRIVILEGES ON uvlhubdb.* TO 'uvlhubdb_user'@'localhost';
GRANT ALL PRIVILEGES ON uvlhubdb_test.* TO 'uvlhubdb_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

#### Preparar el entorno de la aplicación:

Copia el archivo de ejemplo para definir las variables de entorno necesarias:

```bash
cp .env.local.example .env
```

Para evitar conflictos con el módulo webhook, ignóralo usando el archivo `.moduleignore`:

```bash
echo "webhook" > .moduleignore
```

#### Instalar dependencias:

Crea un entorno virtual y actívalo:

```bash
sudo apt install python3.12-venv
python3.12 -m venv venv
source venv/bin/activate
```

Luego, instala las dependencias:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Instala Rosemary en modo editable para reflejar cambios dinámicamente:

```bash
pip install -e ./
```

Verifica que la instalación fue exitosa:

```bash
rosemary
```

#### Ejecutar la aplicación:

Aplica las migraciones para generar las tablas de la base de datos:

```bash
flask db upgrade
```

Genera datos de prueba para facilitar el desarrollo:

```bash
rosemary db:seed
```

Finalmente, inicia el servidor de desarrollo:

```bash
flask run --host=0.0.0.0 --reload --debug
```



## Ejercicio de propuesta de cambio <!--{#ejercicio-de-propuesta-de-cambio}-->

*Se presentará un ejercicio con una propuesta concreta de cambio en la que a partir de un cambio que se requiera, se expliquen paso por paso (incluyendo comandos y uso de herramientas) lo que hay que hacer para realizar dicho cambio. Debe ser un ejercicio ilustrativo de todo el proceso de evolución y gestión de la configuración del proyecto.*

## Conclusiones y trabajo futuro <!--{#conclusiones-y-trabajo-futuro}-->

El desarrollo e integración de los proyectos Cocreta-Hub1 y Cocreta-Hub2 permitió la construcción de un sistema robusto y funcional, destacando la importancia de la colaboración efectiva y el uso de buenas prácticas de desarrollo. A lo largo del proyecto, la constante comunicación entre los equipos y las reuniones periódicas fueron fundamentales para resolver conflictos, aclarar dudas y alinear objetivos, lo que redujo significativamente los errores y facilitó el cumplimiento de los plazos establecidos. La implementación de un flujo de trabajo riguroso, basado en validaciones estrictas y revisiones de pull requests, aseguró que el branch principal permaneciera estable , garantizando la calidad del producto final. Además, el uso de herramientas como Flake8 y la configuración de entornos de prueba facilitaron la detección y corrección de problemas, promoviendo un desarrollo más eficiente y estandarizado. Los métodos de instalación manual, mediante Docker y con Vagrant también contribuyeron al éxito del proyecto al ofrecer flexibilidad y permitir a los desarrolladores trabajar en entornos adaptados a sus necesidades sin comprometer la compatibilidad del sistema. En resumen, la combinación de buenas prácticas técnicas, una metodología estructurada y un enfoque colaborativo permitió alcanzar los objetivos planteados, entregando un producto final de alta calidad que cumplió con los requisitos establecidos.

Aunque el sistema desarrollado cumple con las expectativas iniciales, existen áreas que pueden ser mejoradas o ampliadas en el futuro para asegurar su sostenibilidad y adaptabilidad a nuevas necesidades. Estamos conscientes del trabajo que hemos realizado y de las mejoras que aún se pueden hacer, pero nos sentimos orgullosos de lo que hemos logrado. Este proyecto refleja el esfuerzo y la dedicación del equipo, así como todo lo que hemos aprendido durante el proceso. Nos quedamos con la satisfacción de haber cumplido los objetivos y con la motivación de seguir mejorando en el futuro.


