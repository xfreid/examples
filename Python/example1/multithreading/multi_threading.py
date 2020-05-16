# multi-threading example
# old APIs

# https://www.youtube.com/watch?v=IEEhzQoKtQU

import time
import threading

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second ...')
    time.sleep(1)
    print('Done sleeping ...')

def do_something(seconds):
    print('Sleeping {seconds} second(s) ...')
    time.sleep(seconds)
    print('Done sleeping ...')
    return 'Done sleeping ...'

# running sequentially
# this will take 2 seconds
# do_something()
# do_something()

# creating threads
# note: this does NOT run the threads
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

# running threads, this is non-blocking
t1.start()
t2.start()

# to wait until all threads complete
t1.join()
t2.join()

# how to create and run many threads
# _ is a throw away variable
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


def 

finish = time.perf_counter()

print(f'Finshed in {round(finish-start, 2)} second(s)')


# a new way of creating threads
import concurrent.futures

# context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    # schedule a function to be exectued, and
    # return a future object
    f1  = executor.submit(do_something, 1)
    f2  = executor.submit(do_something, 1)
    print(f1.result())
    print(f2.result())

    # list comprehension
    secs = [5, 4, 3, 2, 1]
    results = [exectued.submit(do_something, sec) for sec in secs]
    results = [exectued.submit(do_something, 1) for _ in range(10)]
    # f's come in the order of as they are completed
    for f in concurrent.futures.as_completed(results):
        print(f.result())

    # this returns result object instead of future object
    results = exectued.map(do_something, secs)
    # results are returned in the order they are started

    for result in results:
        print(result)

