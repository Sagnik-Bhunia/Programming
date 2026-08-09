#include <stdio.h>
#include <math.h>

int main()
{
    int A, B, i, j, isPrime;

    printf("Enter two integers: ");
    scanf("%d %d", &A, &B);

    printf("Prime numbers: ");

    for (i = A; i <= B; i++)
    {
        if (i < 2)
            continue;

        isPrime = 1;

        for (j = 2; j <= sqrt(i); j++)
        {
            if (i % j == 0)
            {
                isPrime = 0;
                break;
            }
        }

        if (isPrime == 1)
            printf("%d ", i);
    }

    return 0;
}
