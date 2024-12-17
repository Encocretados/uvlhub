# Encocretados - Diario del Equipo

- **Grupo**: G3
- **Nombre del grupo**: cocreta-hub-1
- **Tutor**: Belén Ramos
- **Curso Escolar**: 2024/2025  
- **Asignatura**: Evolución y Gestión de la Configuración

---

## Índice

1. [Miembros del grupo](#1-miembros-del-grupo)
2. [Resumen de total de reuniones empleadas en el equipo](#2-resumen-de-total-de-reuniones-empleadas-en-el-equipo)
3. [Actas de acuerdos](#3-actas-de-acuerdos)
   - [ACTA 2024-01](#acta-2024-01)
   - [ACTA 2024-02](#acta-2024-02)
   - [ACTA 2024-03](#acta-2024-03)
   - [ACTA 2024-04](#acta-2024-04)
4. Diario por participante

---

## 1. Miembros del grupo

| **Nombre Completo**                | **UVUS** | **Email**                       |
|------------------------------------|----------|---------------------------------|
|Miret Martín, José Manuel | josmirmar2  | josmirmar2@alum.us.es      |
| Vergara Garrido, Ramon          |ramvergar| ramvergar@alum.us.es          |
| Nicolalde Bravo, Alejandro           | alenicbra  | alenicbra@alum.us.es        |
| Aguilera Camino, Celia              | celagucam| celagucam@alum.us.es       |
| Ruiz Delgado, Victoria del Carmen            | vicruidel1| vicruidel1@alum.us.es      |
| Toro Romero, Raúl             | rautorrom| rautorrom@alum.us.es     |

### Enlaces de interés:
- **Repositorio de código**: [https://github.com/Encocretados/uvlhub](https://github.com/Encocretados/uvlhub)  
- **Sistema desplegado**: []()

---

## 2. Resumen de total de reuniones empleadas en el equipo

- **Total de reuniones (TR):** 4
- **Total de reuniones presenciales (TRP):** 1
- **Total de reuniones virtuales (TRV):** 3
- **Total de tiempo empleado en reuniones presenciales (TTRP):** 1h
- **Total de tiempo empleado en reuniones virtuales (TTRV):** 2h y 30 min

---

## 3. Actas de acuerdos

### ACTA 2024-01

**Asistentes:**

- Miret Martín, José Manuel
- Vergara Garrido, Ramon
- Nicolalde Bravo, Alejandro 
- Aguilera Camino, Celia 
- Ruiz Delgado, Victoria del Carmen
- Toro Romero, Raúl

**Introducción:**

En esta reunión virstual previa al M1, se definieron los Work Items (WIs) a realizar por cada uno de los miembros del equipo. Tras esta reunión confirmamos con el equipo cocreta-hub-2 para saber cuales eran sus WI. Además se comentó, coordinandonos con el otro equipo, cual iba a ser la política de commits, la política de issues y la estrategia de ramas.

**Acuerdos tomados:**
- **Acuerdo 2024-01-01: Política de Commits**.
Todos los mensajes de commit deben seguir el siguiente formato:

    - **feat**: Añadir una nueva funcionalidad.
    - **fix**: Corregir un error.

- **Acuerdo 2024-01-02: Estrategia de Ramas**.
    - Ramas principales:
        - **`main`:** Contiene el código listo para producción.

    - Ramas dde develop:
        - **`cocreta-1`:** Contiene el código listo para producción del equipo cocreta-hub-1.
        - **`cocreta-2`:** Contiene el código listo para producción del equipo cocreta-hub-2.

    - Ramas de funcionalidad:
        - **`feature/`**:
        - Cada Work Item (WI) tiene su propia rama.
        - **Nomenclatura:** `feature/<nombre_WI>`.
            - **Ejemplo:** `feature/improveUI`.
        - Las ramas se eliminan tras fusionarse en la rama `main`.

- **Acuerdo 2024-01-03: Work Items**.
Se han discutido los WI a implementar en el proyecto. Se ha acordado los siguientes WI:  
    - **HIGH**:
        - **Create Communities** *(Asignada a Nicolalde Bravo, Alejandro)*: Permite a los usuarios gestionar comunidades dentro de la plataforma, incluyendo la creación de nuevas comunidades, la exploración de una lista de comunidades existentes y sus datasets públicos, así como la posibilidad de unirse o abandonar comunidades. Además, los miembros de una comunidad pueden acceder a una nueva metodología para visualizar datasets públicos exclusivos, mientras que los usuarios también tienen la opción de gestionar la visibilidad de sus datasets.
        - **Advance filtering** *(Asignada a Vergara Garrido, Ramon)*: Es un filtros avanzados que mejora la búsqueda y organización de datos en la plataforma, permitiendo a los usuarios aplicar múltiples criterios de filtrado simultáneamente, como rango de fechas, atributos específicos de datasets o palabras clave. Esto permite obtener resultados más precisos y relevantes de manera rápida, con actualizaciones instantáneas en la interfaz.
    - **MEDIUM**:
        - **Improve UI** *(Asignada a Aguilera Camino, Celia)*: Se trata de modificar la interfaz de usuario para mejorar la experiencia y usabilidad en la visualización de datasets. Estas mejoras incluyen ajustes visuales, espaciado, tipografía y otros elementos gráficos que el integrante del equipo de desarrollo responsable de este WI ha considerado necesarios.
        - **Download all datasets** *(Asignada a Miret Martín, José Manuel)*: Se implementará un botón en la pantalla inicial que permitirá descargar todos los datasets del sistema. Esto incluye ajustes en el funcionamiento interno de la aplicación para comprimir automáticamente todos los datasets en un archivo ZIP, facilitando su descarga de manera eficiente y centralizada para los usuarios.
    - **LOW**:
        - **View user profile** *(Asignada a Ruiz Delgado, Victoria del Carmen)*: Mediante este WI los usuarios podrán visualizar su perfil dentro de la plataforma. Esta vista incluirá información básica como el nombre, el correo electrónico y otros datos relevantes asociados a la cuenta del usuario, proporcionando un acceso fácil y rápido a la información personal y mejorando la experiencia de uso en la plataforma.
        - **Sign up Validation** *(Asignada a Toro Romero, Raúl)*: Se trata de implementar un sistema de validación de correo electrónico que requerirá que los usuarios verifiquen su dirección de correo tanto al registrarse como al iniciar sesión. Este sistema enviará un código de verificación al correo electrónico proporcionado, que los usuarios deberán ingresar en la plataforma para completar el proceso de registro o acceso. Más tarde este Work Item se expandió para validar y aumentar la seguridad de las contraseñas en el registro de nuevos usuarios. 


- **Acuerdo 2024-01-06: Política de Issues**.

Cada Work Item debe dividirse en al menos dos issues:
- Una issue para implementar la funcionalidad requerida.
- Otra issue para desarrollar las pruebas relacionadas.

### ACTA 2024-02

**Asistentes:**
- Miret Martín, José Manuel
- Vergara Garrido, Ramon
- Nicolalde Bravo, Alejandro 
- Aguilera Camino, Celia 
- Toro Romero, Raúl

**Introducción:**
En esta reunión presencial previa al M2, revisamos cada uno de los WI completados, evaluando el progreso de cada integrante e integrando en la rama principal aquellos WI que estaban terminados o suficientemente avanzados. Además, acordamos con el grupo cocreta-hub-2 que nuestro equipo se encargaría de desarrollar el WI obligatorio, conocido como fakenodo.

**Acuerdos tomados:**
- **Acuerdo 2024-02-01:** Establecer las tareas para la segunda iteración con el objetivo de prever y manejar los posibles conflictos que puedan presentarse.
- **Acuerdo 2024-02-02:** Asignar a un miembro del equipo (José Manuel Miret Martín) el WI del fakenodo, el cual es un módulo idéntico al zenodo. Sin embargo, este nuevo módulo, a diferencia del zenodo, no deberá de realizar llamadas a la API conectada, sino deberá enviar a la aplicación una respuesta json creada por el mismo desarrollador e implementada en el mismo fakenodo. De esta forma no se elaborarán demasiadas llamadas a la API.


### ACTA 2024-03

**Asistentes:**

- Miret Martín, José Manuel
- Vergara Garrido, Ramon
- Nicolalde Bravo, Alejandro 
- Aguilera Camino, Celia 
- Toro Romero, Raúl

**Introducción:**

En esta reunión, elaborada de forma virtual después de haber tenido el M2 junto con el equipo cocreta-hub-2, pusimos en común lo que a ambos equipos nos faltaba poner en el proyecto. Redefinimos la política de ramas, eliminando las ramas developer de cada equipo (cocreta-1 y cocreta-2) debido a que son innecesarias, mejoramos la documentación, mejoramos la política de commits y mejoramos la política de las issues entre otros.

**Acuerdos tomados:**

- **Acuerdo 2024-03-01: Política de issues mejorada.**  
  Todas las issues tienen que tener un comentario que siga una plantilla explicando la propia issue, donde se incluye:
  - **Descripción**
  - **Personas implicadas**: Se incluye tanto la persona que lo ha reportado como el responsable y el revisor
  - **Prioridad**: Puede ser low/medium/high
  - **Información adicional**: Si aplica

- **Acuerdo 2024-03-01: Creación de nuevas issues.**  
  Se ha acordado que también se van a elaborar issues en el caso de haber un nuevo bug o algún error/fallo en el sistema, no funcionando como debería. Este tipo de issues debe incluir:
  - **Descripción**
  - **Pasos a seguir**: Para solventar el bug
  - **Resultado esperado**
  - **Personas implicadas**: Se incluye tanto la persona que lo ha reportado como el responsable y el revisor
  - **Prioridad**: Puede ser low/medium/high
  - **Información adicional**: Si aplica

- **Acuerdo 2024-03-02: Redefinición de la política de ramas.**  
  Se ha acordado por todos los miembros de los grupos (tanto cocreta-hub-1 como cocreta-hub-2) que las ramas creadas para cada grupo (`cocreta-1` y `cocreta-2`) sean eliminadas, debido a que son innecesarias y ralentiza la integración continua si no lo vamos a subir directamente todo a la rama main.

- **Acuerdo 2024-03-03: Implementación de WIs.**  
  Se ha establecido una norma general en el grupo para seguir una correcta integración continua: Cada vez que un WI este completamente, se debe elaborar dos pull request como mínimo a la rama main, una con la implementación del código correspondiente y otra elaborando los tests, cerrando las issues correspondientes.


- **Acuerdo 2024-03-04: Correcto seguimiento de los workflows.**  
  Para seguir un correcto funcionamiento de los workflows, hemos establecido como norma general que debemos de verificar continuamente estos cada vez que hagamos cualquier cambio en el main, ya sea una pull request o un commit. En el caso que de fallo debemos solucionar ese problema de inmediato.


### ACTA 2024-04

**Asistentes:**

- Miret Martín, José Manuel
- Vergara Garrido, Ramon
- Nicolalde Bravo, Alejandro 
- Aguilera Camino, Celia 
- Toro Romero, Raúl

**Introducción:**
Pusimoe en común todo lo que teníamos hecho cada integrante del equipo. Vimos que todos los WI de los integrantes presentes funcionasen, vimos que los tests se habían hecho los necesarios por cada uno y que los workflows creados iban como deberían. Pusimos en común la información que teníamos con respecto el M3, y nos organizamos para tener todo preparado para la entrega final. Repartimos las últimas tareas necesarias. Esta reunión, como las anteriores, la hemos tenido con los miembros de cocreta-hub-2.


**Acuerdos tomados:**

- **Acuerdo 2024-04-01: Últimos cambios necesarios en los WI.**  
    Se repartieron las ultimas tareas del M3 a los integrantes del grupo presentes, tareas como por ejemplo algunos retoques finales a algunos WI, alguna documentación necesaria y algunos cambios a algunos tests.
- **Acuerdo 2024-04-02: Creación del video.**  
  Organizamos entre los miembros del equipo el como deberíamos de hacer el video explicativo de 10 minutos necesario para la entrega final, dividiendo las tareas que habían sido necesarias para su correcta elaboración.
- **Acuerdo 2024-04-03: Despliegue del proyecto.**  
  Se le ha asignado a un miembro de nuestro equipo (Nicolalde Bravo, Alejandro ) el despliegue final del proyecto en Render, siendo este uno de los requisitos necesarios para la última sesión de seguimiento del proyecto M3.

# Diario por participante
 
# Celia Aguilera Camino

## WI Asignado

Durante el período actual, me he encargado del WI "Improve_UI". Mi enfoque ha estado en mejorar la interfaz de usuario para facilitar una experiencia más fluida y atractiva para los usuarios.

## Pruebas Realizadas

He realizado un total de **4 pruebas de Selenium** y **4 pruebas unitarias** relacionadas con la funcionalidad del sistema. A continuación, se describen los detalles de las pruebas ejecutadas:

### Pruebas de Selenium

1. **Prueba de Tabla de Archivos UVL**:  
   Se verificó que la tabla que muestra los archivos esté correctamente cargada, con la presencia de los botones de "Ver", "Check" y "Export" en cada fila de la tabla. La prueba garantizó que los archivos se muestran adecuadamente y que todos los botones interactivos están disponibles.

2. **Prueba de Elementos Interactivos**:  
   Se probó el comportamiento del modal al hacer clic en el botón "Ver". Esta prueba verificó que el modal se abre y se cierra correctamente, lo que asegura la funcionalidad interactiva del sistema.

3. **Prueba de Botón "Explorar Más Conjuntos de Datos"**:  
   Verifiqué que el botón "Explore more datasets" funciona correctamente, asegurando que el sistema redirige al usuario a la página de exploración de conjuntos de datos al hacer clic.

4. **Prueba de Descarga de Todos los Conjuntos de Datos**:  
   Se realizó una prueba para verificar que la opción de "Download all datasets" descargue correctamente todos los conjuntos de datos disponibles en el sistema.

### Pruebas Unitarias

1. **Prueba de DOI Inválido**:  
   Se verificó que el sistema maneje correctamente un DOI con formato no válido, asegurando que la URL generada sea apropiada, incluso cuando el DOI es `None`.

2. **Prueba de Error Interno del Servidor**:  
   Realicé una prueba de integración para simular un error interno del servidor al intentar obtener un conjunto de datos. La prueba verificó que el sistema devuelva un código de estado 500 en caso de error, como es esperado en situaciones de fallo en el servidor.

3. **Prueba de Construcción de URL para DOI**:  
   Esta prueba unitario garantizó que el sistema genere correctamente la URL del DOI de un conjunto de datos cuando se proporciona un DOI válido, y verificó que la función `get_uvlhub_doi` construya la URL correctamente usando el dominio configurado.

4. **Prueba de Cookie Faltante**:  
   Verifiqué cómo el sistema maneja un caso en el que no se puede establecer una cookie al acceder a un conjunto de datos, asegurando que el sistema maneje correctamente la situación y se establezca la cookie de manera adecuada.

### Workflows Implementados

He implementado dos workflows para automatizar tareas en el repositorio:

1. **Workflow de Formateo de Código (Linting)**:  
   Cada vez que se hace un `push` al repositorio, este workflow asegura que el código se formatee de acuerdo con las reglas de estilo definidas mediante `lint`. Esto garantiza que el código del proyecto se mantenga limpio y consistente.

2. **Workflow de Notificación por Correo en Pull Requests**:  
   Este workflow envía un correo electrónico a todos los colaboradores del proyecto cada vez que se crea una `pull request`. El correo contiene información relevante sobre la `pull request`, como el autor, la descripción y el estado de la solicitud, asegurando que todos los miembros del equipo estén al tanto de los cambios.

## Conclusión

Durante este período, he trabajado en mejorar la interfaz de usuario y he ejecutado un conjunto completo de pruebas para asegurar la correcta funcionalidad de diferentes partes del sistema. Además, implementé workflows para mejorar la automatización de tareas y facilitar el proceso de colaboración en el proyecto. Mi enfoque ha sido garantizar una alta calidad en la interfaz y en la funcionalidad del sistema, a la vez que optimizo los procesos internos del equipo.

# Raúl Toro Romero

## WI Asignado

Me he encargado del WI "Sign up validation". Es considerado un Low Work Item así que decidí expandirlo: no solo se realiza una validación de una contraseña segura, sino que además se valida el correo de los usuarios mandándoles a su correo el código de 6 dígitos (creado de forma segura) que deben introducir en la web, tanto para registrarse (valdiación) como para iniciar sesión (autentificación).

## Pruebas Realizadas

Dentro del módulo auth he realizado un total de **7 pruebas unitarias** y **1 prueba de Selenium** relacionadas tanto como la validación de las contraseñas como con la validación del código de autentificación. A continuación, se describen los detalles de las pruebas ejecutadas:

### Pruebas Unitarias

1. **Prueba de correcta redirección**:
   Se comprueba que después de un login exitoso se redirige al endpoint correcto.

2. **Prueba de login y validación de correo exitosa**
   Se comprueba que tras un login exitoso y después de introducir el código de validación correcto, el usuario inicia sesión correctamente.

3. **Prueba de respuesta a login exitoso con validación de correo incorrecta**
   Se comprueba que tras un login exitoso y después de introducir el código de validación distinto al correcto, el usuario no inicia sesión.

4. **Prueba de contraseña de usuario sin mayúsculas ni minúsculas**:
   Para el registro de un nuevo usuario, una contraseña sin mayúsculas ni minúculas es inválida y se muestra el aviso correspondiente correctamente.

5. **Prueba de contraseña de usuario sin número ni caracteres especiales**:
   Para el registro de un nuevo usuario, una contraseña sin números ni caracteres especiales es inválida y se muestra el aviso correspondiente correctamente.

6. **Prueba de contraseña de developer sin mayúsculas ni números**:
   Para el registro de un nuevo developer, una contraseña sin mayúsculas ni número es inválida y se muestra el aviso correspondiente correctamente.

7. **Prueba de contraseña de developer sin minúsculas ni caracteres especiales**:
   Para el registro de un nuevo developer, una contraseña sin minúsculas ni caracteres especiales es inválida y se muestra el aviso correspondiente correctamente.


### Pruebas de Selenium

1. **Prueba de interfaz de validación por correo**:
   Se comprueba que la interfaz responde correctamente a un inicio de sesión y autentificación exitosas.


## Conclusión

Diseñé un sistema de validación completo, llegando a expandirlo más allá de lo inicialmente acordado, que aumenta en gran medida la seguridad de la plataforma, además de un testeo exhaustivo y proporcionado al tamaño de mi Work Item.


# José Manuel Miret Martín

## WI Asignado

Durante el período actual, me he encargado del WI "Download_all_datasets", junto con el WI añadido por el profesorado "Fakenodo". Con respecto al primer WI, me he focalizado en crear un botón en la pantalla de inicio, con el cual, tras pulsarlo, se descarga en tu dispositivo una carpeta comprimita con todos los datasets que hay en el sistema. Por otro lado, el segundo WI (Fakenodo) me he focalizado en sustituir zenodo por un módulo parecido a este, por el cual cuando hagas una llamada, no se comunique con la API, sino que te devuelve el mismo sistema un JSON. De esta forma, cuando quieras crear un nuevo dataset, tanto con como sin DOI, se pueda subir correctamente al fakenodo y no haga falta hacer peticiones a la API mediante zenodo.

## Pruebas Realizadas

He realizado un total de **1 pruebas de Selenium**, **8 pruebas de Locust** y **15 pruebas unitarias** relacionadas con la funcionalidad del sistema. A continuación, se describen los detalles de las pruebas ejecutadas:

### Pruebas de Selenium

1. **Prueba de Botón de Descarga**:  
   He probado la presencia del botón "Download All" en la página de conjuntos de datos. Se verificó que el botón está presente y correctamente ubicado en la interfaz.


### Pruebas de Locust

1. **Prueba de Conexión**:  
   Realiza una solicitud GET para verificar la conexión a la API, accediendo a la ruta "/fakenodo/api/test_connection".

2. **Prueba para crear un nuevo Dataset**:  
   Envía una solicitud POST para crear un nuevo dataset que incluya la información {"dataset_id": 1}, accediendo a la ruta "/fakenodo/api/fakenodos".

3. **Prueba para subir un archivo ya existente**:  
   Realiza una solicitud POST para subir un archivo asociado a un dataset que ya existe, por la cual envía los datos {"dataset_id": 1, "feature_model_id": 1}, accediendo a la ruta "/fakenodo/api/{fakenodo_id}/files".

4. **Prueba para modificar el estado de un dataset**:  
   Envía una solicitud PUT para cambiar el estado del dataset con ID 1 a "publicado", accediendo a la ruta "/fakenodo/api/{fakenodo_id}/publish".

5. **Prueba para obtener un dataset**:  
   Realiza una solicitud GET para obtener la información del dataset con ID 1, accediendo a la ruta "/fakenodo/api/{fakenodo_id}".

6. **Prueba para obtener el DOI**:  
   Envía una solicitud GET para obtener el identificador DOI del dataset con ID 1, accediendo a la ruta "/fakenodo/api/{fakenodo_id}/doi".

7. **Prueba para obtener todos los datasets**:  
   Envía una solicitud DELETE para eliminar el dataset con ID 1, accediendo a la ruta "/fakenodo/api/{fakenodo_id}".

8. **Prueba para obtener todos los datasets**:  
   Realiza una solicitud GET para obtener la lista de todos los datasets, accediendo a la ruta "/fakenodo/api/fakenodos".


### Pruebas Unitarias

1. **Prueba de la existencia del download all**:  
   Verifica que el endpoint /dataset/download_all existe y es accesible mediante una solicitud de tipo GET.

2. **Prueba de lo que devuelve la función download all**:  
   Verifica que el endpoint /dataset/download_all devuelve un archivo ZIP válido, el cual debe de contener todos los datasets del sistema.

3. **Intento de crear un Fakenodo con un dataset inválido**:  
   Esta prueba verifica que el servicio create_new_fakenodo maneje adecuadamente el caso en que se intente crear un dataset con una información de entrada inválida, específicamente uno que no contiene metadatos. La prueba asegura que valida correctamente los datos de entrada antes de procesarlos.

4. **Intento de obtener un Fakenodo inexistente**:  
   Este test evalúa el manejo de errores del método get_fakenodo cuando el dataset solicitado no existe en la base de datos. Asegura que el servicio lanza una excepción con un mensaje claro, validando la robustez del método ante solicitudes inválidas.

5. **Intento de obtener un DOI para un Fakenodo inexistente**:  
   Esta prueba verifica que el método get_doi gestione correctamente el caso de un dataset que no existe, lanzando una excepción con un mensaje. Esto garantiza que el servicio maneja adecuadamente las referencias a objetos no encontrados.

6. **Obtener todos los Fakenodos cuando no existen**:  
   El test asegura que el método get_all_fakenodos funcione correctamente cuando no hay datasets en el sistema. Configura el servicio con un diccionario vacío y verifica que el método devuelve una lista vacía, validando su comportamiento en escenarios iniciales o sin datos.

7. **Intento de subir un archivo a un Fakenodo inexistente**:  
   Esta prueba evalúa el manejo de errores del método upload_file cuando se intenta subir un archivo a un dataset que no existe. Asegura que se lanza una excepción con un mensaje, indicando al cliente que la operación no puede completarse debido a que el dataset no se ha podido encontrar en el sistema.

8. **Intento de publicar un Fakenodo inexistente**:  
   El test verifica que el servicio gestione correctamente un intento de publicar un dataset que no existe. Valida que el método publish_fakenodo lanza una excepción con un mensaje indicando que no se ha podido encontrar ese dataset, confirmando que el servicio valida la existencia del recurso antes de modificarlo.

9. **Intento de eliminar un Fakenodo inexistente**:  
   Esta prueba asegura que el método delete_fakenodo maneje apropiadamente el caso de intentar eliminar un fakenodo que no existe, lanzando una excepción con un mensaje indicando que no se ha podido encontrar el dataset. Valida que el servicio detecte correctamente intentos de acceso inválido.

10. **Crear un nuevo Fakenodo con datos válidos**:  
   Este test evalúa que el método create_new_fakenodo funcione correctamente cuando se le proporciona un dataset válido. Verifica que se crea un fakenodo con datos correctos, incluyendo título, descripción, etiquetas y licencia, y asegura que el resultado contiene un id y un DOI inicial como None. Si incluye DOI se debe sustituir por el suyo correspondiente en vez de None.

11. **Obtener todos los Fakenodos existentes**:  
   La prueba valida que el método get_all_fakenodos devuelve todos los datasets almacenados en el servicio. Simula dos datasets en el sistema y asegura que el método retorna una lista que incluye ambos, confirmando que la función gestiona correctamente múltiples entradas.

12. **Eliminar un Fakenodo existente**:  
   Este test verifica que el método delete_fakenodo elimina correctamente un dataset del sistema. Configura un dataset con ID 1, llama al método para eliminarlo, y asegura que el recurso ya no está presente en el sistema, retornando además un mensaje de éxito.

13. **Obtener un Fakenodo por su ID**:  
   La prueba valida que el método get_fakenodo recupere correctamente la información de un dataset existente dado su ID. Configura un dataset simulado en el servicio y asegura que los datos y el estado devueltos son los esperados.

14. **Generar un DOI para un Fakenodo sin DOI existente**:  
   Este test verifica que el método get_doi genera un DOI para un dataset que no tiene uno asignado. Simula la generación de un DOI, lo asigna al dataset correspondiente y asegura que el valor retornado y el almacenado en los datos coinciden, validando el proceso de generación de identificadores.

15. **Publicar un Fakenodo existente**:  
   La prueba asegura que el método publish_fakenodo publica correctamente un dataset existente. Verifica que el estado del dataset cambia a "published", se asigna un DOI conceptual y se retorna un mensaje de éxito. Esto valida que la publicación actualiza correctamente el recurso.


### Workflows Implementados

He implementado dos workflows para automatizar tareas en el repositorio:

1. **Workflow: Bug Report on Application Error**:  
   Este workflow funciona de la siguiente forma: cada vez que se hace `push` a la rama main, ya sea mediante un commit directo al main o mediante una pull request, este workflow primero inicializa la aplicación, y tras ello intenta acceder. En el caso de que no pueda o la aplicación de algún fallo, se creará una issue automáticamente, la cual seguirá un formato predefinido (esta base la obtiene del archivo `AUTO-ISSUE.md`, localizado en el repositorio). Tras ello, la persona responsable de haber subido esos cambios a la rama main, si lo desea, puede eliminar esa issue o completarla para notificar el fallo.

2. **Workflow: Release Automation**:  
   
   Este workflow crea una nueva tag, indicando la release actual del repositorio, por cada vez que se hacen cambios en la rama `main`, ya sea mediante un commit o mediante una pull request. La tag se actualiza en base al mensaje del commit: 
   - Si se trata de un commit de tipo `feat`, se cambia el valor major de la tag (X.0.0); 
   - Si se trata de un commit de tipo `fix`, se cambia el valor minor de la tag (0.X.0); 
   - Si se trata de un commit de tipo `test` o `refactor`, se cambia el valor pach de la tag (0.0.X).

## Conclusión

Durante este periodo, he trabajado en crear un botón para descargar todos los datasets del sistema y en crear un nuevo módulo conocido como `Fakenodo`, el cual sustituye al módulo de zenodo como he explicado anteriormente. A su vez, he creado un conjunto de pruebas para asegurar la correcta funcionalidad de las diferentes partes del sistema que he modificado/implementado. Además, implementé workflows para crear issues de forma automática cada vez hay algún fallo del sistema y crear tags para una mejor organización del proyecto en base a los commits realizados. Mi enfoque principalemnte ha sido que funcione correctamente el nuevo módulo que he implementado, a la vez que organizo los procesos internos del equipo.

# Ramón Vergara Garrido

## WI Asignado

Durante el período actual, me he encargado del WI de clase High, "Advance filtering". Mi enfoque ha estado en mejorar los filtros avanzados para la búsqueda y organización de datos en la plataforma, permitiendo a los usuarios aplicar múltiples criterios de filtrado simultáneamente.

## Pruebas Realizadas

He realizado un total de **7 pruebas unitarias** relacionadas con la funcionalidad del sistema. A continuación, se describen los detalles de las pruebas ejecutadas:

### Pruebas Unitarias

1. **Prueba de Filtro por Título**:  
   Verifiqué que el sistema filtra correctamente los datasets por título, devolviendo solo aquellos que coinciden con el título especificado.

2. **Prueba de Filtro por Tipo de Publicación**:  
   Probé que el sistema filtra correctamente los datasets por tipo de publicación, devolviendo solo aquellos que coinciden con el tipo de publicación especificado.

3. **Prueba de Filtro por Autor**:  
   Verifiqué que el sistema filtra correctamente los datasets por autor, devolviendo solo aquellos que coinciden con el autor especificado.

4. **Prueba de Filtro por Etiquetas**:  
   Probé que el sistema filtra correctamente los datasets por etiquetas, devolviendo solo aquellos que contienen las etiquetas especificadas.

5. **Prueba de Filtro por Rango de Fechas**:  
   Verifiqué que el sistema filtra correctamente los datasets por rango de fechas, devolviendo solo aquellos que fueron creados dentro del rango de fechas especificado.

6. **Prueba de Filtro por Tamaño**:  
   Probé que el sistema filtra correctamente los datasets por tamaño, devolviendo solo aquellos que están dentro del rango de tamaño especificado.

7. **Prueba de Ordenación por Fecha**:  
   Verifiqué que el sistema ordena correctamente los datasets por fecha de creación, devolviendo los datasets en el orden especificado (más nuevo a más viejo o más viejo a más nuevo).

## Conclusión

Durante este período, me he centrado en mejorar los filtros avanzados y he llevado a cabo una serie de pruebas exhaustivas para asegurar la correcta funcionalidad de diversas partes del sistema. Además, he implementado workflows para optimizar la automatización de tareas y facilitar la colaboración en el proyecto. Mi objetivo ha sido asegurar una alta calidad en la funcionalidad del sistema, al mismo tiempo que optimizo los procesos internos del equipo.


# Alejandro Nicolalde Bravo

## WI Asignado

Durante el período actual, me he encargado del WI de clase High, "Create community". Al principio cuando empecé a desarrollar la funcionalidad tuve un enfoque algo erronéo. Al principio en la aplicación se relacionaban los DataSet con los Users. Al añadir Community a la ecuación tomé un camino algo enrredoso ya que eliminé dicha relacion y conecte a los datasets con los usuarios a partir de comunidad, es decir, los datasets pertenecian a las comunidades. Despues del M1, tras hablar con mi corrector me dijo que sería mejor mantener la relación que había de User con Dataset y añadir una relacion de Community con User. Así hice y cree una relación many to many entre Community y User. Para ello, me ayude de una tabla intermedia community_members. Ya una vez aclarado lo que se quería, los usuarios podían crear, editar, unirse y eliminar comunidades. A partir de las cuales se podrán ver los datasets publicados por los miembros de dicha comunidad.
A demás, implementé al principio un atributo "público" para los datasets que le permitía al creador de los datasets cambiar la visibilidad de los datasets para que salieran en los datasets de las comunidades a las que pertenecian. Posteriormente, tras la implementación del fakenodo por parte de otro compañero, decidí cambiarlo ya que era un poco redundante y solo filtrar el mostrado de datasets de las comunidades por los dataset que hayan sido publicados(que tengan doi).

## Pruebas Realizadas

He realizado un total de **3 pruebas unitarias** y **3 pruebas de interfaz** relacionadas con la funcionalidad del sistema. A continuación, se describen los detalles de las pruebas ejecutadas:

### Pruebas Unitarias

1. **Prueba de Creación de Comunidad estando Autenticado**:  
   Verifiqué que un usuario autenticado pudiera crear crear una comunidad y se verificaba que efectivamente se había creado.

2. **Prueba de Creación de Comunidad no estando Autenticado**:  
   Probé que si un usuario sin autenticar intentaba acceder al endpoint de creacion enviando los datos para crear una comunidad no se creará y verifiqué que efectivamente no se creaba.

3. **Prueba de Borrado de Comunidad**:  
   Verifiqué que sólo el ususario el cual fuera el creador de dicha comunidad pudiera efectuar el borrado de la comunidad, verificando tanto que los usuarios de esa comunidad ya no pertenecieran a dicha comunidad y que dicha comunidad ya no constaba en la base de datos.

## Pruebas de interfaz

1. **Prueba de Creación de Comunidad**:  
   Probé que tras hacer login y la validación del código de autenticación, se puede acceder a la url de creación, se reconocen los inputs de nombre y descripción, se rellenan con datos de prueba y se pulsa el boton de submit. Al crearla que se llega al endpoint del listado de comunidades y que hay una comunidad cuyo titulo es el nombre de la comunidad.

2. **Prueba de Edición de Comunidad**:  
   Probé que tras hacer login y la validación del código de autenticación, se puede acceder a la url de edición, se reconocen los inputs de nombre y descripción, se cambian los datos existentes con datos de prueba y se pulsa el boton de submit. Al editarlo se comprueban que los contenidos de los inputs ya han cambiado.

3. **Prueba de Eliminación de Comunidad**:  
   Probé que tras hacer login y la validación del código de autenticación, se puede acceder a la url de edición(dode se encuentra el botón de borrar), se encuentra el botón de "Eliminar comunidad". Al eliminarla que se llega al endpoint del listado de comunidades y se comprueba que ya no existe una comunidad cuyo titulo es el nombre de la comunidad eliminada.


## Conclusión

Durante este período, a pesar del malentendido inicial y de la implementación del atributo "público" un tanto innecesario, he conseguido implementar las funcionalidade básicas que el WI requeria junto con la realización de pruebas tanto unitarias como de interfaz con Selenium.
