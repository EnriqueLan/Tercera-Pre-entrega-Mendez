# Centro de Adopción de Mascotas

Este proyecto es una aplicación web desarrollada con Django que permite gestionar un centro de adopción de mascotas. Puedes agregar perros y gatos, adoptar una mascota y buscar mascotas en la base de datos.

## Uso de la Aplicación

### 1. Página de Inicio

La página de inicio (`/CentroAdopcion/`) muestra un mensaje de bienvenida y enlaces de navegación a las diferentes secciones de la aplicación.

### 2. Agregar un Perro

1. Haz clic en "Agregar Perro" en la barra de navegación o ve a `/CentroAdopcion/agregar_perro/`.
2. Rellena el formulario con los datos del perro: Nombre, Raza, Género y su Edad la cual debes especificar si son años o meses.
3. Haz clic en "Agregar".

Esto guardará la información del perro en la base de datos y te redirigirá a la página de inicio.

### 3. Agregar un Gato

1. Haz clic en "Agregar Gato" en la barra de navegación o ve a `/CentroAdopcion/agregar_gato/`.
2. Rellena el formulario con los datos del gato: Nombre, Raza, Género y su Edad la cual debes especificar si son años o meses.
3. Haz clic en "Agregar".

Esto guardará la información del gato en la base de datos y te redirigirá a la página de inicio.

### 4. Listar Perros

1. Haz clic en "Listar Perros" en la barra de navegación o Ve a `/CentroAdopcion/lista_perros/` para ver una lista de todos los perros disponibles en la base de datos.

### 5. Listar Gatos

1. Haz clic en "Listar Gatos" en la barra de navegación o Ve a `/CentroAdopcion/lista_gatos/` para ver una lista de todos los gatos disponibles en la base de datos.

### 6. Buscar una Mascota

1. Haz clic en "Buscar Mascota" en la barra de navegación o ve a `/CentroAdopcion/buscar_mascota/`.
2. Selecciona la especie (Perro o Gato) e ingresa el nombre de la mascota que deseas buscar.
3. Haz clic en "Buscar".

Esto te mostrará la mascota que estás buscando ademas de darte otros datos que no te dan las listas de la pagina.

### 7. Adoptar una Mascota

1. Haz clic en "Adoptar Mascota" en la barra de navegación o ve a `/CentroAdopcion/adoptar_mascota/`.
2. Rellena el formulario con tus datos y los de la mascota que deseas adoptar: Nombre, Apellido, Dirección, Número de Teléfono, Nombre de la Mascota y Especie de la Mascota (Ya sea un perro o un gato).
3. Haz clic en "Adoptar".

Esto guardará la información de la adopción en la base de datos y te redirigirá a la página de inicio.

¡¡¡Dato importante!!!
Para la proxima actualizacion de esta aplicacion cada usuario va a poder ver que mascota adoptó y en las listas de perros o gatos de la pagina al costado del Nombre y de la Raza de la mascota habrá un mensaje que diga si ese animal está disponible o si está en proceso de adopcion.(Con proceso de adopcion me refiero a que la mascota podría a llegar a estar nuevamente disponible si el usuario que la adoptó primero decidió cancelar la adopcion pero para eso necesito crear los usuarios y un crud para todo este proceso)


## Fin del README

Este README proporciona las instrucciones necesarias para que cualquier usuario pueda utilizar la aplicación web del Centro de Adopción de Mascotas y entender el flujo de navegación para agregar, buscar y adoptar mascotas.
