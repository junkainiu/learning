from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor

def calc(n):
    return n*2

# with ThreadPoolExecutor(max_workers=10) as executor:
#     future_n = {executor.submit(calc, n): n for n in range(10)}
#     for future in as_completed(future_n):
#         n = future_n[future]
#         res = future.result()
#         print n
#         print res

with ProcessPoolExecutor(max_workers=10) as executor:
    future_n = {executor.submit(calc, n): n for n in range(10)}
    for future in as_completed(future_n):
        n = future_n[future]
        res = future.result()
        print n
        print res
