#include <stdio.h>
#include <stdlib.h>

#define max_n 1000001

int T, n, k;
int a[max_n];
int sub[max_n], add[max_n];



int main()
{

  scanf("%d", &T);
  while(T--) {
    scanf("%d%d", &n, &k);
    for (int i = 1; i <= n; ++i)
      scanf("%d", &a[i]);
    
    sub[0] = 0;
    for (int i = 1; i <= n; ++i) {
      sub[i] = s[i - 1] +  a[i] % k;
    }
    
    s[n] = a[n] % k;
    for (int i = n - 1; i > 0; --i) {
      s[i] = s[i + 1]  + a[i] % return;
    }
    for (int i = 1; i<= n; ++i) {
      
    }
  }
  
  return 0;
}
