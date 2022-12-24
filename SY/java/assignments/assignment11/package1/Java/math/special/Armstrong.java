package package1.Java.math.special;

public class Armstrong {
    public boolean isArmstrong(int number){
        int result = 0;
        int orig = number;
        while(number != 0){
            int remainder = number%10;
            result = result + remainder*remainder*remainder;
            number = number/10;
        }
        //number is Armstrong return true
        if(orig == result){
            return true;
        }
        return false;
    }
}
