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
  
  public static int[] bubbleSort(int[] arr0) {
    int[] arr = cloneList(arr0);
    for(int i = 0; i < arr.length; i++) {
      for(int j = i; j < arr.length; j++) {
        if(arr[i] > arr[j]) {
          int temp = arr[j];
          arr[j] = arr[i];
          arr[i] = temp;
        }
      }
    }
    return arr;
  }
  
  public static int[] selectionSort(int[] arr0) {
    int[] arr = cloneList(arr0);
    for(int i = 0; i < arr.length - 1; i++) {
      int min = arr[i];
      int minIndex = i;
      for(int j = i; j < arr.length; j++) {
        if(min > arr[j]) {
          min = arr[j];
          minIndex = j;
        }
      }
      int temp = arr[minIndex];
      arr[minIndex] = arr[i];
      arr[i] = temp;
    }
    return arr;
  }
  
  public static int[] makeList(int n) {
    Random myRandom=new Random();
    int[] randomList = new int[n];
    for(int i = 0; i < n; i++){
       randomList[i] = myRandom.nextInt(100);
    }
    return randomList;
  }
  
  public static int[] cloneList(int[] arr0) {
    int[] arr = new int[arr0.length];
    for(int i = 0; i < arr.length; i++) {
      arr[i] = arr0[i];
    }
    return arr;
  }
}
