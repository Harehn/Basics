package Sorting;
import java.util.ArrayList;
import java.util.Random;
import structures.Tree;

public class Sort {
  public static int[] treeSort(int[] arr) {
    Tree t = new Tree();
    for (int i:arr) {
      t.insertInOrder(i);
    }
    ArrayList<Integer> complexArr = t.traverse();
    int[] simpleArr = new int[complexArr.size()];
    int index = 0;
    for(Integer i: complexArr) {
      simpleArr[index] = i.intValue();
      index++;
    }
    return simpleArr;
  }
  
  public static int[] makeList(int n) {
    Random myRandom=new Random();
    int[] randomList = new int[n];
    for(int i = 0; i < n; i++){
       randomList[i] = myRandom.nextInt(100);
    }
    System.out.println(randomList);
    return randomList;
  }
  
}
