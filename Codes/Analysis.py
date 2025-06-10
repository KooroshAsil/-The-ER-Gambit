import numpy as np
import matplotlib.pyplot as plt
from mmc_analytics import mmc_metrics  # assumes mmc_metrics is imported from mmc.py
from er_simulation import des          # assumes des function is imported from des.py

"""
===============================================================================
 Why Do We Simulate an M/M/c Queue When We Already Have Analytical Solutions?
===============================================================================

This project involves both:
1. Analytical derivation of performance metrics (e.g., Wq, Lq, ρ) using queueing theory.
2. Discrete-event simulation (DES) of the same system.

...

Conclusion:
Simulating an analytically solvable queue is NOT redundant—it validates the model,
builds trust in the implementation, and prepares us for richer, more realistic modeling.
===================================================================================
"""

def compare_metrics(arrival_rate, service_rate, c_range, sim_time=10000):
    sim_results = {'c': [], 'Wq': [], 'W': [], 'Lq': []}
    theo_results = {'c': [], 'Wq': [], 'W': [], 'Lq': []}

    for c in c_range:
        theo = mmc_metrics(arrival_rate, service_rate, c)
        if not theo['stable']:
            continue

        sim = des(arrival_rate, service_rate, c, total_simulation_time=sim_time)
        sim_Wq = np.mean([w for w in sim['waiting_times'] if w > 0])  # conditional avg
        sim_W = np.mean(sim['time_in_system'])
        sim_Lq = sim_Wq * arrival_rate

        # Store simulation results
        sim_results['c'].append(c)
        sim_results['Wq'].append(sim_Wq)
        sim_results['W'].append(sim_W)
        sim_results['Lq'].append(sim_Lq)

        # Store analytical results
        theo_results['c'].append(c)
        theo_results['Wq'].append(theo['Wq'])
        theo_results['W'].append(theo['W'])
        theo_results['Lq'].append(theo['Lq'])

    return sim_results, theo_results


