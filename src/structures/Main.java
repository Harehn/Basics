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
		
		int[] sortedList = Sort.treeSort(Sort.makeList(20));
		System.out.println(Arrays.toString(sortedList));
	}

}
