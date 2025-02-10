import random
import matplotlib.pyplot as plt

# ===========================
# Algoritmo 2-Aproximación
# ===========================
def uk_2_approximation(W, weights, values):
    m = -1
    d = -1
    for i in range(len(weights)):
        if values[i]/weights[i] > d:
            m = i
    return values[m]*(W//weights[m])
    
# ===========================
# Algoritmo Dinamica
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
    
    for W, weights, values in test_cases:
        # Ejecutar algoritmos
        max_value_aprox = uk_2_approximation(W, weights, values)
        print("aprox")
        max_value_dp = unbounded_knapsack(W, weights, values)
        print("exact")
        
        # Guardar resultados
        results_2_approx.append(max_value_aprox)
        results_dp.append(max_value_dp)
        ratios.append(max_value_aprox / max_value_dp)
    
    # Graficar comparación de soluciones
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(test_cases)), results_2_approx, label="2-Aproximación", marker='o')
    plt.plot(range(len(test_cases)), results_dp, label="DP", marker='x')
    plt.xlabel("Casos de Prueba")
    plt.ylabel("Valor Máximo")
    plt.title("Comparación de Soluciones")
    plt.legend()
    plt.grid()
    plt.show()
    
    # Graficar relación entre soluciones
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(test_cases)), ratios, label="Relación (2-Aprox / DP)", marker='o', color='green')
    plt.axhline(y=2, color='red', linestyle='--', label="Límite Teórico (2)")
    plt.xlabel("Casos de Prueba")
    plt.ylabel("Relación del Valor Máximo")
    plt.title("Relación entre Soluciones")
    plt.legend()
    plt.grid()
    plt.show()
    

# ===========================
# Ejecución Principal
# ===========================
if __name__ == "__main__":
    # Parámetros para generar casos de prueba
    num_tests= 10
    max_price= 100
    max_element_weight= 50
    max_knapsack_weight= 200
    num_elements=10

    # Generar casos de prueba
    test_cases = generate_test_cases(num_tests, max_price, max_element_weight, max_knapsack_weight,num_elements)
    
    # Comparar algoritmos
    compare_algorithms(test_cases)