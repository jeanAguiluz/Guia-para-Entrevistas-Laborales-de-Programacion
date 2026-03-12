# 🚀 HTML & CSS - Preguntas Frecuentes en Entrevistas  

Este documento contiene una recopilación de preguntas comunes sobre HTML y CSS en entrevistas técnicas, con respuestas detalladas y ejemplos prácticos.


🔹 **Cada pregunta está explicada en detalle en este mismo archivo.**  
Puedes desplazarte hasta la sección correspondiente haciendo clic en el índice. 🚀

---

## Índice

### Temario de HTML

1. ¿Qué son los atributos en HTML?
2. ¿Qué es HTML semántico? ¿Y cómo funciona?
3. ¿Qué es SVG en HTML?
4. ¿Cómo se crean páginas web anidadas en HTML?
5. ¿Cuáles son las diferencias entre las lista ordenadas y las lista desordenadas?
6. ¿Cuál es la diferencia entre elementos de línea y de bloque?
7. ¿Podrías mencionar algunos ejemplos de elementos de línea y elementos de bloque?
8. ¿Por qué generalmente es una buena idea colocar `<link>` de CSS entre `<head></head>` y `<script>` de JavaScript justo antes de `</body>`? ¿Conoces alguna excepción?
9. Describe la diferencia entre una cookie, `sessionStorage` y `localStorage`.
10. ¿Qué hace un `doctype`?

### Temario de CSS

11. ¿Cuántas maneras diferentes tenemos para agregar estilos de CSS en HTML?
12. ¿Cuál consideras es la manera adecuada de incluir estilo CSS en HTML?
13. ¿Qué es un Selector en CSS?
14. ¿Cuáles son los diferentes tipos de Selectores en CSS?
15. ¿Qué son Sass, Less y Stylus?
16. ¿Qué son Bootstrap, Materialize y Tailwind?
17. Explica cómo funciona el modelo de caja
18. ¿Cuáles son las diferentes formas de ocultar un Elemento de HTML usando CSS?
19. ¿Qué significa `!important` en CSS y cuáles son sus características?
20. ¿Cómo funcionan las animaciones en CSS?
21. ¿Cuál es la diferencia entre CSS Grid y Flexbox? ¿Cuándo usarías uno sobre el otro?
22. ¿Puedes dar un ejemplo de una pseudo-clase? ¿Puedes proporcionar un caso de uso de ejemplo para una pseudo-clase?
23. ¿Por qué se dice que CSS funciona en cascada?

---

## HTML

### 1. ¿Qué son los atributos en HTML?

Son información adicional que se pasa a las etiquetas HTML para configurar o modificar su comportamiento. Se escriben siempre dentro de la etiqueta de apertura. Por ejemplo:

```html
<img src="imagen.png" alt="Descripción de la imagen" width="300"/>
```
- `src`: ruta de la imagen.
- `alt`: texto alternativo.
- `width`: establece el ancho.

### 2. ¿Qué es HTML semántico? ¿Y cómo funciona?

HTML semántico significa usar etiquetas que describan el significado del contenido, en lugar de usar etiquetas genéricas para todo. Ejemplos:
- `<header>`, `<footer>`, `<main>`, `<section>`, `<article>`

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

### 5. ¿Cuáles son las diferencias entre las lista ordenadas y las lista desordenadas?

- **Lista ordenada** (`<ol>`): los elementos están numerados o con un orden específico.
- **Lista desordenada** (`<ul>`): los elementos usan viñetas o puntos, sin un orden numérico.

### 6. ¿Cuál es la diferencia entre elementos de línea y de bloque?

- **En línea (inline)**: Se ajustan al contenido, no generan salto de línea automático. Ej: `<span>`, `<a>`.
- **De bloque (block)**: Ocupan todo el ancho disponible y generan un salto de línea antes y después. Ej: `<div>`, `<p>`.

### 7. ¿Podrías mencionar algunos ejemplos de elementos de línea y elementos de bloque?

- **En línea**: `<span>`, `<a>`, `<strong>`, `<em>`, `<img>`.
- **De bloque**: `<div>`, `<section>`, `<article>`, `<header>`, `<p>`, `<ul>`.

### 8. ¿Por qué generalmente es una buena idea colocar `<link>` de CSS entre `<head>` y `<script>` de JavaScript justo antes de `</body>`?

- El CSS en `<head>` asegura un rápido renderizado inicial (evita el efecto de "página en blanco" o reestructuración tardía).
- Los scripts al final evitan bloquear el parseo del HTML mientras se cargan.

