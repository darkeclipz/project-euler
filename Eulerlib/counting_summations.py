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
        memo[(i, j)] = M[i, j] + Math.Min(PathSum(M, memo, i + 1, j), PathSum(M, memo, i, j + 1));

    return memo[(i, j)];
}

Memo memo = new();
int sum = PathSum(M, memo, 0, 0);
Console.WriteLine($"Solution = {sum}");