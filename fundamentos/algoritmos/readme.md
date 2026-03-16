# 📚 Algoritmos y Estructuras de Datos - Preguntas Frecuentes en Entrevistas

Este documento recopila preguntas comunes sobre **algoritmos y estructuras de datos** que suelen aparecer en entrevistas técnicas. Incluye explicaciones, ejemplos prácticos y conceptos clave para ayudarte a resolver problemas con eficiencia y claridad.

🔹 **Todas las preguntas están respondidas directamente en este archivo.**
Puedes navegar usando el índice para ir a las secciones que más te interesen.

---

## 📌 Índice

### Temario de Estructuras de Datos

1. ¿Qué es una estructura de datos?
2. ¿Qué es un array y cómo funciona?
3. ¿Qué es una pila (stack)?
4. ¿Qué es una cola (queue)?
5. ¿Qué es una lista enlazada (linked list)?
6. ¿Qué es una tabla hash?
7. ¿Qué es un árbol binario?
8. ¿Qué es un heap?
9. ¿Qué es un grafo?

### Temario de Algoritmos

1. ¿Qué es un algoritmo?
2. ¿Qué es la notación Big O y por qué es importante?
3. ¿Qué es la recursión?
4. ¿Cuál es la diferencia entre búsqueda lineal y búsqueda binaria?
5. ¿Qué es ordenamiento por burbuja (bubble sort)?
6. ¿Qué es quicksort y cómo funciona?
7. ¿Qué es el algoritmo de Dijkstra?
8. ¿Qué es el algoritmo de backtracking?
9. ¿Qué es programación dinámica?
10. ¿Qué es una búsqueda en anchura (BFS)?
11. ¿Qué es una búsqueda en profundidad (DFS)?

---

## Estructuras de Datos

### 1. ¿Qué es una estructura de datos?

Es una forma de organizar y almacenar datos para que puedan ser usados de forma eficiente. Ejemplos: arrays, listas, árboles, grafos.

---

### 2. ¿Qué es un array y cómo funciona?

Es una colección de elementos almacenados en posiciones contiguas de memoria. Permite acceso directo mediante índices.

```js
const arr = [10, 20, 30];
console.log(arr[1]); // 20
```

---

### 3. ¿Qué es una pila (stack)?

Es una estructura LIFO (Last In, First Out). El último en entrar es el primero en salir.

```js
const stack = [];
stack.push(1);
stack.push(2);
console.log(stack.pop()); // 2
```

---

### 4. ¿Qué es una cola (queue)?

Es una estructura FIFO (First In, First Out). El primero en entrar es el primero en salir.

```js
const queue = [];
queue.push(1);
queue.push(2);
console.log(queue.shift()); // 1
```

---

### 5. ¿Qué es una lista enlazada (linked list)?

Es una colección de nodos donde cada nodo apunta al siguiente. Ideal para inserciones/eliminaciones frecuentes.

```js
class Node {
  constructor(valor) {
    this.valor = valor;
    this.next = null;
  }
}
```

---

### 6. ¿Qué es una tabla hash?

Permite almacenar pares clave-valor con acceso rápido. Usa funciones hash para indexar.

```js
const mapa = new Map();
mapa.set("clave", "valor");
console.log(mapa.get("clave")); // "valor"
```

---

### 7. ¿Qué es un árbol binario?

Estructura jerárquica donde cada nodo tiene como máximo dos hijos. Base para árboles de búsqueda, heaps, etc.

---

### 8. ¿Qué es un heap?

Es un árbol binario completo que mantiene una propiedad específica: en un **max heap**, cada padre ≥ hijos.

---

### 9. ¿Qué es un grafo?

Conjunto de nodos conectados por aristas. Puede ser dirigido o no, ponderado o no.

---

## Algoritmos

### 1. ¿Qué es un algoritmo?

Es una secuencia de pasos definidos para resolver un problema. Debe ser claro, finito y ejecutable.

---

### 2. ¿Qué es la notación Big O y por qué es importante?

Describe la complejidad temporal o espacial de un algoritmo en función del tamaño de entrada.

| Notación | Descripción | Ejemplo           |
| -------- | ----------- | ----------------- |
| O(1)     | Constante   | Acceso a un array |
| O(n)     | Lineal      | Búsqueda lineal   |
| O(log n) | Logarítmica | Búsqueda binaria  |
| O(n²)    | Cuadrática  | Bubble sort       |

---

### 3. ¿Qué es la recursión?

Es cuando una función se llama a sí misma para resolver subproblemas.

```js
function factorial(n) {
  if (n === 0) return 1;
  return n * factorial(n - 1);
}
```

---

### 4. ¿Cuál es la diferencia entre búsqueda lineal y búsqueda binaria?

- **Lineal**: Recorre uno a uno los elementos (O(n)).
- **Binaria**: Divide el array ordenado a la mitad en cada paso (O(log n)).

---

### 5. ¿Qué es ordenamiento por burbuja (bubble sort)?

Algoritmo simple que compara e intercambia elementos adyacentes repetidamente.

```js
function bubbleSort(arr) {
  for (let i = 0; i < arr.length - 1; i++)
    for (let j = 0; j < arr.length - i - 1; j++)
      if (arr[j] > arr[j + 1])
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
  return arr;
}
```

---

### 6. ¿Qué es quicksort y cómo funciona?

Algoritmo de ordenamiento basado en "divide y vencerás". Usa un pivote y separa elementos menores y mayores.

---

### 7. ¿Qué es el algoritmo de Dijkstra?

Calcula el camino más corto desde un nodo a todos los demás en un grafo ponderado sin ciclos negativos.

---

### 8. ¿Qué es el algoritmo de backtracking?

Prueba soluciones recursivamente y retrocede si no cumplen. Ejemplo: Sudoku, n-reinas.

---

### 9. ¿Qué es programación dinámica?

Técnica que guarda resultados de subproblemas para no repetir cálculos. Ejemplo: Fibonacci con memoización.

---

### 10. ¿Qué es una búsqueda en anchura (BFS)?

Explora los nodos nivel por nivel. Se implementa con una cola.

---

### 11. ¿Qué es una búsqueda en profundidad (DFS)?

Explora lo más profundo posible antes de retroceder. Se implementa con una pila o recursión.

---

## 📚 Recursos Adicionales

- [Visualgo.net (visualizaciones)](https://visualgo.net/)
- [Leetcode](https://leetcode.com/)
- [GeeksforGeeks - Data Structures](https://www.geeksforgeeks.org/data-structures/)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [CS50 - Harvard](https://cs50.harvard.edu/)

🎥 **Videos recomendados**:

- [Sorting Algorithms Animation (Timo Bingmann)](https://www.youtube.com/watch?v=ZZuD6iUe3Pc)
- [Dynamic Programming - FreeCodeCamp](https://www.youtube.com/watch?v=oBt53YbR9Kk)

---

Hecho con 🧠 por [@holasoymalva](https://holasoymalva.com)
