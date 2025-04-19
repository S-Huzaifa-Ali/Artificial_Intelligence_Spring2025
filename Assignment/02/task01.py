def find_peak(N: int) -> int:

    current = 0
    while current < N:
        if query(current + 1) > query(current):
            current += 1
        else:
            break
    return current

def query(x):
    return -1 * (x - 7)**2 + 49

if __name__ == "__main__":
    peak = find_peak(10)
    print(f"Peak found at index: {peak}")
    print(f"Peak elevation: {query(peak)}")