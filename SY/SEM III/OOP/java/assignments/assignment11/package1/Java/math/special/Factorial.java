package package1.Java.math.special;

public class Factorial {
    public int fact(int n){
       if(n==0){
           return 1;
       }
       else{
           return n*fact(n-1);
       }
    }
}
