def round_robin(processes, time_quantum):
    current_time = 0
    ready_queue = []
    metrics = []
    total_tat, total_wt = 0, 0
    n = len(processes)

    for process in processes:
        process['remaining_time'] = process['burst_time']

    while any(process['remaining_time'] > 0 for process in processes):
        for process in processes:
            if process['arrival_time'] <= current_time and process not in ready_queue and process['remaining_time'] > 0:
                ready_queue.append(process)

        if ready_queue:
            current_process = ready_queue.pop(0)
            if current_process['remaining_time'] > time_quantum:
                current_time += time_quantum
                current_process['remaining_time'] -= time_quantum
            else:
                current_time += current_process['remaining_time']
                current_process['remaining_time'] = 0
                current_process['completion_time'] = current_time
                current_process['turnaround_time'] = current_process['completion_time'] - current_process['arrival_time']
                current_process['waiting_time'] = current_process['turnaround_time'] - current_process['burst_time']
                total_tat += current_process['turnaround_time']
                total_wt += current_process['waiting_time']
                metrics.append(current_process)

            # Add processes that arrived during this process execution
            for process in processes:
                if process['arrival_time'] <= current_time and process not in ready_queue and process['remaining_time'] > 0:
                    ready_queue.append(process)

            # Re-add the current process to the queue if it's not yet completed
            if current_process['remaining_time'] > 0:
                ready_queue.append(current_process)
        else:
            current_time += 1

    avg_tat = total_tat / n
    avg_wt = total_wt / n
    return metrics, avg_tat, avg_wt

def display_metrics(metrics, avg_tat, avg_wt):
    print("\nProcess Metrics:")
    print("ID\tArrival\tBurst\tCompletion\tTAT\tWT")
    for process in metrics:
        print(f"{process['id']}\t{process['arrival_time']}\t{process['burst_time']}\t{process['completion_time']}\t\t{process['turnaround_time']}\t{process['waiting_time']}")
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

def main():
    n = int(input("Enter the number of processes: "))
    processes = []
    for i in range(n):
        process_id = input(f"Enter Process ID for process {i + 1}: ")
        arrival_time = int(input(f"Enter Arrival Time for process {process_id}: "))
        burst_time = int(input(f"Enter Burst Time for process {process_id}: "))
        processes.append({
            'id': process_id,
            'arrival_time': arrival_time,
            'burst_time': burst_time
        })

    time_quantum = int(input("Enter the Time Quantum: "))

    print("\nRound Robin Scheduling Results:")
    rr_metrics, rr_avg_tat, rr_avg_wt = round_robin(processes, time_quantum)
    display_metrics(rr_metrics, rr_avg_tat, rr_avg_wt)

if __name__ == "__main__":
    main()
