# Proyecto de Diseño y Análisis de Algoritmos

## Integrantes:

- Amanda Cordero Lezcano
- Christopher Guerra Herrero

## Descripción del Problema

En una finca agrícola, se deben realizar varias actividades diarias que compiten por el recurso limitado de los **trabajadores disponibles**. Las actividades incluyen:

1. **Cortar hierba**
2. **Alimentar conejos**.
3. **Cercar áreas**, lo cual requiere abrir agujeros en el suelo y asegurar los cercos.
4. **Encender el pozo para regar cultivos**, necesario para garantizar la productividad.
5. Avanzar en la plantación de cultivos según ***la rotación de cultivos*** planificada.

### Restricciones Operativas

- Se dispone de **10 trabajadores** como recurso limitado.
- Cada actividad requiere un número específico de trabajadores y una duración mínima para completarse.
- Algunas actividades tienen **precedencias**:
  - La actividad de riego solo puede realizarse si el pozo ha sido encendido.
- El objetivo es **maximizar la productividad diaria** mediante un uso eficiente de los trabajadores y respetando las restricciones de tiempo y precedencia.

## **Rotación de Cultivos**

### **Objetivo**

El problema consiste en encontrar una secuencia de plantación que maximice el beneficio del suelo a largo plazo, minimizando las enfermedades y maximizando el aprovechamiento de los recursos teniendo en cuenta que:

1. El suelo tiene un nivel de enfermedad y un nivel de beneficio.
2. Cada cultivo afecta estos niveles al aportar cierto grado de beneficio y al aumentar o reducir las enfermedades del suelo.
3. El beneficio del suelo es inversamente proporcional a su nivel de enfermedad.
4. Cada uno de estos cultivos tiene un nivel de prioridad que influye en cuán prioritario es avanzar en la plantación de cultivos en la planificación de actividades de la finca.

## Modelacion de Problemas:

### Problema de Planificación de tareas
se modela como un **Problema de Programación de Proyectos con Recursos Limitados** (*Resource-Constrained Project Scheduling Problem*, RCPSP) que es un problema ampliamente estudiado en la investigación operativa. Su objetivo es programar actividades en un proyecto respetando restricciones de recursos y precedencias, mientras se optimiza algún criterio (como la duración total o los costos). Este problema pertenece a la clase de problemas **NP-duros**.

Se modela la finca como un proyecto en el cual se deben realizar las actividades antes descritas sujeto a las restricciones operativas.

### Problema de Rotación de Cultivos

#### **1. Estado del Suelo**
- $ S_t $: Nivel de beneficio del suelo en el tiempo $ t $.

- $ E_t $: Nivel de enfermedad del suelo en el tiempo $ t $.

#### **2. Cultivo Sembrado**

- $ C_t \in \{C_1, C_2, \dots, C_n\} $: Cultivo seleccionado en el tiempo $ t $, donde $ C_i $ representa una posible opción de cultivo.

#### **Efectos de los Cultivos**

Cada cultivo $ C_i $ tiene dos efectos sobre el suelo:

1. **Beneficio aportado ($ B(C_i) $)**: Incremento directo al nivel de beneficio del suelo.
2. **Impacto sobre la enfermedad ($ \Delta E(C_i) $)**: Incremento o reducción en el nivel de enfermedad.

Por lo tanto:
- Después de sembrar $ C_t $:

  $$
  S_{t+1} = S_t + B(C_t) - \lambda E_{t+1}
  $$
  $$
  E_{t+1} = E_t + \Delta E(C_t)
  $$
  
- 

  \- Donde $lambda > 0 $  es un factor que mide cuánto afecta el nivel de enfermedad al beneficio del suelo.

