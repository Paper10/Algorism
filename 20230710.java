
class Solution {
    public int[] solution(long n) {
        int[] answer = {};
        long t = n;
        while(t>0){
            
            int[] arr = new int[answer.length + 1];
            System.arraycopy(answer, 0, arr, 0, answer.length);
            arr[answer.length] = (int)(t%10);
            answer = arr;
            t /= 10;
        }
        
        
        return answer;
    }
}


//----------------------------------------------
//문제 분야 : 자바 연습
//https://school.programmers.co.kr/learn/courses/30/lessons/12932