def plot_all_metrics(sim, theo):
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    metrics = [('Wq', 'Avg Waiting Time in Queue (Wq) [hrs]'),
               ('W', 'Avg Time in System (W) [hrs]'),
               ('Lq', 'Avg Number in Queue (Lq)')]

    for i, (key, ylabel) in enumerate(metrics):
        axs[i].plot(sim['c'], sim[key], 'o-', color='blue', label='Simulation')
        axs[i].plot(theo['c'], theo[key], 's--', color='red', label='Analytical')
        axs[i].set_xlabel('Number of Doctors (c)')
        axs[i].set_ylabel(ylabel)
        axs[i].set_title(ylabel)
        axs[i].grid(True)
        axs[i].legend()

    fig.suptitle('Simulation vs Analytical Results for M/M/c Queueing (ER Model)', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


def print_interpretation(sim, theo):
    print("\n=== Metric Comparison: Simulation vs Analytical ===\n")
    print("{:<6} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10}".format(
        "Doctors", "Wq(sim)", "Wq(anal)", "%Err", "W(sim)", "W(anal)", "%Err"
    ))

    for i in range(len(sim['c'])):
        c = sim['c'][i]

        # Extract metrics
        wq_sim = sim['Wq'][i]
        wq_theo = theo['Wq'][i]
        w_sim = sim['W'][i]
        w_theo = theo['W'][i]

        # Error calculations
        wq_err = 100 * abs(wq_sim - wq_theo) / max(wq_theo, 1e-8)
        w_err = 100 * abs(w_sim - w_theo) / max(w_theo, 1e-8)

        print(f"{c:<6} {wq_sim:>10.3f} {wq_theo:>10.3f} {wq_err:>10.2f}% {w_sim:>10.3f} {w_theo:>10.3f} {w_err:>10.2f}%")

    print("\n=== Interpretation ===")
    print("1. Simulation and analytical results align closely when traffic intensity (ρ) is moderate.")
    print("2. Slight discrepancies are expected due to stochastic fluctuations in the simulation.")
    print("3. As the number of doctors increases, average waiting time and queue length decrease.")
    print("4. The system becomes more stable with more doctors (lower ρ), lowering both Wq and W.")
    print("5. Percentage error >5% may indicate either low sample size or high system variability.\n")


def sensitivity_to_arrival_rate(service_rate, num_doctors, lambda_values, sim_time=10000):
    """
    Simulate and analyze performance metrics as arrival rate (lambda) increases.
    """
    Wq_list = []
    W_list = []
    Lq_list = []
    utilization = []

    for lamb in lambda_values:
        sim = des(lamb, service_rate, num_doctors, total_simulation_time=sim_time)

        sim_Wq = np.mean([w for w in sim['waiting_times'] if w > 0])
        sim_W = np.mean(sim['time_in_system'])
        sim_Lq = sim_Wq * lamb
        rho = lamb / (num_doctors * service_rate)

        Wq_list.append(sim_Wq)
        W_list.append(sim_W)
        Lq_list.append(sim_Lq)
        utilization.append(rho)

    return {
        'lambda': lambda_values,
        'Wq': Wq_list,
        'W': W_list,
        'Lq': Lq_list,
        'utilization': utilization
    }


def plot_sensitivity(results):
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    axs[0].plot(results['lambda'], results['Wq'], 'o-', color='blue', label='Wq')
    axs[0].set_title('Waiting Time vs Arrival Rate')
    axs[0].set_xlabel('Arrival Rate (λ)')
    axs[0].set_ylabel('Avg Waiting Time in Queue (Wq) [hrs]')
    axs[0].grid(True)

    axs[1].plot(results['lambda'], results['Lq'], 's--', color='red', label='Lq')
    axs[1].set_title('Queue Length vs Arrival Rate')
    axs[1].set_xlabel('Arrival Rate (λ)')
    axs[1].set_ylabel('Avg Queue Length (Lq)')
    axs[1].grid(True)

    axs[2].plot(results['lambda'], results['utilization'], '^-', color='green', label='Utilization')
    axs[2].set_title('Utilization vs Arrival Rate')
    axs[2].set_xlabel('Arrival Rate (λ)')
    axs[2].set_ylabel('Utilization (ρ)')
    axs[2].grid(True)

    fig.suptitle('Sensitivity to Arrival Rate in M/M/c Simulation (Fixed c)', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


def print_sensitivity_summary(results):
    print("\n=== Sensitivity Analysis Summary ===\n")
    print("{:>8} {:>8} {:>8} {:>8} {:>8}".format("λ", "Wq", "W", "Lq", "ρ"))
    for i in range(len(results['lambda'])):
        print("{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}".format(
            results['lambda'][i], results['Wq'][i], results['W'][i],
            results['Lq'][i], results['utilization'][i]
        ))
    print("\nObservations:")
    print("1. As λ increases, Wq and Lq grow rapidly, especially when ρ > 0.8.")
    print("2. Utilization approaches 1 as λ approaches c × μ.")
    print("3. System stability is compromised near ρ = 1 (saturation).")
    print("4. Proper capacity planning requires keeping ρ < 0.85 for predictable performance.\n")


def sensitivity_on_servers(arrival_rate, service_rate, c_range, sim_time=10000):
    """
    Analyze how the system behaves as the number of servers (doctors) varies
    for a fixed arrival rate.
    """
    sim_results = {'c': [], 'Wq': [], 'W': [], 'Lq': [], 'rho': []}
    theo_results = {'c': [], 'Wq': [], 'W': [], 'Lq': [], 'rho': []}

    for c in c_range:
        theo = mmc_metrics(arrival_rate, service_rate, c)
        if not theo['stable']:
            print(f"System unstable for c={c} servers; skipping.")
            continue

        sim = des(arrival_rate, service_rate, c, total_simulation_time=sim_time)

        sim_Wq = np.mean([w for w in sim['waiting_times'] if w > 0])
        sim_W = np.mean(sim['time_in_system'])
        sim_Lq = sim_Wq * arrival_rate
        rho = arrival_rate / (c * service_rate)

        sim_results['c'].append(c)
        sim_results['Wq'].append(sim_Wq)
        sim_results['W'].append(sim_W)
        sim_results['Lq'].append(sim_Lq)
        sim_results['rho'].append(rho)

        theo_results['c'].append(c)
        theo_results['Wq'].append(theo['Wq'])
        theo_results['W'].append(theo['W'])
        theo_results['Lq'].append(theo['Lq'])
        theo_results['rho'].append(rho)

    return sim_results, theo_results


if __name__ == '__main__':
    # Parameters (example for ER scenario)
    arrival_rate = 3  # patients/hour
    service_rate = 2  # patients per hour per doctor
    c_range = range(2, 7)  # doctors from 2 to 6
    sim_time = 10000  # total simulation time in hours

    # 1) Compare simulation vs analytical across c (number of servers)
    sim_metrics, theo_metrics = compare_metrics(arrival_rate, service_rate, c_range, sim_time)
    plot_all_metrics(sim_metrics, theo_metrics)
    print_interpretation(sim_metrics, theo_metrics)

    # 2) Sensitivity analysis to arrival rate for fixed number of doctors
    lambda_values = np.linspace(1, 6, 12)  # vary arrival rate from 1 to 6
    sensitivity_results = sensitivity_to_arrival_rate(service_rate, c=4, lambda_values=lambda_values, sim_time=sim_time)
    plot_sensitivity(sensitivity_results)
    print_sensitivity_summary(sensitivity_results)

    # 3) Sensitivity analysis on number of servers (c)
    sim_c_sensitivity, theo_c_sensitivity = sensitivity_on_servers(arrival_rate=3.5, service_rate=service_rate, c_range=range(1, 10), sim_time=sim_time)
    plot_all_metrics(sim_c_sensitivity, theo_c_sensitivity)
