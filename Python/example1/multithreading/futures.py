# multi-threading example
# old APIs

# https://www.youtube.com/watch?v=IEEhzQoKtQU

import time
# a new way of creating threads
import concurrent.futures

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second ...')
    time.sleep(1)
    print('Done sleeping ...')

def do_something(seconds):
    print(f'Sleeping {seconds} second(s) ...')
    time.sleep(seconds)
    return f'Done sleeping ...{seconds}'

# context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    # schedule a function to be exectued, and
    # return a future object
   #  f1  = executor.submit(do_something, 1)
   #  f2  = executor.submit(do_something, 1)
   #  print(f1.result())
   #  print(f2.result())

    # list comprehension
    secs = [5, 4, 3, 2, 1]
    futures = [executor.submit(do_something, sec) for sec in secs]
    # results = [exectued.submit(do_something, 1) for _ in range(10)]
    # f's come in the order of as they are completed
    for f in concurrent.futures.as_completed(futures):
        print(f.result())

    # this returns result object instead of future object
    # results = exectued.map(do_something, secs)
    # results are returned in the order they are started

    # for result in results:
    #     print(result)


finish = time.perf_counter()

print(f'Finshed in {round(finish-start, 2)} second(s)')




