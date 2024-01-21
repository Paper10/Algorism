
class Solution {
    public int[] solution(String s) {
        int[] answer = {0,0};
        String str = s;
        while(true){
            
            answer[0] += 1;
            
            String result = "";
            for (int i = 0; i < str.length(); i++) {
                char ch = str.charAt(i);
                if (ch != '0') { result += ch; }
            }
            if(result!=str){ answer[1] += str.length()-result.length(); }
            if(result.length()==1){ return answer; }
            str = result;
            
            str = Integer.toBinaryString(str.length());
            
        }
    }
}


//----------------------------------------------
//문제 분야 : 자바 연습
//https://school.programmers.co.kr/learn/courses/30/lessons/70129
