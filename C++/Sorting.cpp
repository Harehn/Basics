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

int* tree_sort(int array[]){
    class node{
        public:
        int val;
        node* right;
        node* left;
        node(int val_f, node* right_f, node* left_f){
            val = val_f;
            right = right_f;
            left = left_f;
        }
        void insert(int val_f){
            if (val < val_f){
                if (right != NULL) right->insert(val_f);
                else right = new node(val_f, NULL, NULL);
            }else {
                if (left != NULL) left->insert(val_f);
                else left = new node(val_f, NULL, NULL);
            }
        }
        // Return slot filled
        int traverse(int* array, int index){
            int i = index;
            if (left != NULL) i = left->traverse(array, i) + 1;
            array[i] = val;
            // cout << i << endl;
            if (right != NULL) i = right->traverse(array, i + 1);
            return i;
        }
    };
    node* root = new node(array[0], NULL, NULL);
    int n = SIZE;
    for(int i = 1; i < n; i++){
        root->insert(array[i]);
    }
    // cout<<endl<<root->val<<" "<<root->right->val<<" "<<root->left->val;
    root->traverse(array,0);
    return array;
}

int partition(int* array, int start, int end){
    if (start >= end) return start;
    int pivot = start;
    int left = start + 1;
    int right = end;
    while (left <= right){
        if (array[left] > array[pivot] && array[right] < array[left]) swap(array, left, right);
        if (array[left] <= array[pivot]) left += 1;
        if (array[right] >= array[pivot]) right -= 1;
    }
    swap(array,pivot, right);
    return right;
}

int* quicksort(int* array, int start, int end){
    if (start >= end) return array;
    int pivot = partition(array, start, end);
    quicksort(array, start, pivot - 1);
    quicksort(array, pivot + 1, end);
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
    cout << "Result of MergeSort:";
    print_array(merge_sort(copy_array(numbers), SIZE));
    cout << "Result of TreeSort:";
    print_array(tree_sort(copy_array(numbers)));
    cout << "Result of Quicksort:";
    print_array(quicksort(copy_array(numbers), 0, SIZE - 1));
    return 0;
}
