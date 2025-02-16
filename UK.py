import random
import matplotlib.pyplot as plt
import time

# ===========================
# Algoritmo 2-Aproximación
# ===========================
def uk_2_approximation(W, weights, values):
    m = -1
    d = -1
    for i in range(len(weights)):
        if values[i] / weights[i] > d and weights[i] < W:
            m = i
            d = values[i] / weights[i]
    return values[m]*(W//weights[m])
    
# ===========================
# Algoritmo Dinámica
# ===========================
def unbounded_knapsack(W, weights, values):
    n = len(weights)
    dp = [0] * (W + 1)
    
    for i in range(W + 1):
        for j in range(n):
            if weights[j] <= i:
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])
    
    return dp[W]

# ===========================
# Generador de Casos de Prueba
# ===========================
def generate_test_cases(num_tests, max_price, max_element_weight, max_knapsack_weight, num_elements):
    test_cases = []
    for _ in range(num_tests):
        W = random.randint(1, max_knapsack_weight)
        weights = [random.randint(1, max_element_weight) for _ in range(num_elements)]
        values = [random.randint(1, max_price) for _ in range(num_elements)]
        test_cases.append((W, weights, values))
    return test_cases

# ===========================
# Comparación y Gráficos
# ===========================
def compare_algorithms(test_cases):
    results_2_approx = []
    results_dp = []
    ratios = []
    times_2_approx = []
    times_dp = []
    
    for W, weights, values in test_cases:
        # Ejecutar algoritmos y medir tiempos
        start_time = time.time()
        max_value_aprox = uk_2_approximation(W, weights, values)
        time_2_approx = time.time() - start_time
        
        start_time = time.time()
        max_value_dp = unbounded_knapsack(W, weights, values)
        time_dp = time.time() - start_time
        
        # Guardar resultados
        results_2_approx.append(max_value_aprox)
        results_dp.append(max_value_dp)
        ratios.append(max_value_dp / max_value_aprox)
        times_2_approx.append(time_2_approx)
        times_dp.append(time_dp)
    
    # Crear una figura con dos subgráficos
    plt.figure(figsize=(14, 10))
    
    # Gráfico 1: Comparación de Valores Máximos
    plt.subplot(2, 1, 1)
    plt.plot(range(len(test_cases)), results_2_approx, label="2-Aproximación", marker='o')
    plt.plot(range(len(test_cases)), results_dp, label="Programación Dinámica", marker='x')
    plt.xlabel("Casos de Prueba")
    plt.ylabel("Valor Máximo")
    plt.title("Comparación de Soluciones")
    plt.legend()
    plt.grid()
    
    # Añadir etiquetas con tiempos de ejecución
    for i, (t2, td) in enumerate(zip(times_2_approx, times_dp)):
        plt.text(i, results_2_approx[i], f"{t2:.4f}s", fontsize=8, ha='center', va='bottom')
        plt.text(i, results_dp[i], f"{td:.4f}s", fontsize=8, ha='center', va='top')
    
    # Gráfico 2: Ratios entre los algoritmos
    plt.subplot(2, 1, 2)
    plt.plot(range(len(test_cases)), ratios, label="Ratio (DP / 2-Aprox)", marker='o', color='green')
    plt.axhline(y=2, color='red', linestyle='--', label="Límite Teórico (2)")
    plt.xlabel("Casos de Prueba")
    plt.ylabel("Ratio")
    plt.title("Relación entre las Soluciones (2-Aproximación / Programación Dinámica)")
    plt.legend()
    plt.grid()
    
    # Añadir etiquetas con los ratios
    for i, r in enumerate(ratios):
        plt.text(i, r, f"{r:.2f}", fontsize=8, ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

# ===========================
# Ejecución Principal
# ===========================
if __name__ == "__main__":
    # Parámetros para generar casos de prueba
    num_tests = 10
    max_price = 1000          # Valores altos para crear elementos de alta densidad
    max_element_weight = 100  # Pesos variados pero manejables
    max_knapsack_weight = 10**5  # Capacidad muy grande (afecta al algoritmo exacto)
    num_elements = 50      # Incluye 1 elemento de densidad alta y otros con densidades engañosas        # Mantén 10 elementos para diversidad

    # Generar casos de prueba
    test_cases = generate_test_cases(num_tests, max_price, max_element_weight, max_knapsack_weight, num_elements)
    for i in test_cases:
        print (i)
   
    # Comparar algoritmos
    compare_algorithms(test_cases)