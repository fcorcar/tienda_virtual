
# Manual de Usuario

## Introducción

Este sistema está diseñado para facilitar la gestión de productos y usuarios mediante una interfaz de consola. Permite registrar usuarios, iniciar sesión, y realizar operaciones CRUD sobre productos, como añadir, listar, buscar, modificar y eliminar productos.

## Instrucciones de uso paso a paso

### 1. Registro de usuario

Al ejecutar el programa, el sistema pregunta si desea registrarse. Ingrese 'S' para proceder al registro. Introduzca su nombre, correo electrónico, y una contraseña segura.

### 2. Iniciar sesión

Si ya está registrado, elija 'N' cuando se le pregunte por el registro. Ingrese su correo y contraseña para iniciar sesión.

### 3. Menú principal

Una vez dentro, verá un menú con las siguientes opciones:
- `1. Agregar producto`: Ingrese los detalles del producto para añadirlo.
- `2. Listar productos`: Muestra todos los productos registrados.
- `3. Buscar producto`: Permite buscar productos por nombre o código.
- `4. Modificar producto`: Modifica los datos de un producto existente.
- `5. Eliminar producto`: Elimina un producto del sistema.
- `6. Salir`: Cierra la sesión actual.

### 4. Cierre de sesión

Seleccione la opción 6 en el menú principal para salir del sistema de forma segura.

## Casos de uso

### Caso de uso 1: Registro y autenticación

**Actor**: Usuario nuevo  
**Escenario**:
1. El usuario ejecuta el programa.
2. Decide registrarse.
3. Ingresa su información.
4. Recibe confirmación de registro.

### Caso de uso 2: Gestión de productos

**Actor**: Usuario autenticado  
**Escenario**:
1. Accede al sistema mediante inicio de sesión.
2. Elige una opción del menú (Agregar, Listar, Buscar, Modificar, Eliminar).
3. Realiza la acción correspondiente.
4. El sistema responde con éxito o error.

### Caso de uso 3: Salida del sistema

**Actor**: Usuario autenticado  
**Escenario**:
1. Elige la opción 6 del menú.
2. El sistema termina la sesión y cierra el programa.

---

Este manual está diseñado para usuarios finales que desean interactuar con el sistema sin necesidad de conocimientos técnicos.
