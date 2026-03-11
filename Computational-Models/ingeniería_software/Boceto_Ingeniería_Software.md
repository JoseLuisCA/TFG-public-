# Boceto Simple de Ingenieria del Software (AutoSandbox)

## 1. Que es la app
AutoSandbox es una aplicacion de escritorio para crear y probar automatas de forma visual.

## 2. Objetivo
Construir una app sencilla que permita:
- crear estados y transiciones,
- simular cadenas,
- aplicar operaciones basicas de automatas,
- guardar y cargar archivos.

## 3. Alcance (MVP)
Incluye:
- Pantalla principal.
- Vista de automata finito con barra de herramientas.
- Crear estado (circulo) en el lienzo.
- Mover estados con el raton.
- Boton Back para volver al inicio.

No incluye (por ahora):
- IA / lenguaje natural.
- Ejercicios autoevaluables.
- Funcionalidades avanzadas de edicion.

## 4. Actores
- Estudiante: usa la app para practicar.
- Docente: usa la app para explicar ejemplos.

## 5. Requisitos funcionales minimos
- RF1: Abrir la app y navegar entre pantallas.
- RF2: Entrar a la vista de automata finito.
- RF3: Arrastrar la herramienta circulo al lienzo.
- RF4: Dejar el estado en una posicion y moverlo despues.
- RF5: Volver al inicio con Back.

## 6. Requisitos no funcionales minimos
- RNF1: Interfaz clara y facil de usar.
- RNF2: Tiempo de respuesta inmediato en acciones basicas.
- RNF3: Estabilidad sin errores al crear/mover estados.

## 7. Casos de uso basicos
- CU1: Entrar en "Finite Automaton".
- CU2: Crear un estado en el lienzo.
- CU3: Mover un estado existente.
- CU4: Volver al menu principal.

## 8. Arquitectura simple
- Capa visual (PySide6): ventanas, botones, lienzo.
- Capa logica: operaciones de automatas existentes del proyecto.
- Capa datos: lectura/escritura de archivos de automatas.

## 9. Plan corto de trabajo
- Fase 1: Navegacion y estructura de pantallas.
- Fase 2: Herramientas visuales basicas (circulo, mover).
- Fase 3: Simulacion y operaciones basicas.
- Fase 4: Pruebas y pulido final.

## 10. Criterio de exito
La app se considera valida si permite un flujo completo:
- abrir app,
- entrar en automata finito,
- crear y mover estados,
- volver al inicio,
- y ejecutar sin errores.
