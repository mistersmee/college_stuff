#include <stdio.h>
#include <limits.h>

// Number of matrices is 6
#define N 6

// Matrix Ai has dimension p[i-1] x p[i] for i = 1..6
int p[] = {30, 35, 15, 5, 10, 20, 25};

// Function to find the most efficient way to multiply the given matrices
void matrixChainOrder()
{
    // Cost matrix for storing the minimum number of multiplications needed to compute the matrix
    int m[N][N];

    // Parenthesis matrix stores the index at which the split is made
    int s[N][N];

    // Initializing the cost and parenthesis matrices
    for (int i = 1; i < N; i++)
        m[i][i] = 0;

    for (int L = 2; L < N; L++)
    {
        for (int i = 1; i < N - L + 1; i++)
        {
            int j = i + L - 1;
            m[i][j] = INT_MAX;
            for (int k = i; k <= j - 1; k++)
            {
                int cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j];
                if (cost < m[i][j])
                {
                    m[i][j] = cost;
                    s[i][j] = k;
                }
            }
        }
    }

    // Printing the optimal solution
    printf("Minimum number of multiplications: %d\n", m[1][N - 1]);
}

// Driver code
int main()
{
    matrixChainOrder();
    return 0;
}
