#include <stdio.h>
#include <stdlib.h>

#include <time.h>
#include <stdlib.h>

// 1..0 FUNCTIONS
int fact(int num){
    return num<2?1:num*fact(num-1);
}

// 2..0 OBJECTS
struct Books {
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
} book;

int main(int argc, char **argv){
    // 3..0 VARIABLES
    int integer = 1;
    float real = 1.0;
    char character = 'c';
    char* string = "Hello world";
    char str[] = "";
    int arr[3] = {1,2,3};
    struct Books b = {"Trial", "Baby", "Ice Ice", 1234};
    printf("%d \n", b.book_id);
    float cast1 = (float) integer;
    int cast2 = (int) real;
    /*printf(b.title, "\n");*/

    // 4..0 ARITHMETIC
    integer = ( integer + 3 ) / (2 * 3);

    // 5..0 PRINTING
    printf("Hello World \n");

    // 6..0 USER INPUT
    printf("Enter a string \n");
    scanf("%s", str);
    printf("%s \n", str);

    // 7..0 CMD INPUT
    if(argc>1){
        printf(argv[1]);
    }

    // 8..0 LOGIC
    if (integer == 1){
        integer++;
    }

    for (int i=0; i<10; i++){
        printf("%d! is %d \n", i, fact(i));
    }

    int counter = 10;
    while(counter > 0){
        counter--;
    }
    for (int i=0; i<10; i++){
        if(i%2 ==0){

        }
    }





    srand(time(NULL));   // Initialization, should only be called once.
    int r = rand();      // Returns a pseudo-random integer between 0 and RAND_MAX.
    printf("%d", r);


    return 1;
}