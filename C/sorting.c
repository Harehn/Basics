#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int range = 100;

void print_array(int arr[], int size){
    for(int i = 0; i < size; i++){
        printf("%d, ", arr[i] % range);
    }
}

void random_arr(int arr[], int size){
    srand(time(NULL));
    for(int i = 0; i < size; i++){
        arr[i] = rand();
    }
}

void swap(int arr[], int pos1, int pos2){
    int temp = arr[pos1];
    arr[pos1] = arr[pos2];
    arr[pos2] = temp;
}

int main()
{
    int numbers[12];
    int n = sizeof(numbers)/sizeof(numbers[0]);
    random_arr(numbers, n);
    print_array(numbers, n);
    
    swap(numbers, 0, 1);
    printf("\n");
    print_array(numbers, n);
    return 0;
}
