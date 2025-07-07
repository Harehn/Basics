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
            if(array[j] < array[j - 1]){
                swap(array, j - 1, j);
            } else{
                break;
            }
        }
    }
    return array;
}

int* split(int array[], int start, int end) {
    int size = end - start + 1;
    int* result = (int*) malloc(sizeof(int) * size);
    for (int i = 0; i < size; i++) {
        result[i] = array[start + i];
    }
    return result;
}

int* merge(int arr1[], int arr2[], int len1, int len2) {
    int* result = (int*) malloc(sizeof(int) * (len1 + len2));
    int i = 0, j = 0, index = 0;
    while (i < len1 && j < len2) {
        if (arr1[i] < arr2[j]) {
            result[index++] = arr1[i++];
        } else {
            result[index++] = arr2[j++];
        }
    }
    while (i < len1) result[index++] = arr1[i++];
    while (j < len2) result[index++] = arr2[j++];
    free(arr1);
    free(arr2);
    return result;
}

int* merge_sort(int array[], int n) {
    if (n < 2) {
        int* result = (int*) malloc(sizeof(int) * n);
        for (int i = 0; i < n; i++) result[i] = array[i];
        return result;
    }
    int len1 = (n + 1) / 2;
    int len2 = n / 2;
    int* arr1 = split(array, 0, len1 - 1);
    int* arr2 = split(array, len1, n - 1);
    return merge(merge_sort(arr1, len1), merge_sort(arr2, len2),len1,len2);
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
    cout << "Result of MergeSort:";
    print_array(merge_sort(copy_array(numbers), SIZE));
    return 0;
}
