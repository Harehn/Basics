package structures;
import java.util.Random;
import Sorting.Sort;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		LinkedList l = new LinkedList();
		for(int i = 0; i<10; i++){
			l.insert(i);
		}
		//l.output();
		int[][] partitionedList;
		int[] sortedList;
		int[] unsortedList = Sort.makeList(10);
		
//		int[] sortedList = Sort.treeSort(Sort.makeList(20));
//		System.out.println(Arrays.toString(sortedList));
	    
		sortedList =Sort.mergeSort(unsortedList);
//		sortedList = Sort.join(new int[][]{unsortedList,{1223}, unsortedList});
		
		partitionedList = Sort.partition(unsortedList);
	    System.out.println(Arrays.toString(unsortedList));
	    System.out.println(Arrays.toString(sortedList));
//	    System.out.println(Arrays.toString(partitionedList[0]));
//	    System.out.println(Arrays.toString(partitionedList[1]));
//	    System.out.println(Arrays.toString(partitionedList[2]));
	}

}
