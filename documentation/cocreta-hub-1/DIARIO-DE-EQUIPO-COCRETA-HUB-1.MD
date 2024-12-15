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
        - **Sign up Validation** *(Asignada a Toro Romero, Raúl)*: Se trata de implementar un sistema de validación de correo electrónico que requerirá que los usuarios verifiquen su dirección de correo tanto al registrarse como al iniciar sesión. Este sistema enviará un código de verificación al correo electrónico proporcionado, que los usuarios deberán ingresar en la plataforma para completar el proceso de registro o acceso.


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