import java.util.*;
import java.lang.String;

class tr1{
    public static void main(String[] args) {
        String X;
        Scanner sc = new Scanner(System.in);
        X = sc.nextLine();
        String Y = new String();
        Y = X.substring(3,0);
        System.out.println(Y);
        if(X.equalsIgnoreCase(Y))
            System.out.println(X);
        else   
            System.out.println("Not palindrom");
    }
}
