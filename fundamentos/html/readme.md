# 🚀 HTML & CSS - Preguntas Frecuentes en Entrevistas

Este documento contiene una recopilación de preguntas comunes sobre HTML y CSS en entrevistas técnicas, con respuestas detalladas y ejemplos prácticos.

Puedes recorrerlo usando el índice y avanzar por HTML y CSS por separado.

---

## Índice

### Temario de HTML

1. ¿Qué son los atributos en HTML?
2. ¿Qué es HTML semántico? ¿Y cómo funciona?
3. ¿Qué es SVG en HTML?
4. ¿Cómo se crean páginas web anidadas en HTML?
5. ¿Cuáles son las diferencias entre las listas ordenadas y las listas desordenadas?
6. ¿Cuál es la diferencia entre elementos de línea y de bloque?
7. ¿Podrías mencionar algunos ejemplos de elementos de línea y elementos de bloque?
8. ¿Por qué generalmente es una buena idea colocar `<link>` de CSS entre `<head>` y `<script>` de JavaScript justo antes de `</body>`?
9. Describe la diferencia entre una cookie, `sessionStorage` y `localStorage`
10. ¿Qué hace un `doctype`?

### Temario de CSS

1. ¿Cuántas maneras diferentes tenemos para agregar estilos de CSS en HTML?
2. ¿Cuál consideras que es la manera adecuada de incluir estilo CSS en HTML?
3. ¿Qué es un selector en CSS?
4. ¿Cuáles son los diferentes tipos de selectores en CSS?
5. ¿Qué son Sass, Less y Stylus?
6. ¿Qué son Bootstrap, Materialize y Tailwind?
7. Explica cómo funciona el modelo de caja.
8. ¿Cuáles son las diferentes formas de ocultar un elemento de HTML usando CSS?
9. ¿Qué significa `!important` en CSS y cuáles son sus características?
10. ¿Cómo funcionan las animaciones en CSS?
11. ¿Cuál es la diferencia entre CSS Grid y Flexbox? ¿Cuándo usarías uno sobre el otro?
12. ¿Puedes dar un ejemplo de una pseudo-clase? ¿Puedes proporcionar un caso de uso para una pseudo-clase?
13. ¿Por qué se dice que CSS funciona en cascada?

---

## HTML

### 1. ¿Qué son los atributos en HTML?

Son información adicional que se pasa a las etiquetas HTML para configurar o modificar su comportamiento. Se escriben siempre dentro de la etiqueta de apertura. Por ejemplo:

```html
<img src="imagen.png" alt="Descripcion de la imagen" width="300" />
```

- `src`: ruta de la imagen.
- `alt`: texto alternativo.
- `width`: establece el ancho.

### 2. ¿Qué es HTML semántico? ¿Y cómo funciona?

HTML semántico significa usar etiquetas que describan el significado del contenido, en lugar de usar etiquetas genéricas para todo.

Ejemplos comunes:

- `<header>` para el encabezado principal.
- `<main>` para el contenido central.
- `<section>` para agrupar contenido relacionado.
- `<article>` para piezas independientes de contenido.
- `<footer>` para el pie del documento o de una sección.

Separa la estructura del diseño y facilita la accesibilidad y el SEO.

### 3. ¿Qué es SVG en HTML?

SVG (Scalable Vector Graphics) es un formato vectorial para mostrar gráficos e ilustraciones en la web. Se incrusta en HTML usando `<svg>` o la etiqueta `<img>`.

```html
<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" fill="blue" />
</svg>
```

### 4. ¿Cómo se crean páginas web anidadas en HTML?

Se pueden usar **iframes** (`<iframe>`) para anidar o incrustar otra página HTML dentro de una página principal.

```html
<iframe src="pagina-interna.html" width="600" height="400"></iframe>
```

### 5. ¿Cuáles son las diferencias entre las listas ordenadas y las listas desordenadas?

- **Lista ordenada** (`<ol>`): los elementos están numerados o siguen un orden específico.
- **Lista desordenada** (`<ul>`): los elementos usan viñetas, sin un orden numérico.

### 6. ¿Cuál es la diferencia entre elementos de línea y de bloque?

- **En línea (inline)**: se ajustan al contenido y no generan salto de línea automático. Ejemplo: `<span>`, `<a>`.
- **De bloque (block)**: ocupan todo el ancho disponible y generan un salto de línea antes y después. Ejemplo: `<div>`, `<p>`.

### 7. ¿Podrías mencionar algunos ejemplos de elementos de línea y de bloque?

- **En línea**: `<span>`, `<a>`, `<strong>`, `<em>`, `<img>`.
- **De bloque**: `<div>`, `<section>`, `<article>`, `<header>`, `<p>`, `<ul>`.

