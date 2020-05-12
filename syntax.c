#include <stdio.h>
#include <stdlib.h>

int fact(int num){
    return num<2?1:num*fact(num-1);
}

int main(int argc, char **argv){
    // VARIABLES
    int integer = 1;
    float real = 1.0;
    char character = 'c';
    char* string = "Hello world";
    char str[] = "";
    int arr[3] = {1,2,3};

    // ARITHMETIC
    integer = ( integer + 3 ) / (2 * 3);

    // PRINTING
    printf("Hello World \n");

    // USER INPUT
    printf("Enter a string \n");
    scanf("%s", str);
    printf("%s \n", str);

    // CMD INPUT
    if(argc>1){
        printf(argv[1]);
    }

    // LOGIC
    if (integer == 1){
        integer++;
    }

    for (int i=0; i<10; i++){
        printf("%d! is %d \n", i, fact(i));
    }


    return 1;
}
