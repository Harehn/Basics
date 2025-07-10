#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void makeIntArray(int* arr, int length){
    time_t t;
    srand((unsigned) time(&t));
    for(int i = 0; i<length; i++){
        arr[i] = rand()%2;
    }
}

int findMaxConsecutiveOnes(int* arr, int length){
    int currmax = 0;
    int max = 0;
    for(int i = 0; i<length; i++){
        int num = arr[i];
        if (num == 1){
            currmax++;
        } else {
            if(currmax > max){
                max = currmax;
            }
            currmax = 0;
        }
    }
    return max;
}

void printArr(int* arr, int length){
    for(int i = 0; i<length; i++){
        int num = arr[i];
        printf("%d ", arr[i]);
    }
}

int main()
{
    int arr[16] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    makeIntArray(arr, 16);
    printArr(arr, 16);
    printf("\nMax ones = %d ", findMaxConsecutiveOnes(arr,16));
    return 0;
}
