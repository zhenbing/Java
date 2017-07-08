package cn.cnic.gscloud;

public class Node {
	private double data;
	private Node pre;
	private Node next;
	
	public Node(Node pre, double data, Node next){
		this.pre = pre;
		this.data = data;
		this.next = next;
	}
	
	public double getData(){
		return this.data;
	}
	
	public Node getNext(){
		return this.next;
	}
	
	public Node getPre(){
		return this.pre;
	}
	
	public void setPre(Node nodepre){
		this.pre = nodepre; 
	}
	
	public void setNext(Node nodenext){
		this.next = nodenext;
	}
	
}
