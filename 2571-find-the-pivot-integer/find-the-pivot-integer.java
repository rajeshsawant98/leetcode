class Solution {
    public int pivotInteger(int n) {
      
        double x2= (n*(n+1))/2;
        double sr=  Math.sqrt(x2);
        int x= (int)Math.round(sr);
        if(sr==x)
        return x;
        else
        return -1;
        
    }
}