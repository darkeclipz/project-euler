using System.Diagnostics;
using Memo = System.Collections.Generic.Dictionary<(int, int), int>;


int PathSum(int[,] M, Memo memo, int i, int j)
{
    // Base case.
    if (i == M.GetLength(0) - 1 && j == M.GetLength(1) - 1)
        return M[i, j];
    
    // Out of bounds.
    if (i >= M.GetLength(0))
        return int.MaxValue;
    
    // Out of bounds.
    if (j >= M.GetLength(0))
        return int.MaxValue;

    // Memoization.
    if (!memo.ContainsKey((i, j)))
    {
        memo[(i, j)] = M[i, j] + Math.Min(PathSum(M, memo, i + 1, j), PathSum(M, memo, i, j + 1));
    }

    return memo[(i, j)];
}

int[,] M = ReadProblem("p081_matrix.txt");
Memo memo = new();

Stopwatch sw = new();
sw.Start();
int sum = PathSum(M, memo, 0, 0);
Console.WriteLine($"Solution = {sum}");
Console.WriteLine($"Time elapsed: {sw.ElapsedMilliseconds} milliseconds.");

int[,] ReadProblem(string filepath)
{
    string[] lines = File.ReadAllLines(filepath);

    int m = lines.Length;
    int n = lines[0].Split(',').Length;
    int[,] matrix = new int[m, n];

    for (int i = 0; i < m; i++)
    {
        int[] elements = lines[i]
            .Split(',')
            .Select(v => int.Parse(v))
            .ToArray();

        for (int j = 0; j < n; j++)
        {
            matrix[i, j] = elements[j];
        }
    }

    return matrix;
}
