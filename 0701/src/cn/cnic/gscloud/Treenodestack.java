package cn.cnic.gscloud;

public class Treenodestack {
	public TreeNode[] stack = new TreeNode[16];
	public int top = -1;
	
	public void push(TreeNode treenode){
		top++;
		stack[top]=treenode;
	}
	
	public TreeNode pop() throws Exception{
		if(top == -1){
			throw new Exception("There is no element in the stack!!");
		}
		TreeNode treenode = this.stack[top];
		top--;
		return treenode;
	}

}
