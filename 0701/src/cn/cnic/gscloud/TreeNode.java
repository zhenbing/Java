package cn.cnic.gscloud;

public class TreeNode {
	private String data;
	private TreeNode left;
	private TreeNode right;
	
	public TreeNode( TreeNode left, String data,TreeNode right){
		this.data = data;
		this.left = left;
		this.right = right;
	}
	
	public String getData(){
		return this.data;
	}
	
	public TreeNode getLeft(){
		return this.left;
	}
	
	public TreeNode getRight(){
		return this.right;
	}
	
	public void setLeft(TreeNode left){
		this.left = left;
	}
	
	public void setRight(TreeNode right){
		this.right = right;
	}
}
