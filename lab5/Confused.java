public class Confused {
    public static void main(String args[]) {
	System.out.println(indecision());
    } //void main

    private static boolean indecision() {
	try {
	    return true;
	} //try
	finally {
	    return false;
	} //finally
    } //indecision()
} //class confused
