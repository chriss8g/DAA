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
- El objetivo es **maximizar la productividad diaria** mediante un uso eficiente de los trabajadores.

## **Rotación de Cultivos**

### **Objetivo**

Encontrar una secuencia de cultivos que maximice el beneficio del suelo a lo largo de un período de tiempo determinado, teniendo en cuenta que:

1. El suelo tiene un nivel de enfermedad y un nivel de beneficio.
2. Cada cultivo afecta estos niveles al aportar cierto grado de beneficio y al aumentar o reducir las enfermedades del suelo.
3. El beneficio del suelo es inversamente proporcional a su nivel de enfermedad.
4. Cada uno de estos cultivos tiene un nivel de prioridad que influye en cuán prioritario es avanzar en la plantación de cultivos en la planificación de actividades de la finca.
