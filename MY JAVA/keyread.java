import java.lang.*;
import java.util.*;

public class keyread
{
    public static void main (String args[])
    {
        Scanner S= new Scanner(System.in);
        float a,b,c;
        System.out.println("Enter 2 Numbers");
           a=S.nextFloat();
           b=S.nextFloat();
           c=a+b;
        System.out.println("Sum is"+c);    
    }
}