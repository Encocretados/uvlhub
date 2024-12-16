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

| **Nombre Completo**                | **UVUS** | **Email**                       |
|------------------------------------|----------|---------------------------------|
|Miret Martín, José Manuel | josmirmar2  | josmirmar2@alum.us.es      |
| Vergara Garrido, Ramon          |ramvergar| ramvergar@alum.us.es          |
| Nicolalde Bravo, Alejandro           | alenicbra  | alenicbra@alum.us.es        |
| Aguilera Camino, Celia              | celagucam| celagucam@alum.us.es       |
| Ruiz Delgado, Victoria del Carmen            | vicruidel1| vicruidel1@alum.us.es      |
| Toro Romero, Raúl             | rautorrom| rautorrom@alum.us.es     |


# Indicadores del Proyecto <!--{#indicadores-del-proyecto}-->

| Miembro del equipo | Horas | Commits | LoC | Test | Issues | Work Item |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Miret Martín, José Manuel|  |  |  |  |  | Download all datasets|
| Vergara Garrido, Ramon  |  |  |  |  |  | Advance filtering |
| Nicolalde Bravo, Alejandro   |  |  |  |  |  | Create Communities|
| Aguilera Camino, Celia   |  |  |  |  |  | Improve UI |
| Ruiz Delgado, Victoria del Carmen  |  |  |  |  |  | View user profile|
| Toro Romero, Raúl      |  |  |  |  |  | Sign up Validation|

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

cocreta-hub-2: *descripción de la integración*

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


## Descripción del sistema *(1500 palabras)* <!--{#descripción-del-sistema-(1500-palabras)}-->

*Se explicará el sistema desarrollado desde un punto de vista funcional y arquitectónico. Se hará una descripción tanto funcional como técnica de sus componentes y su relación con el resto de subsistemas. Habrá una sección que enumere explícitamente cuáles son los cambios que se han desarrollado para el proyecto.*

## Visión global del proceso de desarrollo *(1500 palabras)* <!--{#visión-global-del-proceso-de-desarrollo-(1500-palabras)}-->

*Debe dar una visión general del proceso que ha seguido enlazándolo con las herramientas que ha utilizado. Ponga un ejemplo de un cambio que se proponga al sistema y cómo abordaría todo el ciclo hasta tener ese cambio en producción. Los detalles de cómo hacer el cambio vendrán en el apartado correspondiente.*

## Entorno de desarrollo *(800 palabras)*  <!--{#entorno-de-desarrollo-(800-palabras)}-->

*Debe explicar cuál es el entorno de desarrollo que ha usado, cuáles son las versiones usadas y qué pasos hay que seguir para instalar tanto su sistema como los subsistemas relacionados para hacer funcionar el sistema al completo. Si se han usado distintos entornos de desarrollo por parte de distintos miembros del grupo, también debe referenciarlo aquí.*

## Ejercicio de propuesta de cambio <!--{#ejercicio-de-propuesta-de-cambio}-->

*Se presentará un ejercicio con una propuesta concreta de cambio en la que a partir de un cambio que se requiera, se expliquen paso por paso (incluyendo comandos y uso de herramientas) lo que hay que hacer para realizar dicho cambio. Debe ser un ejercicio ilustrativo de todo el proceso de evolución y gestión de la configuración del proyecto.*

## Conclusiones y trabajo futuro <!--{#conclusiones-y-trabajo-futuro}-->

*Se enunciarán algunas conclusiones y se presentará un apartado sobre las mejoras que se proponen para el futuro (curso siguiente) y que no han sido desarrolladas en el sistema que se entrega*
