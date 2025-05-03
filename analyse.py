import time
import random
import matplotlib.pyplot as plt
from ford_fulkerson import ford_fulkerson
from push_relabel import push_relabel
from min_cost_flow import min_cost_flow

def generate_random_graph(n):
    capacities = [[0]*n for _ in range(n)]
    costs = [[0]*n for _ in range(n)]
    
    num_edges = (n**2) // 2
    
    for _ in range(num_edges):
        i, j = random.sample(range(n), 2)
        capacities[i][j] = random.randint(1, 100)
        costs[i][j] = random.randint(1, 100)
    
    return capacities, costs

def analyze_complexity():
    sizes = [10, 20, 40, 100]
    num_trials = 10
    
    results = {
        'FF': {size: [] for size in sizes},
        'PR': {size: [] for size in sizes},
        'MIN': {size: [] for size in sizes}
    }
    
    for size in sizes:
        print(f"Analyzing size {size}...")
        for _ in range(num_trials):
            capacities, costs = generate_random_graph(size)
            
            # Ford-Fulkerson
            start = time.time()
            ford_fulkerson(size, capacities)
            results['FF'][size].append(time.time() - start)
            
            # Push-Relabel
            start = time.time()
            push_relabel(size, capacities)
            results['PR'][size].append(time.time() - start)
            
            
            # Min-Cost Flow
            start = time.time()
            min_cost_flow(size, capacities, costs, size)
            results['MIN'][size].append(time.time() - start)
    
    # Affichage des résultats
    plot_results(results)

def plot_results(results):
    sizes = results['FF'].keys()
    for algo in results:
        avg_times = [
            sum(results[algo][size]) / len(results[algo][size]) if len(results[algo][size]) > 0 else 0
            for size in sizes
        ]
        worst_times = [
            max(results[algo][size]) if len(results[algo][size]) > 0 else 0
            for size in sizes
        ]
        best_times = [
            min(results[algo][size]) if len(results[algo][size]) > 0 else 0
            for size in sizes
        ]
        
        plt.plot(sizes, avg_times, label=f"{algo} (moyenne)")
        plt.plot(sizes, worst_times, '--', label=f"{algo} (pire cas)")
        plt.plot(sizes, best_times, ':', label=f"{algo} (meilleur cas)")
    
    plt.xlabel("Graph size")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()
    
    
analyze_complexity()