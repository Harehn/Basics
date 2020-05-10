#include <stdio.h>

void main(){
    // VARIABLES
    int integer = 1;
    float real = 1.0;
    char character = 'c';
    char* string = "Hello world";
    int arr[3] = {1,2,3};

    // ARITHMETIC
    integer = ( integer + 3 ) / (2 * 3);

    // PRINTING
    printf("Hello World \n");

    // USER INPUT
    scanf("%s", string);
    //printf("%s \n", string);

    // LOGIC
    if (integer == 1){
        integer++;
    }

    for (int i=0; i<10; i++){
        printf("%d", i);
    }
}
