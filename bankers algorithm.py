def calculate_need(max_need, allocation):
    need = []
    for i in range(len(max_need)):
        need.append([max_need[i][j] - allocation[i][j] for j in range(len(max_need[i]))])
    return need


def is_safe(available, allocation, need):
    n_processes = len(allocation)
    n_resources = len(available)
    work = available[:]
    finish = [False] * n_processes
    safe_sequence = []

    while len(safe_sequence) < n_processes:
        allocated = False
        for i in range(n_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(n_resources)):
                work = [work[j] + allocation[i][j] for j in range(n_resources)]
                finish[i] = True
                safe_sequence.append(i)
                allocated = True
                break

        if not allocated:
            return False, []

    return True, safe_sequence

def bankers_algorithm():
    # Input number of processes and resource types
    n_processes = int(input("Enter the number of processes: "))
    n_resources = int(input("Enter the number of resource types: "))

    print("\nEnter the Maximum Need matrix:")
    max_need = [list(map(int, input(f"Process {i + 1}: ").split())) for i in range(n_processes)]

    print("\nEnter the Allocation matrix:")
    allocation = [list(map(int, input(f"Process {i + 1}: ").split())) for i in range(n_processes)]

    print("\nEnter the Available Resources vector:")
    available = list(map(int, input().split()))

    # Calculate Need matrix
    need = calculate_need(max_need, allocation)

    print("\nNeed Matrix:")
    for row in need:
        print(row)

    # Check system safety
    safe, safe_sequence = is_safe(available, allocation, need)

    if safe:
        print("\nThe system is in a safe state.")
        print("Safe sequence:", " -> ".join([f"P{i}" for i in safe_sequence]))
    else:
        print("\nThe system is NOT in a safe state.")

def main():
    bankers_algorithm()

if __name__ == "__main__":
    main()
