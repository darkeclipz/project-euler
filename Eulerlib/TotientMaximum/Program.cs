using System.Diagnostics;
using System.Numerics;

// https://en.wikipedia.org/wiki/Binary_GCD_algorithm
int BinaryGCD(int u, int v) 
{
    if (u == 0)
    {
        return v;
    }
    else if(v == 0)
    {
        return u;
    }

    int i = BitOperations.TrailingZeroCount(u); 
    u >>= i;

    int j = BitOperations.TrailingZeroCount(v);
    v >>= j;

    int k = Math.Min(i, j);

    for (;;)
    {
        Debug.Assert(u % 2 == 1, "u is even.");
        Debug.Assert(v % 2 == 1, "v is even.");

        if (u > v)
        {
            (u, v) = (v, u);
        }

        v -= u;

        if (v == 0)
        {
            return u << k;
        }

        v >>= BitOperations.TrailingZeroCount(v);
    }
}

// https://www.doc.ic.ac.uk/~mrh/330tutor/ch05s02.html
double EulersTotient(int n, FactorizationSieve sieve) 
{
    // Strategy 2: use a prime factorization sieve to
    // find the prime factorization of the number quickly,
    // and then use the fact that:
    //
    // If the prime factorisation of n is given by n = p1e1*...*pnen, then φ(n) = n * (1 - 1/p1) * ... (1 - 1/pn).
    var distinctPrimeFactors = sieve.DistinctPrimeFactors(n).ToArray();

    if (distinctPrimeFactors.Length == 0)
    {
        return 1;
    }

    double product = n;

    for (int i = 0; i < distinctPrimeFactors.Length; i++)
    {
        product *= (1.0 - 1.0 / (double)distinctPrimeFactors[i]);
    }

    return product;
}

var sw = new Stopwatch();
sw.Start();

void Benchmark(Action action)
{
    Stopwatch sw = new Stopwatch();
    sw.Start();
    action.Invoke();
    sw.Stop();
    double elapsed = Math.Round(sw.ElapsedMilliseconds / 1000.0, 3);
    Console.WriteLine($"Total runtime is {elapsed} seconds.");
}

Benchmark(() => 
{
    var sieve = new FactorizationSieve(1000000);
    int n = 0;
    double max = double.MinValue;
    for (int i = 30; i < 1e6; i += 30)
    {
        double phi = EulersTotient(i, sieve);

        if (phi != 0)
        {
            double value = (double)i / (double)phi;

            if (value > max)
            {
                max = value;
                n = i;
            }
        }
    }

    Console.WriteLine($"Phi({n}) = {max}");
});

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
