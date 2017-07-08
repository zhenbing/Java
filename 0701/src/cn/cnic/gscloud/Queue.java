package cn.cnic.gscloud;

public class Queue {
	class Node{
		private TreeNode data;
		private Node next;
		
		public TreeNode getData() {
			return data;
		}
		public void setData(TreeNode data) {
			this.data = data;
		}
		public Node getNext() {
			return next;
		}
		public void setNext(Node next) {
			this.next = next;
		}
	}
	
	private Node qdata;
	private Node front;
	private Node rear;
	public Node getQdata() {
		return qdata;
	}
	public void setQdata(Node qdata) {
		this.qdata = qdata;
	}
	public Node getFront() {
		return front;
	}
	public void setFront(Node front) {
		this.front = front;
	}
	public Node getRear() {
		return rear;
	}
	public void setRear(Node rear) {
		this.rear = rear;
	}
	
	public void enQueue(Node node){
		Node rearNode = this.getRear();
		rearNode.setNext(node);
		this.setRear(node);
		if(this.front==null){
			this.front = node;
		}
	}
	
	public Node deQueue(){
		Node deNode = this.front;
		this.setFront(deNode.getNext());
		return deNode;
	}
	
}
