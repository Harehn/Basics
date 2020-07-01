import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.util.Random;
import java.util.Scanner;

//1..0 OBJECTS
//Everything is an object
public class Syntax {
  public int x;
  public String s;
  public float y;
  public int[] arr;
  public char c;
  
  public Syntax(int x, String s, float y) {
    super();
    //2..0 VARIABLE TYPES
    this.x = x;
    this.s = s;
    this.y = y;
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
  public String getS() {
    return s;
  }
  public void setS(String s) {
    this.s = s;
  }
  public float getY() {
    return y;
  }
  public void setY(float y) {
    this.y = y;
  }
  
  public static void main(String[] args) {
    Syntax syn = new Syntax(0, null, 0);
    syn.getX();
    
    // GETTING TYPES
    Syntax ex = new Syntax(12, "Example", 12);
    if(ex.arr instanceof int[] || ex.getClass() == Syntax.class || Syntax.class.isInstance(ex)){
    	//TODO
    }
    
    //TYPE CASTING
    int intfromfloat = (int) 12.9;
    float floatfroint = (float) 12;
    
    
    
   //2..1 ARITHMETIC 
    int example = (1 + 2) * 3 / 2;
    
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
   
    
    //4..0 PRINTING
    System.out.println("Printing");
    PrintStream ss = System.out;
    ss.print("Shortcut");
    
    
    //5..0 USER INPUT
    Scanner in = new Scanner(System.in);
    String s = in.nextLine();
    System.out.println("You entered string "+s);
    int a = in.nextInt();
    System.out.println("You entered integer "+a);
    float b = in.nextFloat();
    System.out.println("You entered float "+b);
    
    
    //6..0 RANDOMNESS
    Random myRandom=new Random();
    System.out.print(myRandom.nextInt(10) + 1);
    
    //7..0 FILE IO
    String msg = "";
    try {
      FileOutputStream out = new FileOutputStream("C:\\Users\\Candy\\Desktop\\SaboteurComp424\\src\\autoplay\\output.txt");
      out.write(msg.getBytes());
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  //8..0 FUNCTION
  public static int singular(int x1) {
    return 1;
  }
}

