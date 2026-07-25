from contextlib import contextmanager

def chunked_reader(data: list, chunk_size: int):
    for i in range(0,len(data),chunk_size):
        yield data[i:i+chunk_size]

@contextmanager
def progress_tracker():
    print("Processing started")
    tracker = {'count': 0}
    try:
        yield tracker 
    finally:
        print(f"Processing complete. Chunks processed: {tracker['count']}")

with progress_tracker() as tracker:
    for chunk in chunked_reader([1,2,3,4,5,6,7], 3):
        print(chunk)
        tracker['count'] += 1   