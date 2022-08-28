using System.Diagnostics;

// def farey_sequence(n: int, descending: bool = False) -> None:
//     """Print the n'th Farey sequence. Allow for either ascending or descending."""
//     (a, b, c, d) = (0, 1, 1, n)
//     if descending:
//         (a, c) = (1, n - 1)
//     print("{0}/{1}".format(a, b))
//     while (c <= n and not descending) or (a > 0 and descending):
//         k = (n + b) // d
//         (a, b, c, d) = (c, d, k * c - a, k * d - b)
//         print("{0}/{1}".format(a, b))

Benchmark(() =>
{
    var (a, b, c, d, count) = (1L, 3L, 1L, 2L, 0L);
    bool started = false;

    foreach(var (p, q) in FareySequence((int)8))
    {
        if ((c == p) && (d == q))
        {
            break;
        }

        count++;
    }

    Console.WriteLine(count);
});

IEnumerable<(int, int)> FareySequence(int n)
{
    var (a, b, c, d) = (1, 3, 7, 20);
    while (c <= n)
    {
        Debug.Assert(a >= 0);
        Debug.Assert(b >= 0);

        int k = (n + b) / d;
        (a, b, c, d) = (c, d, k * c - a, k * d - b);

        Console.WriteLine($"{a}/{b}  (a={a}, b={b}, c={c}, d={d})");
        yield return (a, b);
    }
}

void Benchmark(Action action)
{
    Stopwatch sw = new Stopwatch();
    sw.Start();
    action.Invoke();
    sw.Stop();
    double elapsed = Math.Round(sw.ElapsedMilliseconds / 1000.0, 3);
    Console.WriteLine($"Total runtime is {elapsed} seconds.");
}
