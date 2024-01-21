
import java.util.ArrayList;

class Solution
{
    public int solution(String s)
    {

        ArrayList<Character> stack = new ArrayList<>();
        
        for (int i = 0; i<s.length() ; i++){
            char c = s.charAt(i);
            if(stack.isEmpty()){
                stack.add(c);
            }
            else if(stack.get(stack.size()-1)==c){
                stack.remove(stack.size()-1);
            }
            else{
                stack.add(c);
            }
            
        }

        if(stack.isEmpty()){ return 1; }
        else{ return 0; }
    }
}


//----------------------------------------------
//문제 분야 : 자바 연습
//https://school.programmers.co.kr/learn/courses/30/lessons/12973
