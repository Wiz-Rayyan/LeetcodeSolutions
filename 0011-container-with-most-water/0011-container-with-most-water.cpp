class Solution {
public:
    int maxArea(vector<int>& height) {
        int hl = height[0];
        int hx = height[height.size()-1];
        int il = 0;
        int ix = height.size()-1;
        if(hx < hl){
            hl = hx;
            il = ix;
            hx = height[0];
            ix = 0;
        }
        int w = height.size() - 1;
        int areax = hl*w;

        while(w > 0){
            int i = il;
            while(height[i] <= hl){
                if(il < ix)
                 i++;
                else
                 i--;
                w--;
                if(w < 1)
                break;
            

            }
            if(height[i] > hx){
                hl = hx;
                il = ix;
                ix = i;
                hx = height[i];
            
            }
            else{
                il = i;
                hl = height[i];
            }
            areax = max(areax, w*hl);
        }
        return areax;
    }
};