from scipy.special import factorial, gammaln
import numpy as np

def mmc_metrics(lamb, mu, c):
    rho = lamb / (c * mu)
    if rho >= 1:
        return {
            'rho': rho, 'Pw': float('inf'), 'Lq': float('inf'),
            'Wq': float('inf'), 'L': float('inf'), 'W': float('inf'),
            'stable': False
        }

    a = lamb / mu

    if c <= 30:
        # Exact factorial computation
        terms = np.array([a**n / factorial(n, exact=False) for n in range(c)])
        sum_terms = np.sum(terms)
        last_term = (a**c / factorial(c, exact=False)) * (1 / (1 - rho))
        pi_0 = 1 / (sum_terms + last_term)
        Pw = last_term * pi_0
    else:
        # Logarithmic computation for larger c
        log_terms = np.array([n * np.log(a) - gammaln(n + 1) for n in range(c)])
        max_log_term = np.max(log_terms)
        sum_exp = np.sum(np.exp(log_terms - max_log_term))
        sum_terms = np.exp(max_log_term) * sum_exp

        log_last_term = c * np.log(a) - gammaln(c + 1) - np.log(1 - rho)
        last_term = np.exp(log_last_term)

        pi_0 = 1 / (sum_terms + last_term)
        Pw = last_term * pi_0

    Lq = Pw * rho / (1 - rho)
    Wq = Lq / lamb
    L = Lq + a
    W = L / lamb

    return {
        'rho': rho, 'Pw': Pw, 'Lq': Lq,
        'Wq': Wq, 'L': L, 'W': W, 'stable': True
    }

# Example test
if __name__ == "__main__":
    def test_mmc(lamb, mu, c):
        print(f"Testing M/M/c with λ = {lamb}, μ = {mu}, c = {c}:\n")
        metrics = mmc_metrics(lamb, mu, c)
        if not metrics['stable']:
            print("System is unstable! (ρ ≥ 1)")
        else:
            print(f"ρ   (Traffic Intensity)          = {metrics['rho']:.6f}")
            print(f"Pw  (Prob. patient must wait)    = {metrics['Pw']:.6f}")
            print(f"Lq  (Avg patients in queue)      = {metrics['Lq']:.6f}")
            print(f"Wq  (Avg waiting time in queue)  = {metrics['Wq']:.6f} hours ({metrics['Wq']*60:.2f} minutes)")
            print(f"L   (Avg patients in system)     = {metrics['L']:.6f}")
            print(f"W   (Avg time in system)          = {metrics['W']:.6f} hours ({metrics['W']*60:.2f} minutes)")
            print("System is stable (ρ < 1)")

    # Run test with your parameters
    test_mmc(lamb=208.33, mu=1.32, c=158)
