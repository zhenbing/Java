package cn.cnic.gscloud;

import java.util.*;
import java.util.LinkedList;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Node node1 = new Node(null, 1, null);
//		Node node2 = new Node(node1, 13, null);
//		Node node3 = new Node(node2, 15, null);
//		
//		List<Double> list=new LinkedList<>();
//		List<Double> list1=new ArrayList<>(8);
//		double[] arrays=new double[3];
//		node1.setNext(node2);
//		node2.setNext(node3);
//		
//		double avg = Compute.average(node1);
//		double max = Compute.maximum(node1);
//		
//		System.out.println(avg);
//		System.out.println(max);
		
//		String formula= "3+2*5-6";
//		Stack stack = new Stack();
//		int top = stack.top;
//		char[] arr = stack.stack;
//		
//		int len = formula.length();
//		for(int i=0; i<len; i++){
//			char ele = formula.charAt(i);
//			if(ele>=48 && ele<=57){
//				System.out.println(ele);
//			}
//			else{
//				if(ele =='+' || ele == '-'){
//					if(stack.top==-1){
//						stack.push(ele);
//					}
//					else{
//						if(arr[stack.top]=='*' || arr[stack.top] =='/'){
//							try {
//								System.out.println(stack.pop());
//							} catch (Exception e) {
//								// TODO Auto-generated catch block
//								e.printStackTrace();
//							}
//							stack.push(ele);
//						}
//						else{
//							stack.push(ele);
//						}
//					}
//					
//				}
//				else{
//					stack.push(ele);
//				}
//			}
//			
//		}
//		while(stack.top!=-1){
//			try {
//				System.out.println(stack.pop());
//			} catch (Exception e) {
//				// TODO Auto-generated catch block
//				e.printStackTrace();
//			}
//		}
		
		
		//tree construction
		TreeNode root = new TreeNode(null, "(0,360)", null);
		TreeNode node1 = new TreeNode(null, "(0,180)", null);
		TreeNode node2 = new TreeNode(null, "(180,360)", null);
		root.setLeft(node1);
		root.setRight(node2);
		
		TreeNode node3 = new TreeNode(null, "(0,90)", null);
		TreeNode node4 = new TreeNode(null, "(90,180)", null);
		node1.setLeft(node3);
		node1.setRight(node4);
		
		TreeNode node5 = new TreeNode(null, "(180,270)", null);
		TreeNode node6 = new TreeNode(null, "(270,360)", null);
		node2.setLeft(node5);
		node2.setRight(node6);
		
		TreeUtil.preOrder(root);
		TreeUtil.midOrder(root);
		TreeUtil.postOrder(root);

		System.out.println("............BFS.................");
		Queue q = new Queue();
		Queue.Node r = q.new Node();
		r.setData(root);
		q.setQdata(r);
		q.setFront(r);
		q.setRear(r);
		
		while(q.getFront()!=null){
			Queue.Node outnode = q.deQueue();
			System.out.println(outnode.getData().getData());
			if(outnode.getData().getLeft()!=null){
				Queue.Node outnodel = q.new Node();
				outnodel.setData( outnode.getData().getLeft());
				q.enQueue(outnodel);
			}
			if(outnode.getData().getRight()!=null){
				Queue.Node outnoder = q.new Node();
				outnoder.setData( outnode.getData().getRight());
				q.enQueue(outnoder);
			}
			
			
		}
	}

}
