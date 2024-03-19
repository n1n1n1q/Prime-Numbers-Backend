#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

std::vector<unsigned long long> EratosthenesSieve(long long n){
    std::vector<bool> isPrime(n + 1, true);
    for (long long i = 2; i * i <= n; ++i){
        if (isPrime[i]){
            for(long long j = i * i; j <= n; j+=i){
                isPrime[j]=false;
            }
        }
    }
    std::vector<unsigned long long> primes;
    for (long long i = 1; i <= n; ++i){
        if (isPrime[i]){
            primes.push_back(i);
        }
    }
    return primes;
}

PYBIND11_MODULE(sieve, m) {
    m.def("eratosthenes_sieve", &EratosthenesSieve, "Sieve of Eratosthenes");
}

