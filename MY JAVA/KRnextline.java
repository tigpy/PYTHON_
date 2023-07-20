import java.lang.*;
import java.util.*;

public class KRnextline
{
    public static void main(String args[])
    {
        Scanner S= new Scanner(System.in);

        String name;
        System.out.println("May i Know your name");
        name = S.nextLine(); //Nextline will read multi word and next will read only first word .
        System.out.println("Welcome Mr/Miss"+name); //"+"works as concate.
    }

}
