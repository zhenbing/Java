package cn.cnic.gscloud;

public class Compute {
	public static double average(Node first){
		double sum=0;
		int count=0;
		double average = 0;
		
		Node node = first;
		if(node == null){
			return average;
		}
		
		while(node != null){
			sum += node.getData();
			count++;
			node = node.getNext();
		}
		average = sum/count;
		return average;
		
	}
	
	public static double maximum(Node first){
		double max=Double.MIN_VALUE;
		
		Node node = first;
		if(node == null){
			return max;
		}
		
		while(node != null){
			if(node.getData()>max){
				max = node.getData();
			}
			node = node.getNext();
		}
		return max;
	}
}
