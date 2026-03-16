# 📖 Guía para Entrevistas Laborales de Programación

![readme-title](./readme-assets/entrevista.png)

Este repositorio es un recurso abierto para ayudarte a prepararte para entrevistas técnicas de programación. Aquí encontrarás teoría, ejemplos de código, pruebas técnicas, desafíos prácticos y simulacros de entrevistas.

**Objetivo:** brindar una guía completa con preguntas comunes, resolución de problemas y simulacros para mejorar tus habilidades.

## Índice

1. Fundamentos
2. Stacks tecnológicos
3. Pruebas técnicas
4. Simulacros de entrevistas
5. Cómo contribuir

---

## Fundamentos

Esta sección cubre conceptos esenciales de programación y herramientas clave. Cada tema contiene preguntas frecuentes, ejemplos de código y recursos adicionales.

- **Git**: [Preguntas frecuentes](fundamentos/git/readme.md)
- **HTML y CSS**: [Preguntas frecuentes](fundamentos/html/readme.md)
- **JavaScript**: [Preguntas frecuentes](fundamentos/javascript/readme.md)
- **POO (Programación Orientada a Objetos)**: [Preguntas frecuentes](fundamentos/poo/readme.md)
- **Algoritmos y estructuras de datos**: [Preguntas frecuentes](fundamentos/algoritmos/readme.md)
- **Diseño de sistemas**: [Preguntas frecuentes](fundamentos/systems-design/readme.md)

---

## Stacks tecnológicos

Exploramos preguntas y desafíos específicos para distintos stacks.

- **Node.js**: [Preguntas frecuentes](stacks/node/readme.md)
- **React**: [Preguntas frecuentes](stacks/react/readme.md) _(En desarrollo)_

Cada stack reúne preguntas técnicas y ejercicios aplicados a entrevistas reales.

---

## Pruebas técnicas

La clave para superar entrevistas técnicas es la práctica constante. Aquí encontrarás desafíos y ejercicios para entrenar lógica, diseño y UI.

- **Lógica, algoritmos y estructuras de datos**: [Ejercicios](pruebas-tecnicas/desafios/logica/readme.md) _(En desarrollo)_
- **Diseño de sistemas**: [Ejercicios](pruebas-tecnicas/desafios/systems-design/readme.md) _(En desarrollo)_
- **Desarrollo frontend UI**: [Ejercicios](pruebas-tecnicas/desafios/frontend-ui/readme.md) _(En desarrollo)_

### Ejemplo de desafío

```js
// Dado un string, encuentra la subcadena más larga sin caracteres repetidos
const longestSubstring = (s) => {
  let seen = new Set();
  let maxLen = 0;
  let left = 0;

  for (let right = 0; right < s.length; right++) {
    while (seen.has(s[right])) {
      seen.delete(s[left]);
      left++;
    }

    seen.add(s[right]);
    maxLen = Math.max(maxLen, right - left + 1);
  }

  return maxLen;
};

console.log(longestSubstring("abcabcbb")); // Output: 3
```

---

## Simulacros de entrevistas

Pon a prueba tus habilidades con entrevistas simuladas y escenarios reales.

1. Entrevistas de algoritmos y lógica
2. Entrevistas de código en varios lenguajes
3. Casos prácticos de desarrollo

---

## Cómo contribuir

Si deseas contribuir, sigue estos pasos:

1. Clona el repositorio.

   ```sh
   git clone https://github.com/holasoymalva/Guia-para-Entrevistas-Laborales-de-Programacion.git
   ```

2. Crea una nueva rama.

   ```sh
   git checkout -b mi-contribucion
   ```

3. Realiza tus cambios y sube tus mejoras.
4. Abre un Pull Request.

Gracias por tu apoyo.

---

Hecho con ❤️ por [@holasoymalva](https://holasoymalva.com)
