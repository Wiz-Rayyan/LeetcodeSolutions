//gives nth fabonnaci number
class Solution {
    public int fib(int n) {
        if (n==0){
            return 0 ;
        }else if (n==1){
            return 1 ;
        }
        int term1 = 0;
        int term2 = 1;
        int term3 = 2;

        for(int i=1; i<=n; i++){
             term3 = term1 + term2;
            term1 = term2;
            term2 = term3;

        }
        return term1; // term2 & 3 shall return 1,2,3,5,8 instead of 1,1,2,3,5
    }
}