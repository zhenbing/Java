package cn.cnic.gscloud;

public class Stack {
	public char[] stack=new char[16];
	public int top = -1;
	
	public void push(char element){
		top ++;
		stack[top]=element;
		
	}
	
	public char pop() throws Exception {
		if(top == -1){
			throw new Exception("There is no element in the stack!!");
		}
		char element = stack[top];
		top--;
		return element;
	}

}
