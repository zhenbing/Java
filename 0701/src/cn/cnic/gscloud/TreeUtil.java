package cn.cnic.gscloud;

public class TreeUtil {
	public static void preOrder(TreeNode root){
		if(root!=null){
			System.out.println(root.getData());
			preOrder(root.getLeft());
			preOrder(root.getRight());
		}
		
	}
	
	public static void midOrder(TreeNode root){
		if(root!=null){
			midOrder(root.getLeft());
			System.out.println(root.getData());
			midOrder(root.getRight());
		}
		
	}
	
	public static void postOrder(TreeNode root){
		if(root!=null){
			postOrder(root.getLeft());
			postOrder(root.getRight());
			System.out.println(root.getData());
		}
	}
}
