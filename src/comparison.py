"""
Cpp and python time comparison
"""
import time
import matplotlib
import matplotlib.pyplot as plt
from sieve import eratosthenes_sieve
from src.pySieve import eratosthenes_sieve_py

matplotlib.use('Qt5Agg')

VALUES = [0, 1000, 100000, 1000000, 100000000]

time_list=[[], []]
for value in VALUES:
    tmp_time=[0, 0]
    start=time.time()
    eratosthenes_sieve(value)
    time_list[0].append(time.time()-start)

    start=time.time()
    eratosthenes_sieve_py(value)
    time_list[1].append(time.time()-start)

plt.xlabel('Values')
plt.ylabel('Runtime')
plt.plot(VALUES, time_list[0], label = "C++")
plt.plot(VALUES, time_list[1], label = "Python")
plt.legend()
plt.show()
