#include <iostream>
#include <stdint.h>
#include <fstream>

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
    int* ptr = &place;
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
    
    return 0;
}