import random
import matplotlib.pyplot as plt
import time

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
    times_2_approx = []
    times_bb = []
    
    for tasks, m in test_cases:
        # Ejecutar algoritmos y medir tiempos
        start_time = time.time()
        makespan_2_approx = load_balancing_2_approximation(tasks, m)
        time_2_approx = time.time() - start_time
        
        start_time = time.time()
        makespan_bb = branch_and_bound_optimized(tasks, m)
        time_bb = time.time() - start_time
        
        # Guardar resultados
        results_2_approx.append(makespan_2_approx)
        results_bb.append(makespan_bb)
        ratios.append(makespan_2_approx / makespan_bb)
        num_tasks_list.append(len(tasks))
        num_servers_list.append(m)
        times_2_approx.append(time_2_approx)
        times_bb.append(time_bb)
    
    # Crear una figura con dos subgráficos
    plt.figure(figsize=(14, 10))
    
    # Gráfico 1: Comparación de Makespan
    plt.subplot(2, 1, 1)
    plt.plot(range(len(test_cases)), results_2_approx, label="2-Aproximación", marker='o')
    plt.plot(range(len(test_cases)), results_bb, label="Branch and Bound", marker='x')
    # plt.xlabel("Casos de Prueba")
    plt.ylabel("Makespan")
    plt.title("Comparación de Soluciones")
    plt.legend()
    plt.grid()
    
    # Añadir etiquetas con tiempos de ejecución
    for i, (t2, tb) in enumerate(zip(times_2_approx, times_bb)):
        plt.text(i, results_2_approx[i], f"{t2:.2f}s", fontsize=8, ha='center', va='bottom')
        plt.text(i, results_bb[i], f"{tb:.2f}s", fontsize=8, ha='center', va='top')
    
    # Gráfico 2: Ratios entre los algoritmos
    plt.subplot(2, 1, 2)
    plt.plot(range(len(test_cases)), ratios, label="Ratio (2-Aprox / B&B)", marker='o', color='green')
    plt.xlabel("Casos de Prueba")
    plt.ylabel("Ratio")
    plt.title("Relación entre las Soluciones (2-Aproximación / Branch and Bound)")
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
    num_cases = 20          # Número de casos de prueba
    max_tasks = 15         # Máximo número de tareas
    max_servers = 5         # Máximo número de servidores
    max_task_time = 100     # Máximo tiempo de una tarea
    
    # Generar casos de prueba
    test_cases = generate_test_cases(num_cases, max_tasks, max_servers, max_task_time)
    
    # Comparar algoritmos
    compare_algorithms(test_cases)