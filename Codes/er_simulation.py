import numpy as np
import heapq

def des(arrival_rate, service_rate, num_doctors, total_simulation_time=1000, seed=42):
    """
    Discrete-Event Simulation for an M/M/c queueing system (ER model with multiple doctors).

    Returns dict including per-doctor utilization.
    """
    rho = arrival_rate / (num_doctors * service_rate)
    if rho >= 1:
        print("Warning: System is UNSTABLE. Results may not be meaningful.")

    np.random.seed(seed)

    # event: (time, type, doc_id)
    events = []
    current_time = 0.0

    # server tracking
    free_doctors = list(range(num_doctors))
    busy_doctors = []  # list of doc_ids busy

    # metrics
    waiting_times = []
    service_times = []
    time_in_system = []
    queue = []  # arrival times
    queue_lengths = []
    busy_history = []

    # track busy time per doctor
    doctor_busy_time = [0.0] * num_doctors
    last_time = 0.0

    # schedule first arrival
    first = np.random.exponential(1/arrival_rate)
    heapq.heappush(events, (first, 'arrival', None))
    served = 0

    while events and current_time < total_simulation_time:
        current_time, etype, doc = heapq.heappop(events)

        # update busy_time for each busy doctor
        dt = current_time - last_time
        for d in busy_doctors:
            doctor_busy_time[d] += dt
        last_time = current_time

        queue_lengths.append((current_time, len(queue)))
        busy_history.append((current_time, len(busy_doctors)))

        if etype == 'arrival':
            # schedule next arrival
            nxt = current_time + np.random.exponential(1/arrival_rate)
            if nxt <= total_simulation_time:
                heapq.heappush(events, (nxt, 'arrival', None))

            if free_doctors:
                d = free_doctors.pop(0)
                busy_doctors.append(d)
                s = np.random.exponential(1/service_rate)
                heapq.heappush(events, (current_time+s, 'departure', d))
                waiting_times.append(0.0)
                service_times.append(s)
                time_in_system.append(s)
                served += 1
            else:
                queue.append(current_time)

        else:  # departure
            # free doctor doc
            busy_doctors.remove(doc)
            free_doctors.append(doc)

            if queue:
                arr = queue.pop(0)
                wait = current_time - arr
                waiting_times.append(wait)
                s = np.random.exponential(1/service_rate)
                heapq.heappush(events, (current_time+s, 'departure', doc))
                service_times.append(s)
                time_in_system.append(wait+s)
                served += 1
                # doctor immediately busy again
                free_doctors.remove(doc)
                busy_doctors.append(doc)

    total_time = total_simulation_time
    utilization = [bt/total_time for bt in doctor_busy_time]
    idle_time = [total_time - bt for bt in doctor_busy_time]

    return {
        'waiting_times': waiting_times,
        'service_times': service_times,
        'time_in_system': time_in_system,
        'queue_lengths': queue_lengths,
        'busy_history': busy_history,
        'utilization': utilization,
        'idle_time': idle_time,
        'patients_served': served,
        'patients_arrived': served + len(queue)
    }


if __name__ == '__main__':
    import numpy as np
    def test_drive(arrival_rate, service_rate, num_doctors, total_time=1000, seed=42):
        results = des(arrival_rate, service_rate, num_doctors, total_time, seed)

        waiting_times = results['waiting_times']
        avg_wait = np.mean(waiting_times)
        p_wait = np.count_nonzero(waiting_times) / len(waiting_times)

        print(f"Simulated {results['patients_arrived']} patients")
        print(f"Patients served: {results['patients_served']}")
        print(f"Average waiting time (Wq): {avg_wait:.2f} hours")
        print(f"Probability a patient had to wait: {p_wait:.2%}")

        # Print per-doctor utilization
        for idx, util in enumerate(results['utilization'], start=1):
            print(f"Doctor {idx} utilization: {util:.2%}")
        overall_util = np.mean(results['utilization'])
        print(f"Overall utilization: {overall_util:.2%}")

        # Idle times
        for idx, idle in enumerate(results['idle_time'], start=1):
            print(f"Doctor {idx} idle time: {idle:.2f} hours")
        avg_tis = np.mean(results['time_in_system'])
        print(f"Average time in system (W): {avg_tis:.2f} hours")

    test_drive(28, 6, 5, 10000)
