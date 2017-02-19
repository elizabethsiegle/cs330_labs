#include <stdio.h>
#include <stdlib.h>

int isOdd(int n) {
    return (n%(2) == 1);
}
//returns -5..-3.. as False

int isOdd2(int n) {
    return (n%2 != 0);
}
//returns all correct

int isOdd3(int n) {
    return (n & 1) != 0;
}
//returns all correct

int main(){
    for(int i=-5; i<=5; i++){
        printf("%d %s\n", i, isOdd(i)?"true":"false"); 
    }
    //printf("%d \n", (-5)%2);
}



