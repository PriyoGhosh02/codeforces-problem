#include<stdio.h>
#define mod 1000000007

int bigmod(int b, int p){
if(p==0)return 1;
if(p==1) return b%mod;
int val=bigmod(b,p/2);
int total=((long long )val*val)%mod;
if(p%2==1)
    total=(long long )total *b %mod;
return total;
}

int main(){
int t;
scanf("%d", &t);
for(int i=1;i<=t;i++){
    int n,k;
    scanf("%d%d",&n,&k);
    printf("%d\n",bigmod(n,k));

}
}

