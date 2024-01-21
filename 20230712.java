
class Solution {
    public boolean solution(int x) {
        boolean answer = false;
        
        int sum = 0;
        int t = x;
        while(t>0){
            sum += t%10;
            t /= 10;
        }
        
        if(x%sum==0){
            answer = true;
        }
        
        return answer;
    }
}


//----------------------------------------------
//문제 분야 : 자바 연습
//https://school.programmers.co.kr/learn/courses/30/lessons/12947
