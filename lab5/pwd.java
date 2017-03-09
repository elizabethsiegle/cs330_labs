import java.util.*;
import java.lang.*;


public class pwd{
    static Random rd;
    public static void main(String args[]) {
	rd = new Random(System.currentTimeMillis());
	for (int i = 0; i < 5; i++){
	    int len = rd.nextInt(9) + 8;
	    System.out.println("Password " + (i+1) + ", length " + len +": " + passGen(len));
	}
    }

    public static String passGen(int n) {
	char[] arr = new char[n];
	for (int i = 0; i < n; i++){
	    int temp = (rd.nextInt(95) + 32);
	    char c = (char)temp;
	    arr[i] = c;
	}
	return String.valueOf(arr);
    }
}
