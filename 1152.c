
#include <stdio.h>
int main()
{
    char S[1000000];
    char *new_S;
    int count = 0;
    fgets(S, sizeof(S), stdin);
    for (char *i = S; *(char *)i != 0; i++){
        if (*(char *)i != 32){ // If char is not space : start of them
            new_S = i;
            break;
        }
    }
    for (char *i = new_S; *(char *)i != 0; i++){
        // printf("%d\n",*i);
        if (*(char *)i == 32 && 
            ((*(char *)(i - 1)) != 32 && (*(char *)(i - 1)) >= 31)){
            count++;
        }
        else if (((*(char *)(i - 1)) != 32 && (*(char *)(i - 1)) >= 31) &&
            *(char *)(i + 1) == 0){
            count++;
        }
    }
    printf("%d",count);
    
}
