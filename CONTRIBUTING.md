# Guía para contribuir

## Política de commits

Todos los mensajes de commit deben seguir el siguiente formato:

### Tipos permitidos:
- **feat**: Añadir una nueva funcionalidad.
- **fix**: Corregir un error.
- **docs**: Cambiar documentación.
- **style**: Cambios de formato (sin afectar la lógica).
- **refactor**: Refactorización del código.
- **test**: Añadir o corregir pruebas.
- **chore**: Actualizaciones menores y tareas rutinarias.

**Ejemplo:**
```plaintext
feat(auth): añadir autenticación con Google
```

## Flujo de trabajo (Workflow):

### Ramas principales:
- **`main`:** Contiene el código listo para producción.

### Ramas de funcionalidad:
- **`feature/`**:
  - Cada Work Item (WI) tiene su propia rama.
  - **Nomenclatura:** `feature/<nombre_WI>`.
    - **Ejemplo:** `feature/improveUI`.
  - Las ramas se eliminan tras fusionarse en la rama `main`.

## Pull Requests (PR):
- Un PR debe incluir una descripción clara de los cambios realizados.
- Indicar el issue relacionado.
- Todo PR debe ser aprobado por al menos un revisor antes de ser fusionado.

## Issues

### Creación de issues:
Cada Work Item debe dividirse en al menos dos issues:
- Una issue para implementar la funcionalidad requerida.
- Otra issue para desarrollar las pruebas relacionadas.

### Categorías:
- **bug**: Indica un problema o error en el sistema que necesita ser corregido.
- **enhancement**: Representa una mejora o nueva funcionalidad que se desea agregar al sistema.
- **test**: Corresponde a *Work Items* relacionados con la creación o mejora de pruebas automatizadas.

### Complejidad:
- **low**: Tareas de baja complejidad. Recomendadas para nuevos contribuidores o tareas rápidas.
- **medium**: Tareas de complejidad intermedia. Suelen requerir conocimientos moderados sobre el sistema.
- **high**: Tareas de alta complejidad. Requieren conocimientos avanzados y pueden involucrar múltiples componentes del sistema.