**Excepción**: Scripts críticos para el contenido interactivo podrían ir en `<head>`.

### 9. Describe la diferencia entre una cookie, `sessionStorage` y `localStorage`.

- **Cookie**: Se almacena en el navegador y se envía al servidor con cada request. Tiene fecha de expiración. Menos espacio de almacenamiento.
- **sessionStorage**: Solo disponible durante la sesión de la pestaña (se borra al cerrar la pestaña). No se envía al servidor.
- **localStorage**: Persiste incluso cerrando el navegador. No se envía al servidor.

### 10. ¿Qué hace un `doctype`?

Informa al navegador el tipo de documento y la versión de HTML a usar. En HTML5 se escribe simplemente `<!DOCTYPE html>`.

---

## CSS

### 11. ¿Cuántas maneras diferentes tenemos para agregar estilos de CSS en HTML?

1. **Estilos en línea (inline)** usando el atributo `style` en cada elemento.
2. **Estilos internos (internal)**, dentro de la etiqueta `<style>` en `<head>`.
3. **Estilos externos (external)**, mediante un archivo `.css` enlazado con `<link>`.

### 12. ¿Cuál consideras es la manera adecuada de incluir estilo CSS en HTML?

La mejor práctica es usar un archivo CSS externo para mantener el contenido (HTML) separado de la presentación (CSS), lo que mejora la mantenibilidad y la escalabilidad.

```html
<link rel="stylesheet" href="styles.css">
```

### 13. ¿Qué es un Selector en CSS?

Un selector define a qué elementos HTML se aplicarán las reglas de estilo.

### 14. ¿Cuáles son los diferentes tipos de Selectores en CSS?

- **Selector de etiqueta**: `div`, `p`, `h1`, etc.
- **Selector de clase**: `.clase`.
- **Selector de id**: `#id`.
- **Selectores de atributo**: `input[type="text"]`.
- **Selectores de pseudo-clase**: `:hover`, `:focus`.
- **Selectores de pseudo-elemento**: `::before`, `::after`.

### 15. ¿Qué son Sass, Less y Stylus?

Son preprocesadores de CSS que añaden características como variables, mixins y funciones. Luego se compilan a CSS puro.

### 16. ¿Qué son Bootstrap, Materialize y Tailwind?

Son frameworks/librerías CSS que facilitan la creación de interfaces responsivas y estéticas con clases predefinidas.

### 17. Explica cómo funciona el modelo de caja

Cada elemento en CSS se modela como una caja con:
- **Contenido** (width y height)
- **Padding** (espacio interno entre contenido y borde)
- **Borde (border)**
- **Margen (margin)**

### 18. ¿Cuáles son las diferentes formas de ocultar un Elemento de HTML usando CSS?

- `display: none;` (remueve el elemento del flujo)
- `visibility: hidden;` (oculta pero mantiene el espacio)
- `opacity: 0;` (invisible pero interactuable)

### 19. ¿Qué significa `!important` en CSS y cuáles son sus características?

Fuerza a que esa regla tenga mayor prioridad que otras reglas (incluyendo inline styles), lo que puede dificultar el mantenimiento si se abusa de ello.

### 20. ¿Cómo funcionan las animaciones en CSS?

Se definen con la regla `@keyframes` y se aplican a un elemento con propiedades como `animation-name`, `animation-duration`, `animation-iteration-count`, etc.

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

### 21. ¿Cuál es la diferencia entre CSS Grid y Flexbox? ¿Cuándo usarías uno sobre el otro?

- **Flexbox**: se enfoca en la distribución de elementos en una sola dimensión (fila o columna).
- **Grid**: permite trabajar en dos dimensiones (filas y columnas al mismo tiempo).

Usar **Flexbox** para barras de navegación, menús simples. Usar **Grid** para diseños más complejos y bidimensionales.

### 22. ¿Puedes dar un ejemplo de una pseudo-clase? ¿Puedes proporcionar un caso de uso de ejemplo para una pseudo-clase?

- **Pseudo-clase**: `:hover`. Cambia el estilo cuando el cursor se posa sobre un elemento.

```css
button:hover {
  background-color: blue;
  color: white;
}
```

### 23. ¿Por qué se dice que CSS funciona en cascada?

Porque las reglas se aplican en orden de prioridad (heredando estilos de sus padres) y, en caso de conflicto, el último estilo declarado (o el más específico) anula los anteriores.

---
