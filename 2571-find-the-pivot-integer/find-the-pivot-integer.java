class Solution {
    public int pivotInteger(int n) {
      
        double x2= (n*(n+1))/2;
        int x=  (int)Math.sqrt(x2);
        
        if(x*x==x2)
        return x;
        else
        return -1;
        
    }
}