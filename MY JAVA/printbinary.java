import java.lang.*;
import java.util.*;


public class printbinary 
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);

        sc.useRadix(2);
        int X=sc.nextInt();

        System.out.println(X);
    }
}