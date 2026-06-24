from contextlib import contextmanager

# def  fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# fib = fibonacci()
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))


# def read_file(filename):
#     with open(filename, "r") as f:
#         for line in f:
#             line = line.strip()
#             if line:
#                 yield line

# for line in read_file("test.txt"):
#     print(line)


@contextmanager
def managed_list():
    my_list = []
    print("List ready")
    try:
        yield my_list 
    finally:
        print(f"List size: {len(my_list)}")

with managed_list() as my_list:
    my_list.append("item1")
    my_list.append("item2")
    print(my_list)