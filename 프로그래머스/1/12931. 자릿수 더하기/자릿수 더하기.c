#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    
    char s[10];
    int temp = n;
    
    sprintf(s, "%d", temp);
    printf("%s" , s);
        
    int length = strlen(s);
    
    for(int i = 0; i < length; i++){
        int num = s[i] -'0';
        answer += num;
    }
     
    return answer;
}