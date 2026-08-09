#include <stdio.h>

int main()
{
    int num, n, i;

    printf("Enter the number: ");
    scanf("%d", &num);

    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("\nMultiplication Table of %d:\n", num);

    for(i = 1; i <= n; i++)
    {
        printf("%d x %d = %d\n", num, i, num * i);
    }

    return 0;
}
