# FIFO Page Replacement Algorithm
def fifo(pages, n, capacity):
    s = set()
    indexes = []
    page_faults = 0

    for page in pages:
        if page not in s:
            if len(s) < capacity:
                s.add(page)
                indexes.append(page)
            else:
                val = indexes.pop(0)
                s.remove(val)
                s.add(page)
                indexes.append(page)
            page_faults += 1

    return page_faults

# LRU Page Replacement Algorithm
def lru(pages, n, capacity):
    s = set()
    indexes = []
    page_faults = 0

    for page in pages:
        if page not in s:
            if len(s) < capacity:
                s.add(page)
                indexes.append(page)
            else:
                lru_page = indexes.pop(0)
                s.remove(lru_page)
                s.add(page)
                indexes.append(page)
            page_faults += 1
        else:
            indexes.remove(page)
            indexes.append(page)

    return page_faults

# Optimal Page Replacement Algorithm
def opt(pages, n, capacity):
    s = set()
    page_faults = 0

    for i in range(n):
        page = pages[i]
        if page not in s:
            if len(s) < capacity:
                s.add(page)
            else:
                farthest = -1
                val_to_remove = None
                for val in s:
                    if val not in pages[i + 1:]:
                        val_to_remove = val
                        break
                    else:
                        index = pages[i + 1:].index(val)
                        if index > farthest:
                            farthest = index
                            val_to_remove = val

                s.remove(val_to_remove)
                s.add(page)
            page_faults += 1

    return page_faults

# Main Function
def main():
    # Input from user
    capacity = int(input("Enter the number of page frames: "))
    pages = list(map(int, input("Enter the page reference string (comma-separated): ").split(',')))
    n = len(pages)

    # Calculate page faults for each algorithm
    fifo_faults = fifo(pages, n, capacity)
    lru_faults = lru(pages, n, capacity)
    opt_faults = opt(pages, n, capacity)

    # Output Results
    print("\nResults:")
    print(f"FIFO: Page Faults = {fifo_faults}")
    print(f"LRU: Page Faults = {lru_faults}")
    print(f"OPT: Page Faults = {opt_faults}")

if __name__ == "__main__":
    main()
