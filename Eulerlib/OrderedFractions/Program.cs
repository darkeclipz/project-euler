using System;
using System.Diagnostics;
using System.Numerics;

Stopwatch sw = new();
sw.Start();

int a = 2, b = 5, c = 3, d = 7, s = 0;

while (b + d <= 1e6)
{
    a = a + c;
    b = b + d;
    s++;
}

Console.WriteLine(a);
sw.Stop();

Console.WriteLine($"Runtime is {sw.ElapsedTicks / 10000.0 / 1000.0} milliseconds.");
Console.WriteLine($"Total steps: {s}");

// Fraction x = new(2, 4);
// Fraction y = new(3, 7);

// Console.WriteLine($"{x} > {y} = {x > y}");
// Console.WriteLine($"{x} > {x} = {x > x}");
// Console.WriteLine($"{x} == {x} = {x == x}");

// static IEnumerable<Fraction> Q(int d)
// {
//     SortedList<double, Fraction> Q = new();

//     for (int i = 1; i <= d; i++)
//     {
//         for (int j = 1; j < i; j++)
//         {
//             Fraction frac = new(j, i);

//             if (!Q.ContainsKey(frac.Value))
//             {
//                 Q.Add(frac.Value, frac);
//             }
//         }
//     }

//     return Q.Values;
// }

// for (int i = 2; i < 15; i++)
// {
//     Console.WriteLine($"Q({i}) = ".PadLeft(10, ' ') + string.Join(", ", Q(i)));
// }

class Fraction : IEquatable<Fraction>, IComparable<Fraction>
{
    int _num;
    int _den;
    double _value;
    int _gcd;

    public int Num { get => _num; }
    public int Den { get => _den; }
    public double Value { get => _value; }

    public Fraction(int num, int den)
    {
        _gcd = NumberTheory.BinaryGcd(num, den);

        // Reduce the fraction if possible.
        if (_gcd != 1)
        {
            num /= _gcd;
            den /= _gcd;
        }

        _num = num;
        _den = den;
        _value = (double)_num / (double)_den;
    }

    public static bool operator ==(Fraction self, Fraction other)
    {
        return self.Num * other.Den == other.Num * self.Den;
    }

    public static bool operator !=(Fraction self, Fraction other)
    {
        return self.Num * other.Den != other.Num * self.Den;
    }

    public static bool operator >(Fraction self, Fraction other)
    {
        return self.Num * other.Den > other.Num * self.Den;
    }

    public static bool operator >=(Fraction self, Fraction other)
    {
        return self.Num * other.Den >= other.Num * self.Den;
    }

    public static bool operator <(Fraction self, Fraction other)
    {
        return self.Num * other.Den < other.Num * self.Den;
    }

    public static bool operator <=(Fraction self, Fraction other)
    {
        return self.Num * other.Den <= other.Num * self.Den;
    }

    public override bool Equals(object? obj)
    {
        return obj is not null
            && obj is Fraction other 
            && Num == other.Num
            && Den == other.Den;
    }
    
    public override int GetHashCode()
    {
        return base.GetHashCode();
    }

    public bool Equals(Fraction? other)
    {
        return other is not null
            && Num == other.Num
            && Den == other.Den;
    }

    public override string ToString()
    {
        return $"{Num}/{Den}";
    }

    public int CompareTo(Fraction? other)
    {
        ArgumentNullException.ThrowIfNull(other);

        if (this == other)
        {
            return 0;
        }

        return this > other ? 1 : -1;
    }
}

static class NumberTheory
{
    public static int Lcm(int a, int b)
    {
        return a * b / BinaryGcd(a, b);
    }

    public static int BinaryGcd(int u, int v) 
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
}