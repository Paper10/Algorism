
class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        for(int i=0;i<signs.length;i++){
            if(signs[i]){
                answer += absolutes[i];
            }
            else{
                answer -= absolutes[i];
            }
        }
        return answer;
    }
}


//----------------------------------------------
//문제 분야 : 자바 연습
//https://school.programmers.co.kr/learn/courses/30/lessons/76501
