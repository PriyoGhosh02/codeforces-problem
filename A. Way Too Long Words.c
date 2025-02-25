#include<stdio.h>
#include<string.h>

int main(){
int n,i,len;
char ch[100];
scanf("%d",&n);
for(i=0;i<n;i++){
    scanf("%s",ch);
    len=strlen(ch);
    if(len>10)
        printf("%c%d%c",ch[0],len-2,ch[len-1]);

    else
        printf("%s",ch);
    printf("\n");

}
return 0;
}
