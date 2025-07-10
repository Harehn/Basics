package structures;
import java.util.ArrayList;

public class Tree {
  public Tree left;
  public Tree right;
  public Integer value;
  
  public Tree() {
    this.left = null;
    this.right = null;
    this.value = null;
  }

  public void insertInOrder(int newVal) {
    //For case of Head
    if(! this.hasValue()) {
      this.value = Integer.valueOf(newVal);
      return;
    }
    if(newVal < value.intValue()) {
      this.initialiseLeft(); //Makes sure it's not null
      this.left.insertInOrder(newVal);
    }else {
      this.initialiseRight(); //Makes sure it's not null
      this.right.insertInOrder(newVal);
    }
  }

  
  public ArrayList<Integer> traverse() {
    ArrayList<Integer> sortedList = new ArrayList<Integer>();
    if(! this.hasValue()) {return sortedList;}
    
    this.initialiseLeft();
    this.initialiseRight();
    
    sortedList.addAll(left.traverse());
    sortedList.add(this.value);
    sortedList.addAll(right.traverse());
    
    return sortedList;
  }
  
  public boolean hasValue() {return this.value != null;}
  public void initialiseLeft() {if(this.left == null) this.left =new Tree();}
  public void initialiseRight() {if(this.right == null) this.right =new Tree();}
  
  
  
}
