# Importación de bibliotecas necesarias
import math  # Para funciones matemáticas como sqrt
import matplotlib.pyplot as plt  # Para visualización de gráficos
from matplotlib.animation import FuncAnimation  # Para crear animaciones

class Planeta:
    """
    Clase que representa un cuerpo celeste con propiedades físicas y visuales.
    """
    def __init__(self, x, y, radio, color, masa, vx=0, vy=0):
        """
        Inicializa un planeta con su posición, características y velocidad.
        
        Parámetros:
        x, y: Coordenadas iniciales
        radio: Tamaño visual del planeta
        color: Color para representación gráfica
        masa: Masa del planeta para cálculos gravitacionales
        vx, vy: Componentes de velocidad inicial (por defecto 0)
        """
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.masa = masa
        self.vx = vx  # Velocidad en el eje X
        self.vy = vy  # Velocidad en el eje Y
        self.orbita = [(x, y)]  # Lista para almacenar el historial de posiciones

def update_position(planeta, dt):
    """
    Actualiza la posición del planeta según su velocidad actual.
    
    Parámetros:
    planeta: Objeto de la clase Planeta
    dt: Incremento de tiempo
    """
    planeta.x += planeta.vx * dt
    planeta.y += planeta.vy * dt

def actualizar_velocidad(planeta, fuerza, dt):
    """
    Actualiza la velocidad del planeta según la fuerza neta aplicada.
    Implementa la segunda ley de Newton: a = F/m
    
    Parámetros:
    planeta: Objeto de la clase Planeta
    fuerza: Tupla con componentes (fx, fy) de la fuerza
    dt: Incremento de tiempo
    """
    ax = fuerza[0] / planeta.masa  # Aceleración en X (F = m·a)
    ay = fuerza[1] / planeta.masa  # Aceleración en Y
    planeta.vx += ax * dt  # Incremento de velocidad en X
    planeta.vy += ay * dt  # Incremento de velocidad en Y

def fuerza_gravitacional(planeta1, planeta2):
    """
    Calcula la fuerza gravitacional entre dos planetas según la ley de gravitación de Newton.
    
    Parámetros:
    planeta1, planeta2: Objetos de la clase Planeta
    
    Retorna:
    Tupla con las componentes (fx, fy) de la fuerza ejercida sobre planeta1
    """
    G = 1.0  # Constante gravitacional simplificada
    
    # Cálculo de la distancia entre los planetas
    dx = planeta2.x - planeta1.x
    dy = planeta2.y - planeta1.y
    distancia_cuadrada = dx**2 + dy**2
    distancia = math.sqrt(distancia_cuadrada)
    
    # Ley de gravitación: F = G * m1 * m2 / r²
    magnitud_fuerza = G * planeta1.masa * planeta2.masa / distancia_cuadrada
    
    # Componentes de la fuerza en cada eje
    fuerza_x = magnitud_fuerza * dx / distancia
    fuerza_y = magnitud_fuerza * dy / distancia
    
    return (fuerza_x, fuerza_y)

def simular(planetas, dt):
    """
    Avanza la simulación un paso de tiempo para todos los planetas.
    
    Parámetros:
    planetas: Lista de objetos Planeta
    dt: Incremento de tiempo
    """
    # Primero calculamos todas las fuerzas
    for planeta in planetas:
        fuerza_neta = [0, 0]  # Inicializa la fuerza neta
        for other_planeta in planetas:
            if planeta != other_planeta:  # No calcular fuerza con uno mismo
                fuerza = fuerza_gravitacional(planeta, other_planeta)
                fuerza_neta[0] += fuerza[0]  # Suma componente X
                fuerza_neta[1] += fuerza[1]  # Suma componente Y
        actualizar_velocidad(planeta, fuerza_neta, dt)
    
    # Luego actualizamos todas las posiciones
    for planeta in planetas:
        update_position(planeta, dt)
        planeta.orbita.append((planeta.x, planeta.y))  # Registra la nueva posición en la órbita

def animar(frame):
    """
    Función de actualización para cada fotograma de la animación.
    
    Parámetros:
    frame: Número de fotograma (no usado pero requerido por FuncAnimation)
    """
    global planetas
    dt = 0.02  # Paso de tiempo para la simulación
    
    simular(planetas, dt)  # Avanza la simulación un paso
    ax.clear()  # Limpia el gráfico anterior
    
    # Dibuja cada planeta y su órbita
    for planeta in planetas:
        # Dibuja el planeta como un punto
        ax.scatter(planeta.x, planeta.y, color=planeta.color, s=100)
        
        # Dibuja la trayectoria (órbita)
        puntos_actualizados = list(zip(*planeta.orbita))
        ax.plot(puntos_actualizados[0], puntos_actualizados[1], color=planeta.color, linewidth=2)

# Crear instancias de Planeta con coordenadas y velocidades iniciales

# Caso 1: Tres planetas en un sistema gravitacional simple
# Cada planeta tiene masa 2 y velocidades iniciales específicas

planeta_A = Planeta(0, 0, 0.1, 'red', 2, 1, 0)    # Planeta en el origen con velocidad en x positiva
planeta_B = Planeta(2, 0, 0.1, 'green', 2, 0, 1)  # Planeta a la derecha con velocidad en y positiva
planeta_C = Planeta(0, 2, 0.1, 'blue', 2, -1, 0)  # Planeta arriba con velocidad en x negativa

# Lista con todos los planetas para la simulación
planetas = [planeta_A, planeta_B, planeta_C]

# Configurar la animación
fig, ax = plt.subplots()  # Crea una figura y ejes para el gráfico
animacion = FuncAnimation(fig, animar, interval=0)  # Crea la animación con velocidad máxima

# Mostrar la animación
plt.show()