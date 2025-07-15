import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.util.Random;
import java.util.Scanner;



interface MyLambda {
    void foo();
 }

public class Syntax {
//  public int x;
 
  public static void main(String[] args) {
    //1..0 Variables
	//1..1 Comments
    /*
     * Multi-line comment
    */
	
	//1..2 Variable Types
	int x;
    String s = "";
    float y;
    char c;
	
    //1..3 Operations 
    int example = (1 + 2) * 3 / 2;
	s = s + "Java Programming";  
    
    //1..4 Type Casting
    int intfromfloat = (int) 12.9;
    float floatfroint = (float) 12;
	  
    //1..5 Arrays
    int[] arr={1,2,3};
    int firstElement = arr[0];
    int lastElement = arr[arr.length - 1];
    boolean isEmpty = arr == null || arr.length == 0;
    
//	Syntax syn = new Syntax(0, null, 0);
//    syn.getX();
    
    //1..7 Getting Types
    Syntax ex = new Syntax(12, "Example", 12);
    if(arr instanceof int[] || ex.getClass() == Syntax.class || Syntax.class.isInstance(ex)){
    	//TODO
    }

    //2..0 Input / Output
    //2..1 Printing
    System.out.println("Printing");
    PrintStream ss = System.out;
    ss.print("Shortcut");
    
    //2..2 User Input
    Scanner in = new Scanner(System.in);
    System.out.println("Enter a String:");
    String str = in.nextLine();
    System.out.println("You entered string "+str);
//    int a = in.nextInt();
//    System.out.println("You entered integer "+a);
//    float b = in.nextFloat();
//    System.out.println("You entered float "+b);
    
    //2..3 Console Input
    System.out.println(args);
    
    //2..4 File IO
    String msg = "Hello World!";
    try {
      FileOutputStream out = new FileOutputStream("test.txt");
      out.write(msg.getBytes());
      String read_txt = "";
      FileInputStream in_file = new FileInputStream("test.txt");
      read_txt = new String(in_file.readAllBytes());
      System.out.println(read_txt);
    } catch (IOException e) {
      e.printStackTrace();
    }

    
    // 3..0 LOGIC
    if(example != 0) {
      example++;
    }else {
    	example = 0;
    }
    int[] examples = {1,2,3,4};
    for(int i: examples) {
      System.out.println(i);
    }
    
    for(int i=0;i<10;i++) {
      example++;
    }
    int i = 0;
    while(i<10) {
      i++;
    }
    for(int j: examples) {
    	if(j%2 == 0)
    		System.out.println("Even");
    }   
    //Try Catch
    try{
    	throw new Exception("Just kidding");
    }catch(Exception e){
    	System.out.println(e.getMessage());
    }
    //switch case
    int day = 6;
    switch(day){
        case 5:
            System.out.println("\nIt is Saturday\n");
            break;
        case 6:
        	System.out.println("\nIt is Sunday\n");
            break;
        default:
        	System.out.println("\nIt is not yet the weekend :/\n");
    }
    // Ternary operator
    int is_even = 12 % 2 == 0 ? 11: 13;
        
    //6..0 RANDOMNESS
    Random myRandom=new Random();
    System.out.print(myRandom.nextInt(10) + 1);
     
    //4..3 Lambda
    MyLambda fun = () -> System.out.println("Goodbye Cruel World");
    fun.foo();
  }

  //4..0 FUNCTION
  public static int singular(int x1) {
    return 1;
  }
  
  //HIGHER ORDER FUNCTION
  public static void doStuff(MyLambda action){
	  action.foo();
  }
  
  //Function overloading
  // No default arguments
  public static void doStuff(int val) {
	  System.out.println(val);
  }
  
  public int x;
  public Syntax(int x, String s, float y) {
	    super();
	    this.x = x;
	  }
	  /**
	   * JavaDoc 
	   * get X
	   * @return x
	   */
	  public int getX() {
	    return x;
	  }
	  /**
	   * set X to x
	   * @param x
	   */
	  public void setX(int x) {
	    this.x = x;
	  }

	  public class Syntax2 extends Syntax{

		public Syntax2(int x, String s, float y) {
			super(x, s, y);
		}
		  
	  }
}

