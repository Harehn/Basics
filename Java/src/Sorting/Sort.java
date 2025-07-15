package Sorting;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
//import structures.Tree;

public class Sort {
  public static class Tree{
	  public int val;
	  public Tree left;
	  public Tree right;
	  public Tree(int val_f) {this.val=val_f;this.left=null;this.right=null;}
	  public void insert(int val_f) {
		  if (this.val < val_f) {
			  if (this.right != null) this.right.insert(val_f);
			  else this.right = new Tree(val_f);
		  }else {
			  if (this.left != null) this.left.insert(val_f);
			  else this.left = new Tree(val_f);
		  }
	  }
	  public int traverse(int[] arr, int index) {
		  int i = index;
          if (this.left != null) i = this.left.traverse(arr, i) + 1;
          arr[i] = val;
          if (this.right != null) i = this.right.traverse(arr, i + 1);
          return i;
	  }
  }
  public static int[] treeSort(int[] arr) {
    Tree t = null;
    for (int i:arr) {
    	if (t == null) t = new Tree(i);
    	else t.insert(i);
    }
    int[] new_arr = new int[20];
    t.traverse(new_arr, 0);
    return new_arr;
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
  
  public static int[] quickSort(int[] arr) {
    if(arr.length < 2) {
      return arr;
    }
    int[][] arrs = partition(arr);
    int[] lessList  = arrs[0];
    int[] pivotList  = arrs[1];
    int[] moreList  = arrs[2];
    return join(new int[][] {quickSort(lessList), pivotList, quickSort(moreList)});
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
  
  public static int[] mergeSort(int[] arr) {
    if(arr.length < 2) {
      return arr;
    }
    int[][] arrs = split(arr);
    int[] list1 = arrs[0];
    int[] list2 = arrs[1];
    return mergejoin(mergeSort(list1), mergeSort(list2));
    
  }
  public static int[][] split(int[] arr){
    int length1 = arr.length/2;
    int length2 = arr.length -length1;
    int[] list1 = new int[length1];
    int[] list2 = new int[length2];
    
    for(int i = 0; i < length1; i++) {
      list1[i] = arr[i];
    }
    for(int i = 0; i < length2; i++) {
      list2[i] = arr[length1 + i];
    }
    return new int [][] {list1,list2};
  }
  
  public static int[] mergejoin(int[] list1,int[] list2){
    int[] result = new int[list1.length + list2.length];
    int length1 = list1.length;
    int length2 = list2.length;
    for(int i = 0; i < result.length; i++) {
      // Get current
      int list1val = length1<=0 ? Integer.MAX_VALUE : list1[list1.length -length1];
      int list2val = length2<=0 ? Integer.MAX_VALUE : list2[list2.length -length2];
      
      // Compare and set
      if(list1val < list2val) {
        result[i] = list1val;
        length1--;
      }else {
        result[i] = list2val;
        length2--;
      }
    }
    return result;
  }
  
  public static int[] makeList(int n) {
    Random myRandom=new Random();
    int[] randomList = new int[n];
    for(int i = 0; i < n; i++){
       randomList[i] = myRandom.nextInt(10000);
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
  
  public static String listToString(int[] arr) {
	  String to_return = "[";
	  for (int num: arr) {
		  to_return += num + ", ";
	  }
	  return to_return+"]";
  }
  
  public static void heapify(int[] arr, int size, int index) {
	  int largest = index;
	  int left = 2 * index + 1;
	  int right = 2 * index + 2;
	  if (left < size && arr[left] > arr[largest]) largest = left;
	  if (right < size && arr[right] > arr[largest]) largest = right;
	  if (largest != index) {
		  int temp = arr[index];
		  arr[index] = arr[largest];
		  arr[largest] = temp;
		  heapify(arr, size, largest);
	  }
  }
  
  public static int[] heapSort(int[] arr) {
	  for(int i = arr.length/2 - 1; i>=0; i--) heapify(arr, arr.length, i);
	  for(int i = arr.length - 1; i > 0; i--) {
		  int temp = arr[0];
		  arr[0] = arr[i];
		  arr[i] = temp;
		  heapify(arr, i, 0);
	  }
	  return arr;
  }
  
  public static void main(String[] args) {
	int[] numbers = makeList(20);
	System.out.println("Original array: " + listToString(numbers));
	System.out.println("BubbleSort result: " + listToString(bubbleSort(cloneList(numbers))));
	System.out.println("SelectionSort result: " + listToString(selectionSort(cloneList(numbers))));
	System.out.println("InsertionSort result: " + listToString(insertionSort(cloneList(numbers))));
	System.out.println("MergeSort result: " + listToString(mergeSort(cloneList(numbers))));
	System.out.println("QuickSort result: " + listToString(quickSort(cloneList(numbers))));
	System.out.println("TreeSort result: " + listToString(treeSort(cloneList(numbers))));
	System.out.println("HeapSort result: " + listToString(heapSort(cloneList(numbers))));
  }
  
}
