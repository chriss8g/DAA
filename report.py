import random
import matplotlib.pyplot as plt

# ===========================
# Algoritmo 2-Aproximación
# ===========================
def load_balancing_2_approximation(tasks, m):
    machines = [0] * m  # Carga inicial de cada máquina
    for task in tasks:
        # Asignar la tarea a la máquina con menor carga actual
        min_load_machine = machines.index(min(machines))
        machines[min_load_machine] += task
    return max(machines)  # Makespan es la máxima carga entre todas las máquinas

# ===========================
# Algoritmo Branch and Bound Optimizado
# ===========================
def branch_and_bound_optimized(jobs, m):
    """
    Algoritmo Branch and Bound optimizado para Load Balancing.
    
    :param jobs: Lista de tiempos de procesamiento de las tareas.
    :param m: Número de máquinas.
    :return: Makespan mínimo (T_best).
    """
    # Paso 1: Ordenar los trabajos en orden descendente
    jobs = sorted(jobs, reverse=True)
    
    # Paso 2: Inicializar variables
    n = len(jobs)  # Número de trabajos
    T_best = sum(jobs)  # Cota superior inicial (suma total de los tiempos)
    loads = [0] * m  # Carga inicial de cada máquina
    
    def backtrack(current_job, loads, T_best):
        """
        Función recursiva para explorar todas las asignaciones posibles.
        
        :param current_job: Índice del trabajo actual a asignar.
        :param loads: Lista de cargas actuales de las máquinas.
        :param T_best: Mejor makespan encontrado hasta ahora.
        :return: Mejor makespan encontrado.
        """
        # Caso base: Todos los trabajos han sido asignados
        if current_job == n:
            return max(loads)  # El makespan es la máxima carga entre las máquinas
        
        # Obtener el tiempo del trabajo actual
        job = jobs[current_job]
        
        # Probar asignar el trabajo a cada máquina
        for i in range(m):
            # Poda: Si la carga de la máquina supera T_best, no explorar esta rama
            if loads[i] + job >= T_best:
                continue
            
            # Asignar el trabajo a la máquina i
            loads[i] += job
            
            # Llamada recursiva para el siguiente trabajo
            new_T = backtrack(current_job + 1, loads, T_best)
            
            # Actualizar T_best si encontramos una solución mejor
            T_best = min(T_best, new_T)
            
            # Backtracking: Deshacer la asignación
            loads[i] -= job
        
        return T_best
    
    # Paso 3: Llamada inicial a la función recursiva
    return backtrack(0, loads, T_best)

# ===========================
# Generador de Casos de Prueba
# ===========================
def generate_test_cases(num_cases, max_tasks, max_servers, max_task_time):
    test_cases = []
    for _ in range(num_cases):
        num_tasks = random.randint(5, max_tasks)
        num_servers = random.randint(2, max_servers)
        tasks = [random.randint(1, max_task_time) for _ in range(num_tasks)]
        test_cases.append((tasks, num_servers))
    return test_cases

# ===========================
# Comparación y Gráficos
# ===========================
def compare_algorithms(test_cases):
    results_2_approx = []
    results_bb = []
    ratios = []
    num_tasks_list = []
    num_servers_list = []
    
    for tasks, m in test_cases:
        # Ejecutar algoritmos
        makespan_2_approx = load_balancing_2_approximation(tasks, m)
        print("aprox")
        makespan_bb = branch_and_bound_optimized(tasks, m)
        print("exact")
        
        # Guardar resultados
        results_2_approx.append(makespan_2_approx)
        results_bb.append(makespan_bb)
        ratios.append(makespan_2_approx / makespan_bb)
        num_tasks_list.append(len(tasks))
        num_servers_list.append(m)
    
    # Graficar comparación de soluciones
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(test_cases)), results_2_approx, label="2-Aproximación", marker='o')
    plt.plot(range(len(test_cases)), results_bb, label="Branch and Bound", marker='x')
    plt.xlabel("Casos de Prueba")
    plt.ylabel("Makespan")
    plt.title("Comparación de Soluciones")
    plt.legend()
    plt.grid()
    plt.show()
    
    # Graficar relación entre soluciones
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(test_cases)), ratios, label="Relación (2-Aprox / BB)", marker='o', color='green')
    plt.axhline(y=2, color='red', linestyle='--', label="Límite Teórico (2)")
    plt.xlabel("Casos de Prueba")
    plt.ylabel("Relación de Makespan")
    plt.title("Relación entre Soluciones")
    plt.legend()
    plt.grid()
    plt.show()
    

# ===========================
# Ejecución Principal
# ===========================
if __name__ == "__main__":
    # Parámetros para generar casos de prueba
    num_cases = 20          # Número de casos de prueba
    max_tasks = 10          # Máximo número de tareas
    max_servers = 5         # Máximo número de servidores
    max_task_time = 100     # Máximo tiempo de una tarea
    
    # Generar casos de prueba
    test_cases = generate_test_cases(num_cases, max_tasks, max_servers, max_task_time)
    
    # Comparar algoritmos
    compare_algorithms(test_cases)