#include <iostream>
#include <stdint.h>
#include <fstream>

int add(int a, int b);
int add2(int a, int b, int(*func)(int,int));
void logger(int a);
void logger(float a);
void logger(bool a);
void f(int a = 12);


//Command line arguments; see 2.0 INPUT/OUTPUT
int main(int argc, char *argv[]) 
{
    //----- 1.0 VARIABLES------
    //----- 1.1 Comments ------
    /*
    Multiline Comments
    */
    
    //------1.2 Variables -----
    int number = 2;
    float decimal = 3.3;
    std::string message = "Hello World"; //Strings are in the std library
    //String literals can be stored in char* but cannot be changed later
    const char* message2 = "Hello?";
    //The following will give an error because of the missing const
    //char* message2 = "Hello?"; 
    bool happy = true;
    
    //----- 1.3 Operations -----
    int earth_day = (31 - 9) * 100 / 5 - 20;
    float weeks = 31 / 7; //Evaluates to 4 since integer division
    weeks = 31.0 / 7; //Evaluates to 4.4... since 31.0 is a float
    std::string name = "Hello" + std::string(" ") + "Nitin";
    // The following will give an error because both of the first 2 operands are string literals
    //std::string name = "Hello" + " " + "Nitin";
    
    //---- 1.4 TypeCasting -----
    int exact_weeks = int(31.0 / 7.0);
    float accurate_temp = float(27); // No difference
    bool not_zero = bool(123/1234);
    // String conversion is a bit complicated. See: https://stackoverflow.com/questions/5590381/how-can-i-convert-int-to-string-in-c
    std::string to_str = std::to_string(exact_weeks);
    if (not_zero){std::cout << "Not_zero\n";} else {std::cout << "Zero\n";}
    
    //------1.5 Arrays ------
    std::string names[] = {"Patrick", "Bob", "Sandy"};
    int points[4] = {0}; //All numbers initialised to 0
    int coordinates[4][2] = {{1,2}, {3,4}, {4,5}, {5,6}};//(i,j) zero indexed
    int second_x_coordinate = coordinates[1][0];//Value -> 3
    
    //------1.6 Other strutures -----
    int place = 12;
    int* ptr = &place;//Pointer
    int& ref = place;//points to place, any changes to ref will change place
    struct person{
        std::string name;
        int age;
    }first,second;//Created struct first and second
    //No need to name struct type if all structs are declared at the start
    person third;
    person* third_place = &third;
    third_place->age = 19;
    third.name = "Nitin";
    //Unions can only hold one value. size is max of sizes of diff Variables
    //Can declare variables at start of declaration(same as structs)
    //It is not 'possible' 
    union place_in_race{
        int position;
        // std::string error;
        bool error;
    }good_place;
    enum level{LOW, MEDIUM, HIGH};//Evaluates to 0, 1, 2
    enum places{
        START = 12,
        START2, // Now 13
        END // Now 14
    };
    typedef int zahl;
    zahl eins = 1;
    uint8_t small = 1; // Needs the <stdint.h> library
    short small2 = 1;
    long big = 12345;
    
    //----- 1.7 GetVariable Type -------
    std::cout << typeid(place).name();//Outputs i 
    
    
    //------2.0 INPUT/OUTPUT ----------
    std::cout << "\nEnter your name: ";
    std::string x;
    std::cin >> x;
    std::cout << "\nWelcome " << x << std::endl;
    std::cout << "You have entered " << argc - 1 << " arguments.";//Taken from main declaration
    
    std::ofstream MyFile("message.txt");
    MyFile << "dQw4w9WgXcQ" << std::endl;
    MyFile << "We should greet the world with open arms.";
    MyFile.close();
    
    std::string line;
    std::ifstream MyReadFile("message.txt");
    while (getline(MyReadFile, line)) {
      std::cout << std::endl << line;
    }
    MyReadFile.close(); 
    
    //------3.0 LOGIC ----------
    int even = 0;
    int odd = 0;
    //for loop
    for (int i = 0; i < 25; i++){
        if (i % 2 == 0) even += 1;
        else{
            odd ++;
        }
    }
    int total = 0;
    int numbers[5] = {1, 2, 3, 4, 5};
    //for each loop
    for (int i : numbers) {
        total += i;
    }
    //while loop
    while (total >0){
        total -= 10;
    }
    //switch case
    int day = 6;
    switch(day){
        case 5:
            std::cout<<"\nIt is Saturday\n";
            break;
        case 6:
            std::cout<<"\nIt is Sunday\n";
            break;
        default:
            std::cout<<"\nIt is not yet the weekend :/\n";
    }
    //try catch
    try {
        throw 404;
    }
    catch (int errorCode) {
        std::cout << "Error occurred: " << errorCode;
    }
    try {
        int x = 123/12;
    }
    catch (...) {
        std::cout << "Cannot divide by zero!";
    }
    //ternary operator
    int x1 = 1234;
    int x2 = 2345;
    int maximum_number = x1 > x2? x1:x2;
    
    //--------- 4.0 FUNCTIONS ---------
    int total_value = add2(3, 4, add);
    std::cout <<std::endl << total_value <<std::endl;
    // Lambda
    auto logging = [](int values){std::cout << std::endl << values + 1;};
    logging(total_value);
    logger(3);
    logger(2.5f); // float, 2.5 is considered ambiguous, https://stackoverflow.com/questions/34960166/call-of-overloaded-function-is-ambiguous-double-vs-float
    logger(false);
    f();
    return 0;
}

int add(int a, int b){
    return a + b;
}
//Higher Order function
// Alternative way: https://www.w3schools.com/cpp/cpp_functions_lambda.asp
int add2(int a, int b, int(*func)(int,int)){
    return func(a,b);
}
//Function overloading
void logger(int a){
    std::cout << a;
}
void logger(float a){
    std::cout << a;
}
void logger(bool a){
    std::cout << a;
}
//Default arguments
void f(int a){
    std::cout << a;
}