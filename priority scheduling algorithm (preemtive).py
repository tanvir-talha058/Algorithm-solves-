import heapq
def priority_scheduling(processes):
    current_time = 0
    completed = 0
    n = len(processes)
    ready_queue = []
    metrics = []
    total_tat, total_wt = 0, 0

    while completed < n:
        for process in processes:
            if process['arrival_time'] <= current_time and process['remaining_time'] > 0 and process not in ready_queue:
                heapq.heappush(ready_queue, (process['priority'], process))

        if ready_queue:
            _, current_process = heapq.heappop(ready_queue)
            if current_process['remaining_time'] == current_process['burst_time']:
                current_process['start_time'] = current_time

            current_process['remaining_time'] -= 1
            current_time += 1

            if current_process['remaining_time'] == 0:
                current_process['completion_time'] = current_time
                current_process['turnaround_time'] = current_process['completion_time'] - current_process['arrival_time']
                current_process['waiting_time'] = current_process['turnaround_time'] - current_process['burst_time']
                total_tat += current_process['turnaround_time']
                total_wt += current_process['waiting_time']
                metrics.append(current_process)
                completed += 1
        else:
            current_time += 1

    avg_tat = total_tat / n
    avg_wt = total_wt / n
    return metrics, avg_tat, avg_wt

def display_metrics(metrics, avg_tat, avg_wt):
    print("\nProcess Metrics:")
    print("ID\tArrival\tBurst\tPriority\tCompletion\tTAT\tWT")
    for process in metrics:
        print(f"{process['id']}\t{process['arrival_time']}\t{process['burst_time']}\t{process['priority']}\t{process['completion_time']}\t\t{process['turnaround_time']}\t{process['waiting_time']}")
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

def main():
    n = int(input("Enter the number of processes: "))
    processes = []
    for i in range(n):
        process_id = input(f"Enter Process ID for process {i + 1}: ")
        arrival_time = int(input(f"Enter Arrival Time for process {process_id}: "))
        burst_time = int(input(f"Enter Burst Time for process {process_id}: "))
        priority = int(input(f"Enter Priority for process {process_id}: "))
        processes.append({
            'id': process_id,
            'arrival_time': arrival_time,
            'burst_time': burst_time,
            'priority': priority,
            'remaining_time': burst_time
        })

    print("\nPriority Scheduling Results:")
    priority_metrics, priority_avg_tat, priority_avg_wt = priority_scheduling(processes)
    display_metrics(priority_metrics, priority_avg_tat, priority_avg_wt)

if __name__ == "__main__":
    main()
