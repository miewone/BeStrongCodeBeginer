import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        
        
        HashMap<Integer,String> hash = new HashMap<>();
    
        for(int i=0;i<numbers.length;i++)
        {
            for(int j=0;j<numbers.length;j++)
            {
                if(i==j)continue;
                hash.put((numbers[i]+numbers[j]),"1");
            }
        }
        int[] answer = new int[hash.size()];
        int size =0;
        for(var a : hash.keySet())
        {
            answer[size++] = a;
        }
        
        Arrays.sort(answer);
        return answer;
    }
}