### 8. ¿Por qué generalmente es una buena idea colocar `<link>` de CSS entre `<head>` y `<script>` de JavaScript justo antes de `</body>`?

- El CSS en `<head>` asegura un renderizado inicial más estable y evita cambios bruscos de estilo al cargar la página.
- Los scripts al final evitan bloquear el parseo del HTML mientras se cargan.

**Excepción:** scripts críticos para el contenido interactivo podrían ir en `<head>`.

### 9. Describe la diferencia entre una cookie, `sessionStorage` y `localStorage`

- **Cookie**: se almacena en el navegador y se envía al servidor con cada request. Tiene fecha de expiración y menos espacio disponible.
- **sessionStorage**: solo vive durante la sesión de la pestaña. No se envía al servidor.
- **localStorage**: persiste incluso después de cerrar el navegador. No se envía al servidor.

### 10. ¿Qué hace un `doctype`?

Informa al navegador el tipo de documento y la versión de HTML a usar. En HTML5 se escribe simplemente `<!DOCTYPE html>`.

---

## CSS

### 1. ¿Cuántas maneras diferentes tenemos para agregar estilos de CSS en HTML?

1. **Estilos en línea (inline)** usando el atributo `style` en cada elemento.
2. **Estilos internos (internal)**, dentro de la etiqueta `<style>` en `<head>`.
3. **Estilos externos (external)**, mediante un archivo `.css` enlazado con `<link>`.

### 2. ¿Cuál consideras que es la manera adecuada de incluir estilo CSS en HTML?

La mejor práctica es usar un archivo CSS externo para mantener el contenido (HTML) separado de la presentación (CSS), lo que mejora la mantenibilidad y la escalabilidad.

```html
<link rel="stylesheet" href="styles.css" />
```

### 3. ¿Qué es un selector en CSS?

Un selector define a qué elementos HTML se aplicarán las reglas de estilo.

### 4. ¿Cuáles son los diferentes tipos de selectores en CSS?

- **Selector de etiqueta**: `div`, `p`, `h1`, etc.
- **Selector de clase**: `.clase`.
- **Selector de ID**: `#id`.
- **Selectores de atributo**: `input[type="text"]`.
- **Selectores de pseudo-clase**: `:hover`, `:focus`.
- **Selectores de pseudo-elemento**: `::before`, `::after`.

### 5. ¿Qué son Sass, Less y Stylus?

Son preprocesadores de CSS que añaden características como variables, mixins y funciones. Luego se compilan a CSS puro.

### 6. ¿Qué son Bootstrap, Materialize y Tailwind?

Son frameworks o librerías CSS que facilitan la creación de interfaces responsivas y consistentes con clases predefinidas.

### 7. Explica cómo funciona el modelo de caja

Cada elemento en CSS se modela como una caja con:

- **Contenido** (`width` y `height`)
- **Padding** (espacio interno entre contenido y borde)
- **Borde** (`border`)
- **Margen** (`margin`)

### 8. ¿Cuáles son las diferentes formas de ocultar un elemento de HTML usando CSS?

- `display: none;` elimina el elemento del flujo.
- `visibility: hidden;` lo oculta pero mantiene su espacio.
- `opacity: 0;` lo vuelve invisible, aunque puede seguir siendo interactuable.

### 9. ¿Qué significa `!important` en CSS y cuáles son sus características?

Fuerza a que esa regla tenga mayor prioridad que otras reglas, lo que puede dificultar el mantenimiento si se abusa de ello.

### 10. ¿Cómo funcionan las animaciones en CSS?

Se definen con la regla `@keyframes` y se aplican a un elemento con propiedades como `animation-name`, `animation-duration` y `animation-iteration-count`.

```css
@keyframes girar {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}

.elemento {
  animation: girar 2s linear infinite;
}
```

### 11. ¿Cuál es la diferencia entre CSS Grid y Flexbox? ¿Cuándo usarías uno sobre el otro?

- **Flexbox**: se enfoca en la distribución de elementos en una sola dimensión (fila o columna).
- **Grid**: permite trabajar en dos dimensiones (filas y columnas al mismo tiempo).

Usa **Flexbox** para barras de navegación o menús simples. Usa **Grid** para layouts más complejos y bidimensionales.

### 12. ¿Puedes dar un ejemplo de una pseudo-clase? ¿Puedes proporcionar un caso de uso para una pseudo-clase?

- **Pseudo-clase**: `:hover`. Cambia el estilo cuando el cursor se posa sobre un elemento.

```css
button:hover {
  background-color: blue;
  color: white;
}
```

### 13. ¿Por qué se dice que CSS funciona en cascada?

Porque las reglas se aplican en orden de prioridad y, en caso de conflicto, el último estilo declarado o el más específico anula a los anteriores.
