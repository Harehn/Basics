package structures;

public class LinkedList {
	public Node head;
	
	public LinkedList(Node head) {
		this.head = head;
	}
	
	public LinkedList(){
		this.head = null;
	}
	
	public Node get(int index){
		return this.getNode(index, this.head);
	}
	
	private Node getNode(int i, Node node){
		if(i == 0){
			return node;
		}
		if(node == null){
			return null;
		}
		return this.getNode(i-1, node.next);
	}
	
	public void insert(Node n){
		if (this.head == null){
			this.head = n;
		} else{
			this.head.insertLast(n);
		}
	}
	
	public void insert(int v){
		this.insert(new Node(v));
	}
	
	public void output(){
		int index = 0;
		Node n = this.get(index); 
		while(n != null){
			System.out.println(n.value);
			index++;
			n = this.get(index);
		}
	}

	public class Node{
		public int value;
		public Node next;
		
		public Node(int value, Node next) {
			this.value = value;
			this.next = next;
		}

		public Node(int value) {
			this.value = value;
			this.next = null;
		}
		
		public void insert(Node n){
			n.next = this.next;
			this.next = n;
		}
		
		public void insertLast(Node n){
			if (this.next == null){
				this.insert(n);
			} else {
				this.next.insertLast(n);
			}
		}
	}
}
