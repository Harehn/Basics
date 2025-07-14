#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 25
#define RANGE 10000

int numbers[SIZE];

void init_number(){
    srand(time(0));
    for(int index = 0; index < SIZE; index++){
        numbers[index] = rand() % (RANGE + 1);
    }
}
void swap(int array[], int i, int j){
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}

int get_min(int array[], int i, int j){
    int n = SIZE;
    int min_value = array[i];
    int min_index = i;
    for(int index = i; index < n; index++){
        if (min_value > array[index]){
            min_value = array[index];
            min_index = index;
        }
    }
    return min_index;
}

void print_array(int* array){
    printf("\n[");
    for(int index = 0; index < SIZE; index++){
        printf("%d", array[index]);
        if (index == SIZE - 1) break;
        printf(", ");
    }
    printf("]\n");
}

int main()
{
    init_number();
    printf("Numbers: ");
    print_array(numbers);
    return 0;
}