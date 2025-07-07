#include <iostream>
#include <cstdlib>
using namespace std;

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
    cout << endl <<"[ ";
    for(int index = 0; index < SIZE; index++){
        cout << array[index];
        if (index == SIZE - 1) break;
        cout << ", ";
    }
    cout << " ]" << endl;
}

int* bubble_sort(int array[]){
    int n = SIZE;
    for(int i = 0; i < n; i++){
        for (int j = i + 1; j < n; j++){
            if (array[i] > array[j]){
                swap(array, i, j);
            }
        }
    }
    return array;
}

int* copy_array(int array[]){
    int n = SIZE;
    int* array2 = (int*) malloc(n * sizeof(int));
    for(int i = 0; i < n; i++){
        array2[i]= array[i];
    }
    return array2;
}

int* selection_sort(int array[]){
    int n = SIZE;
    for(int i = 0; i < n; i++){
        int min_index = get_min(array, i, n);
        swap(array, i, min_index);
    }
    return array;
}

int* insertion_sort(int array[]){
    int n = SIZE;
    for(int i = 0; i < n; i++){
        for(int j = i; j > 0; j--){
            if(array[i] < array[j]){
                swap(array, j - 1, j);
            } else{
                break;
            }
        }
    }
    return array;
}

int main()
{
    init_number();
    cout << "Numbers: ";
    print_array(numbers);
    cout << "Result of BubbleSort:";
    print_array(bubble_sort(copy_array(numbers)));
    cout << "Result of SelectionSort:";
    print_array(selection_sort(copy_array(numbers)));
    cout << "Result of InsertionSort:";
    print_array(insertion_sort(copy_array(numbers)));
    return 0;
}
