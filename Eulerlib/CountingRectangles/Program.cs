using System.Diagnostics;

int CountingRectangles(int w, int h)
{
    int W = w * (w + 1) >> 1;
    int H = h * (h + 1) >> 1;
    return (h * h - H + h) * (w * w - W + w);
}

Stopwatch sw = new();
sw.Start();

int limit = 2_000_000;
int min = int.MaxValue;
(int w, int h) minRectangle = (0, 0);

for (int i = 0; i < 1000; i++)
{
    for (int j = i; j < 1000; j++)
    {
        int n = CountingRectangles(i, j);
        if (Math.Abs(n - limit) < min)
        {
            min = Math.Abs(n - limit);
            minRectangle = (i, j);
        }
    }
}

sw.Stop();

Console.WriteLine(
    $"Solution = {minRectangle.w * minRectangle.h}, "
    + $"found in {sw.ElapsedMilliseconds} milliseconds."
);
