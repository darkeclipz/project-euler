// See https://aka.ms/new-console-template for more information
using System.Diagnostics;

Console.WriteLine("Hello, World!");

Benchmark(() =>
{
    int n = 1_000_000;
    FactorizationSieve sieve = new(n);
    long answer = 1 + SummatoryTotient(n, sieve);
    Console.WriteLine(answer);
});

void Benchmark(Action action)
{
    Stopwatch sw = new Stopwatch();
    sw.Start();
    action.Invoke();
    sw.Stop();
    double elapsed = Math.Round(sw.ElapsedMilliseconds / 1000.0, 3);
    Console.WriteLine($"Total runtime is {elapsed} seconds.");
}

long SummatoryTotient(int n, FactorizationSieve sieve)
{
    long sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += (int)EulersTotient(i, sieve);
    }
    return sum;
}

double EulersTotient(int n, FactorizationSieve sieve) 
{
    var distinctPrimeFactors = sieve.DistinctPrimeFactors(n).ToArray();

    if (distinctPrimeFactors.Length == 0)
    {
        return 0;
    }

    double product = n;

    for (int i = 0; i < distinctPrimeFactors.Length; i++)
    {
        product *= (1.0 - 1.0 / (double)distinctPrimeFactors[i]);
    }

    return product;
}

class FactorizationSieve
{
    int _size { get; set; }
    int[] _sieve { get; set; }
    const int PRIME = 0;
    
    public FactorizationSieve(int n)
    {
        _size = n + 1;
        _sieve = new int[_size];
        InitializeSieve(_size);
    }

    void InitializeSieve(int n)
    {
        _sieve[0] = 1;
        _sieve[1] = 1;

        int upperBound = (int)Math.Sqrt(n);

        for (int i = 2; i < upperBound; i++)
        {
            if (IsPrime(i))
            {
                for (int j = 2; i * j < _size; j++)
                {
                    _sieve[i * j] = i;
                }
            }
        }
    }

    public bool IsPrime(int k) => _sieve[k] == PRIME;

    public IEnumerable<int> PrimeFactors(int k)
    {
        List<int> factors = new();

        while (k != 1)
        {
            int smallestPrimeFactor = _sieve[k];

            if (smallestPrimeFactor == PRIME)
            {
                factors.Add(k);
                return factors;
            }

            factors.Add(smallestPrimeFactor);
            k /= smallestPrimeFactor;
        }

        return factors;
    }

    public IEnumerable<int> DistinctPrimeFactors(int k)
    {
        return PrimeFactors(k).Distinct();
    }

    public IEnumerable<int> Primes
    {
        get
        {
            for (int i = 2; i < _size; i++)
            {
                if (IsPrime(i))
                {
                    yield return i;
                }
            }
        }
    }
}
