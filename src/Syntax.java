import java.util.Scanner;

//1..0 OBJECTS
//Everything is an object
public class Syntax {
  public int x;
  public String s;
  public float y;
  
  public Syntax(int x, String s, float y) {
    super();
    //
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
  
  //2..0 FUNCTION
  public static int singular(int x1) {
    return 1;
  }


  public static void main(String[] args) {
    Syntax syn = new Syntax(0, null, 0);
    syn.getX();
    
    
    int example = (1 + 2) * 3 / 2;
    if(example != 0) {
      example++;
    }
    
    int[] examples = {1,2,3,4};
    for(int i: examples) {
      System.out.println(i);
    }
    
    for(int i=0;i<10;i++) {
      example++;
    }
    
    Scanner in = new Scanner(System.in);
    String s = in.nextLine();
    System.out.println("You entered string "+s);
    int a = in.nextInt();
    System.out.println("You entered integer "+a);
    float b = in.nextFloat();
    System.out.println("You entered float "+b);
  }

}
