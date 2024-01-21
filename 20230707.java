
class Solution {
    public int solution(int n) {
        int answer = 0;
        int tmp = n;
        while(tmp>0){
            answer += tmp%10;
            tmp /= 10;
        }

        return answer;
    }
}



//----------------------------------------------
//문제 분야 : 자바 연습
//https://school.programmers.co.kr/learn/courses/30/lessons/87389
