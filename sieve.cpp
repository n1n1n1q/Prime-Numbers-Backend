// #include <iostream>
#include <vector>
// #include <ctime>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

std::vector<unsigned long long> EratosthenesSieve(long long n){
    std::vector<int> isPrime(n + 1, 1);
    for (long long i = 2; i * i <= n; ++i){
        if (isPrime[i] == 1){
            for(long long j = i * i; j <= n; j+=i){
                isPrime[j]=0;
            }
        }
    }
    std::vector<unsigned long long> primes;
    for (long long i = 2; i <= n; ++i){
        if (isPrime[i] == 1){
            primes.push_back(i);
        }
    }
    return primes;
}

PYBIND11_MODULE(sieve, m) {
    m.def("eratosthenes_sieve", &EratosthenesSieve, "Sieve of Eratosthenes");
}


// int main(){
//     clock_t start = clock();
//     EratosthenesSieve(100000000);
//     clock_t end = clock();
//     std::cout << double(end - start) / CLOCKS_PER_SEC;
//     return 0;
// }