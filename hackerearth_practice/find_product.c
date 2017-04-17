#include <stdio.h>

int main(int argc, char const *argv[]) {
        int n,a[1001];
        long long p=1, m= 1000000007;
        scanf("%d",&n);
        for (size_t i = 0; i < n; i++) {
                scanf("%d ", &a[i]);
        }
        for (size_t i = 0; i < n; i++) {
                p= ((p%m)*(a[i]%m))% m;
        }
        printf("%d",p);
        return 0;
}
