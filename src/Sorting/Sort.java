package Sorting;
import java.util.ArrayList;
import java.util.Random;
import structures.Tree;

public class Sort {
  public static int countSortMaximum = 100;
  
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
   
  public static int[] insertionSort(int[] arr0) {
    int[] arr = new int[arr0.length];
    int length = -1;
    for(int newVal : arr0) {
      length++;
      boolean inserted = false;
      
      //insert in arr
      for(int j = 0; j < length; j++) {
        if(newVal < arr[j]) {
          for(int shift = length; shift > j;shift--) {
            arr[shift] = arr[shift -1]; 
          }
          arr[j] = newVal;
          inserted = true;
          break;
        }
      }
      
      if(! inserted) {
        arr[length] = newVal;
      }
    }
    return arr;    
  }
  
  public static int[] quicksort(int[] arr) {
    if(arr.length < 2) {
      return arr;
    }
    int[][] arrs = partition(arr);
    int[] lessList  = arrs[0];
    int[] pivotList  = arrs[1];
    int[] moreList  = arrs[2];
    return join(new int[][] {quicksort(lessList), pivotList, quicksort(moreList)});
  }
  
  public static int[][] partition(int[] arr){
    int pivot = arr[0];
    int morelength = 0;
    int lesslength = 0;
    for(int i = 1; i < arr.length; i++) {
      if(arr[i] < pivot) {
        lesslength++;
      }else {
        morelength++;
      }
    }
    int[] moreList = new int[morelength];
    int[] lessList = new int[lesslength];
    int[] pivotList = {pivot};
    for(int i = 1; i < arr.length; i++) {
      if(arr[i] < pivot) {
        lessList[lesslength -1] = arr [i];
        lesslength--;
      }else {
        moreList[morelength - 1] = arr[i];
        morelength--;
      }
    }
    return new int[][]{lessList,pivotList,moreList};
  }
  
  public static int[] join(int[][] arrs) {
    int[] joinedList = new int[arrs[0].length + arrs[2].length + 1];
    for(int i = 0;  i < arrs[0].length; i++) {
      joinedList[i] = arrs[0][i];
    }
    joinedList[arrs[0].length] = arrs[1][0];
    for(int i = 0;  i < arrs[2].length; i++) {
      joinedList[arrs[0].length + 1 + i] = arrs[2][i];
    }
    return joinedList;
  }
  
  public static int[] countSort(int[] arr0) {
    int[] counts = new int[countSortMaximum];
    int[] sortedList =new int[arr0.length];
    for(int i: arr0) {
      counts[i]++;
    }
    for(int i = 1; i< counts.length; i++) {
      counts[i]+=counts[i-1];
    }
    for(int i:arr0) {
      sortedList[counts[i]-1] = i;
      counts[i]--;
    }
    return sortedList;
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
