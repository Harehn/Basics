#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

// 4..0 FUNCTIONS
int fact(int num){
    return num<2?1:num*fact(num-1);
}

// 4..2 Higher Order Functions
void func(int nb, void (*f)(int)) {
    int i;
    for (i = 0; i < nb; i++) f(i);
}

void callback(int v) {
    printf("%d\n", v);
}

// 1.. Structs
struct Books {
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
} book;


int main(int argc, char **argv){
    // 1..0 VARIABLES
	// Comments
	/* 
	* Multiline comment
	*/
    int integer = 1;
    float real = 1.0;
    char character = 'c';
    char* string = "Hello world";
    char str[] = "";
	// bool daytime = false; No boolean in C
	// Operation
	integer = ( integer + 3 ) / (2 * 3);
	//Type casting
	float cast1 = (float) integer;
    int cast2 = (int) real;
	
	// Array
    int arr[3] = {1,2,3};
    
	// Other structures
	// Structs
	struct Books b = {"Trial", "Baby", "Ice Ice", 1234};
    printf("%d \n", b.book_id);
    /*printf(b.title, "\n");*/
	short small = 1;
	long bigger = 345678;
	uint8_t positive = 12;
	int* ptr = &integer;
	
	int extra_int = 1;
    ptr = (int*) malloc(sizeof(int));
    printf("\n%p", ptr);
    free(ptr);
    printf("\n%p", ptr);

	enum level{LOW, MEDIUM, HIGH};//Evaluates to 0, 1, 2
    enum places{
        START = 12,
        START2, // Now 13
        END // Now 14
    };
	union place_in_race{
        int position;
        char error;
    }good_place;
	// Cannot get variable types in C without compiler extensions

    // 2..0 INPUT/OUTPUT
    // 2..1 Printing
	printf("Hello World %d \n", 123);
    // 2..2 User Input
    printf("Enter a string \n");
    scanf("%s", str);
    printf("%s \n", str);
    // 2..3 Console Input
    if(argc>1){
        printf("%s",argv[1]);
    }
	// 2..4 File IO
	FILE *file;
    file = fopen("test.txt", "w+");
    fprintf(file, "Fprint to write to file\n");
    fputs("fputs to write to file\n", file);
    fclose(file);

    // 3..0 LOGIC
    // 3..1 For loop
	for (int i=0; i<10; i++){
        printf("%d! is %d \n", i, fact(i));
    }
	// 3..2 While loop
    int counter = 10;
    while(counter > 0){
        counter--;
    }
	// 3..3 If else
	if (integer == 1){
        integer++;
    }
	// Combination
	int odd_numbers = 0;
    for (int i=0; i<10; i++){
        if(i%2 ==0){
			odd_numbers ++;
        }
    }
	
    // Switch Case
	int day = 6;
    switch(day){
        case 5:
            printf("\nIt is Saturday\n");
            break;
        case 6:
            printf("\nIt is Sunday\n");
            break;
        default:
            printf("\nIt is not yet the weekend :/\n");
    }
	
	// Ternary operator
	int num = 3;
	num = num<2?1:num;
	// 4..0 Function
	func(4, callback); // Stack smashing in this situation but not when done separately
	// No lambdas , no default arguments, no overloading functions in C
	
    srand(time(NULL));   // Initialization, should only be called once.
    int r = rand();      // Returns a pseudo-random integer between 0 and RAND_MAX.
    printf("%d", r);

    return 1;
}