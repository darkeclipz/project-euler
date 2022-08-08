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
double Phi(int n, PrimeSieve sieve) 
{
    // Strategy 2: use a prime factorization sieve to
    // find the prime factorization of the number quickly,
    // and then use the fact that:
    //
    // If the prime factorisation of n is given by n = p1e1*...*pnen, then φ(n) = n * (1 - 1/p1) * ... (1 - 1/pn).
    var factorization = sieve.Factorize(n).OrderBy(v => v).Distinct().ToArray();

    if (factorization.Length == 0)
    {
        return 1;
    }

    double product = n;

    for (int i = 0; i < factorization.Length; i++)
    {
        product *= (1.0 - 1.0 / (double)factorization[i]);
    }

    return product;
}

var sieve = new PrimeSieve(1000000);
int n = 0;
double max = double.MinValue;
for (int i = 2; i < 1e6; i++)
{
    double phi = Phi(i, sieve);

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

class PrimeSieve
{
    int _size { get; set; }
    bool[] _sieve { get; set; }

    const bool PRIME = false;
    const bool COMPOSITE = true;
    
    public PrimeSieve(int n)
    {
        _size = n + 1;
        _sieve = new bool[_size];
        InitializeSieve(_size);
    }

    void InitializeSieve(int n)
    {
        Set(0, COMPOSITE);
        Set(1, COMPOSITE);

        int upperBound = (int)Math.Sqrt(n);

        for (int i = 2; i < upperBound; i++)
        {
            if (IsPrime(i))
            {
                for (int j = 2; i * j < _size; j++)
                {
                    Set(i * j, COMPOSITE);
                }
            }
        }
    }

    bool Set(int k, bool value) => _sieve[k] = value;
    public bool IsPrime(int k) => !_sieve[k];

    public IEnumerable<int> Factorize(int k)
    {
        if (k == 0 || k == 1)
        {
            return new int[0];
        }

        if (k == 2)
        {
            return new int[1] { 2 };
        }

        List<int> factors = new();

        if (IsPrime(k))
        {
            factors.Add(k);
            return factors;
        }

        int bound = (int)Math.Sqrt(k) + 1;
        for (int i = 2; i < bound; i++)
        {
            if (!IsPrime(i))
            {
                continue;
            }

            if (k % i == 0)
            {
                factors.Add(i);
                k /= i;
            }
        }

        return factors.Concat(Factorize(k));
    }
}
