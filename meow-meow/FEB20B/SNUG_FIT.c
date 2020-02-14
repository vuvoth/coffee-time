#include <stdio.h>
#include <stdlib.h>

#define max_n 10001

int T;
int n;
long long ans;
int a[max_n], b[max_n];

int cmpDec(const void *a, const void *b)
{
    return (*(int *)b - *(int *)a);
}

int cmpInc(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}
int main()
{
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
        {
            scanf("%d", a + i);
        }
        for (int i = 0; i < n; ++i)
        {
            scanf("%d", b + i);
        }

        qsort(b, n, sizeof(int), cmpInc);
        qsort(a, n, sizeof(int), cmpInc);
        ans = 0LL;
        for (int i = 0; i < n; ++i)
        {
            // printf("%d %d\n", a[i], b[i]);
            if (a[i] > b[i])
                ans += b[i];
            else
                ans += a[i];
        }
        printf("%lld\n", ans);
    }
    return 0;
}