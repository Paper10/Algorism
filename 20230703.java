
class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        double sum = 0;
        for(int i = 0;i<arr.length;i++){
            sum += arr[i];
        }
        answer = sum / arr.length;
        return answer;
    }
}



//----------------------------------------------
//문제 분야 : 자바 연습
//https://school.programmers.co.kr/learn/courses/30/lessons/12944?language=java
