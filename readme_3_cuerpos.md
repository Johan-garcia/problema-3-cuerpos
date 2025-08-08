# Simulación del Problema de los 3 Cuerpos
### johan garcia
### joya
### santiago

Este proyecto implementa una simulación interactiva del famoso **problema de los 3 cuerpos** en mecánica celestial, utilizando Python y visualización en tiempo real.

##  Descripción

El problema de los 3 cuerpos es un problema clásico de la mecánica celestial que estudia el movimiento de tres objetos masivos bajo la influencia de su mutua atracción gravitacional. A diferencia del problema de 2 cuerpos (que tiene solución analítica), el problema de 3 cuerpos es caótico y requiere métodos numéricos para su resolución.

##  Física y Matemáticas Implementadas

### Ley de Gravitación Universal de Newton

La fuerza gravitacional entre dos cuerpos está dada por:

```
F = G * (m₁ * m₂) / r²
```

Donde:
- `F` = Magnitud de la fuerza gravitacional
- `G` = Constante gravitacional (simplificada a 1.0 en la simulación)
- `m₁, m₂` = Masas de los dos cuerpos
- `r` = Distancia entre los centros de los cuerpos

### Componentes de la Fuerza

Para obtener las componentes vectoriales de la fuerza:

```
Fx = F * (Δx / r)
Fy = F * (Δy / r)
```

Donde:
- `Δx = x₂ - x₁` (diferencia en coordenada x)
- `Δy = y₂ - y₁` (diferencia en coordenada y)
- `r = √(Δx² + Δy²)` (distancia euclidiana)

### Segunda Ley de Newton

La aceleración de cada cuerpo se calcula mediante:

```
a = F_neta / m
```

### Integración Numérica (Método de Euler)

La simulación utiliza el método de Euler para integrar las ecuaciones de movimiento:

```
v(t + Δt) = v(t) + a(t) * Δt
x(t + Δt) = x(t) + v(t) * Δt
```

##  Características

- **Simulación en tiempo real**: Visualización animada del movimiento orbital
- **Trazado de órbitas**: Muestra las trayectorias históricas de cada cuerpo
- **Colores diferenciados**: Cada planeta tiene su propio color para fácil identificación
- **Física realista**: Implementación precisa de las leyes de Newton y gravitación

##  Requisitos

### Dependencias de Python

```bash
matplotlib>=3.5.0
```

##  Instalación y Ejecución

### En Linux (Ubuntu/Debian)

1. **Instalar Python y pip** (si no están instalados):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

2. **Instalar matplotlib**:
```bash
pip3 install matplotlib
```

3. **Ejecutar la simulación**:
```bash
python3 3-Cuerpos.py
```

### En Linux (CentOS/RHEL/Fedora)

1. **Instalar Python y pip**:
```bash
# Para CentOS/RHEL
sudo yum install python3 python3-pip

# Para Fedora
sudo dnf install python3 python3-pip
```

2. **Instalar matplotlib**:
```bash
pip3 install matplotlib
```

3. **Ejecutar la simulación**:
```bash
python3 3-Cuerpos.py
```

### En Windows

#### Opción 1: Usando Python desde python.org

1. **Descargar e instalar Python**:
   - Ir a https://python.org/downloads/
   - Descargar la versión más reciente de Python 3
   - Durante la instalación, asegúrate de marcar "Add Python to PATH"

2. **Instalar matplotlib** (usar Command Prompt o PowerShell):
```cmd
pip install matplotlib
```

3. **Ejecutar la simulación**:
```cmd
python 3-Cuerpos.py
```

#### Opción 2: Usando Anaconda (Recomendado)

1. **Instalar Anaconda**:
   - Descargar desde https://www.anaconda.com/products/distribution
   - Seguir las instrucciones de instalación

2. **Abrir Anaconda Prompt y ejecutar**:
```cmd
conda install matplotlib
python 3-Cuerpos.py
```

## Configuración del Sistema

### Configuración Inicial por Defecto

El código viene preconfigurado con tres planetas:

- **Planeta A** (Rojo): Posición (0, 0), velocidad inicial (1, 0)
- **Planeta B** (Verde): Posición (2, 0), velocidad inicial (0, 1)  
- **Planeta C** (Azul): Posición (0, 2), velocidad inicial (-1, 0)

### Personalización

Puedes modificar los parámetros iniciales cambiando estas líneas en el código:

```python
planeta_A = Planeta(x, y, radio, 'color', masa, vx, vy)
```

Donde:
- `x, y`: Posición inicial
- `radio`: Tamaño visual (0.1 recomendado)
- `'color'`: Color del planeta ('red', 'green', 'blue', etc.)
- `masa`: Masa del planeta (afecta la gravitación)
- `vx, vy`: Velocidad inicial en x e y

##  Controles

- **Cerrar ventana**: Detiene la simulación
- La simulación corre automáticamente al ejecutar el script
- No hay controles interactivos durante la ejecución

## Parámetros Ajustables

### Paso de Tiempo (dt)
```python
dt = 0.02  # Valor más pequeño = mayor precisión, simulación más lenta
```

### Constante Gravitacional
```python
G = 1.0  # Aumentar = fuerzas gravitacionales más fuertes
```

### Velocidad de Animación
```python
animacion = FuncAnimation(fig, animar, interval=0)  # interval=0 = velocidad máxima
```

Este proyecto es de código abierto y puede ser usado con fines educativos y de investigación.

---

*Desarrollado como herramienta educativa para el estudio de la mecánica celestial y sistemas dinámicos.*
