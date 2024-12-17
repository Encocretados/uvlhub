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

[Resumen Ejecutivo](#resumen-ejecutivo-\(800-palabras\))

[Descripción del sistema](#descripción-del-sistema-\(1500-palabras\))

[Visión global del proceso de desarrollo](#visión-global-del-proceso-de-desarrollo-\(1500-palabras\))

[Entorno de desarrollo](#entorno-de-desarrollo-\(800-palabras\))

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

| Miembro del equipo | Horas    | Commits   | LoC   | Test  | Issues    | Work Item     |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Miret Martín, José Manuel|    | 82 | +459 -77 |   24    |     13      |  Download all datasets|
| Vergara Garrido, Ramon  |  | 20 | +1526 -2034 | 7 | 5 | Advance filtering |
| Nicolalde Bravo, Alejandro   |  | 26 | +2184 -1193 | 6 | 6 | Create Communities|
| Aguilera Camino, Celia   |  | 42 | +1759 -1141 | 8 | 6 | Improve UI |
| Ruiz Delgado, Victoria del Carmen  | 0 | 0 | N/A | 0 | 2 | View user profile|
| Toro Romero, Raúl      |  | 34 | +891 -916 | 8 | 5 | Sign up Validation|
| **TOTAL** |  | 204 | +6819 -5361 | 53 | 37 | 6 |

 - **HIGH**:
 
	-  **Create Communities** *(Asignada a Nicolalde Bravo, Alejandro)*: Permite a los usuarios gestionar comunidades dentro de la plataforma, incluyendo la creación de nuevas comunidades, la exploración de una lista de comunidades existentes y sus datasets públicos, así como la posibilidad de unirse o abandonar comunidades. Además, los miembros de una comunidad pueden acceder a una nueva metodología para visualizar datasets públicos exclusivos, mientras que los usuarios también tienen la opción de gestionar la visibilidad de sus datasets.
 
 	- **Advance filtering** *(Asignada a Vergara Garrido, Ramon)*: Es un filtros avanzados que mejora la búsqueda y organización de datos en la plataforma, permitiendo a los usuarios aplicar múltiples criterios de filtrado simultáneamente, como rango de fechas, atributos específicos de datasets o palabras clave. Esto permite obtener resultados más precisos y relevantes de manera rápida, con actualizaciones instantáneas en la interfaz.
- **MEDIUM**:

  	- **Improve UI** *(Asignada a Aguilera Camino, Celia)*: Se trata de modificar la interfaz de usuario para mejorar la experiencia y usabilidad en la visualización de datasets. Estas mejoras incluyen ajustes visuales, espaciado, tipografía y otros elementos gráficos que el integrante del equipo de desarrollo responsable de este WI ha considerado necesarios.

	- **Download all datasets** *(Asignada a Miret Martín, José Manuel)*: Se implementará un botón en la pantalla inicial que permitirá descargar todos los datasets del sistema. Esto incluye ajustes en el funcionamiento interno de la aplicación para comprimir automáticamente todos los datasets en un archivo ZIP, facilitando su descarga de manera eficiente y centralizada para los usuarios.
- **LOW**:

  	- **View user profile** *(Asignada a Ruiz Delgado, Victoria del Carmen)*: Mediante este WI los usuarios podrán visualizar su perfil dentro de la plataforma. Esta vista incluirá información básica como el nombre, el correo electrónico y otros datos relevantes asociados a la cuenta del usuario, proporcionando un acceso fácil y rápido a la información personal y mejorando la experiencia de uso en la plataforma.
  	- **Sign up Validation** *(Asignada a Toro Romero, Raúl)*: Inicialmente se trataba de implementar un sistema de validación de correo electrónico que requerirá que los usuarios verifiquen su dirección de correo tanto al registrarse como al iniciar sesión. Más tarde se expandió para también validar las contraseñas en el registro de nuevos usuarios para aumentar su seguridad.


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


# Resumen Ejecutivo <!--{#resumen-ejecutivo-(800-palabras)}-->

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

---

## Descripción del sistema <!--{#descripción-del-sistema}-->

**UVLHUB** es una plataforma basada en una **aplicación web** construida con **Flask** que interactúa con múltiples componentes y servicios externos para su funcionamiento. A continuación vamos a desglosa las conexiones y flujos de datos entre los diferentes elementos del sistema:


#### **Aplicación Web (núcleo del sistema)**  
La **aplicación web** es el centro de toda la arquitectura y actúa como intermediario clave entre los usuarios y los datos. Está desarrollada utilizando **Flask**, un framework ligero y flexible de desarrollo web en Python, que facilita la creación de aplicaciones dinámicas y **APIs REST**. Flask permite gestionar solicitudes, procesar datos y devolver respuestas de manera eficiente.

- Los **usuarios** acceden a esta aplicación mediante un **navegador web**, enviando solicitudes HTTP a través de Internet.  
- La aplicación expone servicios y funcionalidades al cliente, asegurando una comunicación eficiente con otros sistemas o aplicaciones externas mediante **APIs REST**.  

Flask estructura las solicitudes a través de rutas y controladores, maneja la lógica empresarial con servicios, y se vincula con la base de datos mediante repositorios y modelos para recuperar o gestionar datos. Adicionalmente, la aplicación emplea **plantillas** para crear interfaces amigables y **formularios** para gestionar la validación de los datos suministrados por los usuarios. De esta manera, la aplicación no solo conecta a los usuarios con los datos locales y externos, sino que también garantiza un flujo claro y organizado de información entre todos los componentes del sistema.


#### **Almacenamiento Local**  
El sistema incluye **almacenamiento local** para la gestión de datos críticos necesarios para el funcionamiento interno de la aplicación. Este componente tiene dos grandes funciones:  

- **APP DATA**: La base de datos principal se implementa utilizando **MariaDB**, un sistema de gestión de bases de datos relacionales. Aquí se almacenan datos estructurados, como información de usuarios, configuraciones, y registros.  
- **Modelos UVL**: Además de los datos relacionales, se almacenan modelos UVL, los cuales son fundamentales para las operaciones del sistema.  

El almacenamiento local establece la comunicación bidireccional entre la aplicación web y estos datos. La aplicación puede **guardar** y **recuperar** información en tiempo real para atender las solicitudes de los usuarios.  


#### **API REST para Ciencia Abierta**  
La arquitectura incluye una integración con **Zenodo**, un repositorio de ciencia abierta que permite almacenar y compartir recursos científicos. A través de una **API REST**, la aplicación puede:  
- Subir datos generados en la plataforma para su publicación en Zenodo.  
- Descargar o consultar recursos científicos relevantes.  

Esta integración facilita el **compartir modelos** o información dentro de la comunidad científica, promoviendo la reutilización de datos y la colaboración abierta.


#### **API REST para AAFM (Flamapy)**  
Otro componente clave de la arquitectura es la interacción con **flamapy**, una herramienta para la gestión y análisis de modelos de características en sistemas de software. Esta comunicación se realiza también a través de una **API REST**.  

Las funcionalidades incluyen:  
- Procesamiento y análisis automatizado de **modelos UVL**.  
- Generación de métricas, validaciones y transformaciones de modelos en tiempo real.  

La conexión con Flamapy permite a la aplicación ampliar sus capacidades y realizar operaciones complejas relacionadas con el manejo de **modelos de características**.  


#### **Interacción con el Navegador Web**  
Los **usuarios finales** acceden a la aplicación web mediante un **navegador web** (como Chrome, Firefox, etc.). Esta interacción es clave, ya que:  
- La aplicación proporciona una interfaz de usuario (UI) amigable y accesible.  
- Los usuarios envían solicitudes y reciben respuestas a través del navegador.  
- Se implementa una comunicación fluida con la aplicación web mediante **HTTP** o **APIs REST**.


### Los modelos del sistema

A continuación, detallaremos cómo funciona la arquitectura modular del repositorio **UVLHUB**, en la que cada módulo se relaciona con otros elementos para ofrecer funciones particulares dentro de la red. La estructura se fundamenta en un sistema jerárquico y vínculos directos entre módulos, lo que facilita un funcionamiento adaptable y escalable. A continuación, se explica el rol de cada módulo en la arquitectura:


#### **1. Módulo Principal: `modules`**
En la parte superior de la arquitectura se encuentra el módulo **"modules"**, que actúa como la **estructura raíz** que organiza los diferentes componentes funcionales del sistema. Desde este módulo principal se derivan los submódulos clave, que se encargan de funcionalidades específicas, tales como autenticación, gestión de datos, conexiones con sistemas externos, y análisis.


#### **2. Módulo `auth` (Autenticación)**
El módulo **auth** (autenticación) es uno de los componentes centrales y proporciona servicios relacionados con la **gestión de usuarios** y la seguridad. Entre sus funciones destacan:  
- Autenticación y autorización de usuarios.  
- Comunicación con el módulo **profile** para recuperar información de usuarios autenticados.  
- Conexión con el módulo **dataset** para garantizar el acceso a datos autorizados.  

Este módulo es fundamental para asegurar que los recursos y operaciones sean accesibles únicamente por usuarios autorizados.


#### **3. Módulo `profile` (Perfil de usuario)**  
Este módulo está relacionado directamente con **auth** y permite gestionar la **información del perfil de usuario**, como datos personales y configuraciones. Es una extensión de **auth** y se utiliza para personalizar la experiencia del usuario dentro de la plataforma.


#### **4. Módulo `dataset` (Gestión de datos)**  
El módulo **dataset** es otro de los núcleos funcionales de la plataforma. Es responsable de administrar y procesar los **datasets** (conjuntos de datos) que se utilizan dentro del sistema. Sus principales conexiones incluyen:  
- **Zenodo** (En un futuro pasará a ser `fakenodo`), lo que permite el intercambio de datos científicos mediante APIs.  
- **Explore**, que facilita la exploración de los datasets disponibles.  
- **Flamapy**, para realizar análisis sobre modelos y datos relacionados con características.  
- **Feature model**, que conecta y procesa modelos de características con base en datasets gestionados.

El módulo **dataset** actúa como intermediario entre distintas funcionalidades y servicios, facilitando la **gestión centralizada de datos**.


#### **5. Módulo `explore` (Exploración de datos)**  
El módulo **explore** está vinculado con **dataset** y facilita la **exploración y visualización** de los datos almacenados. Los usuarios pueden buscar, analizar y explorar datasets para obtener información relevante o seleccionar recursos de interés.


#### **6. Módulo `feature model` (Modelo de características)**  
El módulo **feature model** interactúa con **hubfile** y **dataset**, siendo responsable de gestionar y analizar **modelos de características**. Estos modelos representan configuraciones y variabilidades en sistemas software. Es fundamental para entender y procesar información compleja estructurada en estos modelos.


#### **7. Módulo `hubfile`**  
El módulo **hubfile** interactúa con **feature model** y **dataset**, sirviendo como un intermediario para la gestión de archivos y recursos específicos relacionados con el sistema. Este módulo facilita el flujo de información entre componentes y permite manejar configuraciones o archivos particulares.


#### **8. Módulos `public`, `teams`, y `webhook`**  
Estos módulos ofrecen funcionalidades adicionales:  
- **Public**: Proporciona recursos públicos que no requieren autenticación.  
- **Teams**: Facilita la colaboración entre múltiples usuarios o grupos dentro de la plataforma.  
- **Webhook**: Permite integrar servicios externos y notificaciones mediante **webhooks**, automatizando tareas y mejorando la interoperabilidad.

### Estructura del proyecto

Ahora pasamos a explicar la **estructura de archivos y carpetas** de un repositorio, dividiendo los componentes en categorías específicas según su funcionalidad y propósito:


#### **Repository Configuration (Configuración del Repositorio)**
Esta sección incluye archivos y carpetas relacionados con la **configuración del repositorio** para su funcionamiento en plataformas como GitHub y para el control de versiones.  
- **`.github`**: Carpeta que probablemente contiene flujos de trabajo (workflows) de GitHub Actions, plantillas de issues o pull requests.  
- **`.gitignore`**: Archivo que define qué archivos o carpetas se excluyen del control de versiones.  
- **`README.md`**: Archivo de documentación principal del proyecto que suele contener instrucciones sobre instalación, uso y contribución.


#### **Application Files (Archivos de la Aplicación)**
Esta sección incluye los archivos y carpetas centrales de la aplicación.  
- **`requirements.txt`**: Archivo que especifica las dependencias necesarias para ejecutar el proyecto.  
- **`scripts`**: Carpeta que posiblemente contiene scripts de utilidad, automatización o tareas de desarrollo.  
- **`app`**: Carpeta principal de la aplicación, donde se encuentran los archivos de código.  
- **`core`**: Carpeta que contiene la funcionalidad central o lógica principal del proyecto.  
- **`migrations`**: Carpeta destinada a las migraciones de la base de datos, utilizadas en frameworks como Django o Flask.


### **Working Environment (Entorno de Trabajo)**  
Esta sección contiene archivos y carpetas relacionados con el entorno de desarrollo y despliegue.  

- **`docker`**: Carpeta que posiblemente contiene configuraciones y archivos relacionados con Docker (como `Dockerfile` o `docker-compose.yml`).  
- **`vagrant`**: Carpeta que incluye configuraciones para **Vagrant**, una herramienta de creación y gestión de máquinas virtuales.  
- **`.env.*`**: Archivos de configuración para entornos específicos (por ejemplo, desarrollo, producción), usados para **variables de entorno**.  


#### **Rosemary CLI**
Esta sección parece estar relacionada con una herramienta CLI (Command-Line Interface) personalizada llamada **Rosemary**.  
- **`rosemary`**: Carpeta o módulo específico de la herramienta.  
- **`setup.py`**: Archivo utilizado para configurar la instalación del proyecto como un paquete Python, indicando dependencias y metadatos.


#### **Configuration Files (Archivos de Configuración)**
- **`.flake8`**: Archivo de configuración para la herramienta **Flake8**, que se utiliza para el análisis de estilo y calidad del código Python.


### Peticiones HTTP

Para finalizar con la descrición general del proyecto, vamos a explicar cómo en nuestro proyecto una petición HTTP fluye desde un cliente (navegador) hasta el servidor y cómo se procesan las peticiones en la aplicación:

1. Las peticiones llegan desde **Internet**, donde la aplicación **UVLHub** es accesible públicamente.  
2. El servidor **Flask**, gestionado con **Gunicorn**, recibe las solicitudes y las redirige a **routes.py** (Controlador), que determina qué ruta y lógica ejecutar según la URL y el método HTTP.  
3. Las rutas (**routes.py**) delegan la lógica de negocio a **services.py**, que organiza las operaciones y procesos necesarios para responder a la solicitud.  
4. **services.py** interactúa con **repositories.py** para realizar consultas a la base de datos, utilizando **models.py** como estructura que define las tablas y datos.  
5. Los **formularios** (**forms.py**) se utilizan para validar y manejar los inputs proporcionados por los usuarios, como formularios de búsqueda o envío de datos.  
6. Los datos procesados se pasan a las **plantillas** (**templates**), que generan una interfaz HTML dinámica y amigable para el usuario.  
7. Finalmente, el servidor envía la respuesta al navegador del cliente, mostrando la información solicitada en forma de página web.

Este flujo modular separa claramente las responsabilidades (controlador, lógica de negocio, acceso a datos y vistas), facilitando el desarrollo, mantenimiento y escalabilidad de la aplicación.

---

## Visión global del proceso de desarrollo <!--{#visión-global-del-proceso-de-desarrollo}-->

### Planificación y diseño

La fase de planificación desempeñó un papel crucial para establecer las bases organizativas y metodológicas del proyecto. Este proceso comenzó con una serie de reuniones periódicas en las que el equipo definió y acordó aspectos clave del flujo de trabajo, diseñados para garantizar un desarrollo eficiente y ordenado. A continuación, se detallan los puntos principales tratados durante esta fase:

1. **Plantillas estándar**:  
   Se diseñaron plantillas específicas para la creación de issues, mensajes de commits y pull requests. Esto permitió al equipo mantener un enfoque uniforme en la documentación de tareas y cambios. Por ejemplo:  
   - En las issues, se incluyeron campos obligatorios como descripción, criterios de aceptación y pasos para reproducir errores (en caso de bugs).  
   - Los mensajes de commit siguieron un formato estructurado, como: feat(modulo al que afecta): descripción del cambio para funcionalidades o fix(modulo al que afecta): descripción del bug corregido, lo que facilitó el rastreo del historial de cambios.  
   - Las pull requests debían incluir un resumen detallado del cambio, capturas de pantalla (si eran relevantes) y una referencia directa a las issues vinculadas.  

   Además, se utilizó un tablero Kanban para gestionar las issues, moviéndolas a través de diferentes estados (como "Por hacer", "En progreso", "En revisión" y "Finalizado") para facilitar el seguimiento del progreso del equipo y asegurar que todas las tareas se completaran de manera organizada.

2. **Gestión de ramas**:  
   Para evitar conflictos en el código y mantener un flujo de trabajo ordenado, se definió una estrategia clara para las ramas:  
   - **main**: la rama principal siempre reflejó una versión estable y lista para producción.  
   - **Ramas funcionales**: se nombraron siguiendo un estándar descriptivo, como feature/nueva-funcionalidad. Esto permitió a los desarrolladores trabajar de manera ordenada y en sus tareas específicas sin interferir con el código de otros.  

3. **Etiquetado (labels) para las issues**:  
   Se establecieron etiquetas específicas para categorizar las issues según su tipo, prioridad y estado. Algunas de las etiquetas utilizadas fueron:  
   - **Tipo**: bug, documentation, enhancement, test, workflow.  
   - **Prioridad**: high, medium, low.  
   - **Estado o contexto**: good first issue, help wanted, question, invalid, duplicate, wontfix.  

   Estas etiquetas facilitaron la gestión del backlog, ayudando a priorizar tareas y asignarlas a los miembros del equipo según su disponibilidad y experiencia.  

   Además, se utilizó un tablero Kanban para gestionar las issues y moverlas según su estado, lo que proporcionó una visualización clara del flujo de trabajo y permitió mantener a todo el equipo alineado respecto al progreso del proyecto.

4. **Revisión de Pull Requests**:  
   Se definieron políticas estrictas para las revisiones de código. Antes de realizar un merge a la rama principal, cada pull request debía ser revisada por al menos un compañero, garantizando así la calidad del código. Durante estas revisiones, se verificaban aspectos como:  
   - Cumplimiento de los criterios de aceptación definidos en la issue.  
   - Calidad y claridad del código, incluyendo comentarios y organización.  
   - Ejecución correcta de pruebas automatizadas y ausencia de errores.  

Esta fase de planificación no solo estableció un marco sólido para el desarrollo, sino que también promovió una cultura de colaboración y calidad en el equipo.

---

### Fase de desarrollo

En la fase de desarrollo, el equipo trabajó siguiendo los lineamientos definidos en la planificación. Dos herramientas fundamentales para garantizar la consistencia y eficiencia del trabajo fueron el uso del archivo .env y el control de versiones con GitHub.

1. **Entorno de desarrollo**:  
   Se utilizó un archivo .env para gestionar variables de entorno críticas, como claves de API, credenciales y configuraciones específicas de cada entorno (desarrollo, pruebas, producción). Este enfoque permitió:  
   - **Estandarización**: Todos los miembros del equipo pudieron replicar fácilmente el entorno de desarrollo local sin riesgo de errores de configuración.  
   - **Seguridad**: Las variables sensibles se mantuvieron fuera del código fuente, reduciendo riesgos de exposición en los repositorios públicos.  

   Por ejemplo, la configuración de la base de datos local y la clave para servicios externos se definieron en este archivo, asegurando que cada desarrollador trabajara bajo las mismas condiciones.

2. **Control de versiones con GitHub**:  
   GitHub fue el pilar principal para la gestión del código fuente y la colaboración del equipo. Entre sus principales usos, destacan:  
   - **Ramas organizadas**: Se utilizó una estructura de ramas basada en funcionalidades, siguiendo los estándares definidos en la planificación.  
   - **Commits descriptivos**: Cada cambio realizado se documentó con mensajes claros y estructurados, facilitando la trazabilidad del proyecto.  
   - **Pull Requests**: Todas las integraciones a la rama principal (main) se realizaron a través de pull requests, asegurando que el código fuera revisado y probado antes de ser aceptado.  

   La colaboración en GitHub fue respaldada por el uso de herramientas de comunicación como **WhatsApp** y **Discord**, que permitieron mantener una interacción fluida entre los miembros del equipo. Estas plataformas facilitaron la resolución rápida de dudas y la discusión de aspectos técnicos y no técnicos del proyecto, lo que mejoró la eficiencia del trabajo en equipo.

Estas herramientas y prácticas garantizaron un desarrollo ordenado, minimizando conflictos y manteniendo un historial claro de las modificaciones realizadas.

---

### Integración Continua y Pruebas

Para mantener un nivel constante de calidad, el equipo implementó flujos de integración continua mediante **workflows de GitHub Actions**. Estos workflows ejecutaron automáticamente una serie de pruebas cada vez que se realizaban cambios en el código, ofreciendo retroalimentación inmediata sobre posibles errores o incumplimientos de estándares.

1. **Workflows automatizados**:  
   - Los workflows se activaban con cada commit o pull request, ejecutando un conjunto de tareas predefinidas, como validaciones de estilo de código y ejecución de pruebas.  
   - Las notificaciones automáticas alertaban al equipo en caso de fallos, permitiendo corregir errores rápidamente antes de que fueran integrados a las ramas principales.  

2. **Pruebas con pytest y Selenium**:  
   Para validar las funcionalidades desarrolladas, se utilizó la herramienta **pytest** para pruebas unitarias, junto con **Selenium** para realizar pruebas de automatización de interfaces de usuario. Entre las ventajas de estas herramientas destacan:  
   - **Facilidad de uso**: Su sintaxis simple permitió escribir casos de prueba de manera rápida y efectiva.  
   - **Cobertura de pruebas**: Se implementaron pruebas unitarias y funcionales para garantizar que cada componente del sistema funcionara correctamente, incluso bajo condiciones inesperadas.  

   Además, se realizaron pruebas de carga con **Locust**, lo que permitió evaluar el rendimiento del sistema bajo condiciones de alta demanda, asegurando que el sistema pudiera manejar picos de tráfico sin problemas.

   Por ejemplo, al desarrollar una nueva funcionalidad, como la validación de etiquetas en los modelos, se crearon pruebas específicas para verificar que las entradas inválidas fueran correctamente rechazadas y que el sistema respondiera adecuadamente en caso de errores.

---

### Despliegue

El despliegue del proyecto se realizó utilizando una combinación de herramientas que garantizaron consistencia, escalabilidad y facilidad de uso.

1. **Docker**:  
   Docker fue una herramienta esencial para crear contenedores que encapsularan el entorno de ejecución del proyecto. Esto permitió:  
   - **Portabilidad**: El mismo contenedor podía ejecutarse en cualquier entorno, asegurando que el sistema funcionara de manera consistente, independientemente de la plataforma.  
   - **Eficiencia**: Los contenedores se crearon con imágenes ligeras, optimizando los tiempos de despliegue.  

2. **Render**:  
   El sistema se desplegó en la plataforma **Render**, elegida por su facilidad de configuración y soporte para despliegues automatizados. Algunos beneficios de usar Render incluyen:  
   - **Actualización continua**: Render detecta automáticamente cambios en el repositorio y despliega la nueva versión del sistema sin interrupciones significativas.  
   - **Escalabilidad**: La plataforma permite escalar recursos según la demanda, asegurando que el sistema pueda manejar picos de tráfico sin problemas.

---

### Lecciones aprendidas

A lo largo del proyecto, el equipo ha aprendido valiosas lecciones que han mejorado la forma en que trabajamos y colaboramos. Entre las principales lecciones aprendidas, destacamos:

- **Trabajo con integración continua**: Hemos aprendido a trabajar bajo el modelo de integración continua, donde las pruebas se ejecutan de manera automática en cada cambio, lo que ha permitido detectar errores de forma temprana y garantizar la calidad del código antes de su integración en la rama principal.
  
- **Familiarización con GitHub**: El uso intensivo de GitHub nos ha permitido mejorar nuestras habilidades en la gestión de código fuente, en el manejo de pull requests, la revisión de código y la resolución de conflictos. También nos hemos familiarizado con las herramientas de integración continua como GitHub Actions, lo que ha optimizado nuestro flujo de trabajo.

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


