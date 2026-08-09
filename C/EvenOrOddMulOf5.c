#include<stdio.h>
int main()
{ int n;
printf("Enter an integer");
scanf("%d",&n);
if(n%2==0)
    printf("%d is even.\n",n);
else
    printf("%d is odd.\n",n);
if(n%5==0)
    printf("%d is a multiple of 5");
else
    printf("%d is not a multiple of 5.",n);
return 0;
}
