import java.nio.charset.Charset;
import java.nio.file.*;
import java.util.*;
import java.io.*;


public class lab6 {
    static HashMap<String, ArrayList<String>> HML;
    public static void main(String[] args) {
	HML = new HashMap<String, ArrayList<String>>();
	preprocess("/usr/share/dict", "words");
	query("Anns");
	query("racecar");
	query("pickle");
    }

    public static void preprocess(String dictFileDir, String FileName) {
	Path path = Paths.get(dictFileDir, FileName);
	try {
	    List<String> lines = Files.readAllLines(path, Charset.defaultCharset());
	    for (String word : lines) {
		if (word.indexOf("\'") != -1) {
		    //System.out.println(word);
		    continue;
	       	}
		else {
		    String lword = leastAna(word);
		    ArrayList<String> llist = new ArrayList<String>();
		    if (HML.containsKey(lword)){
			llist = HML.get(lword);
		    }
		    llist.add(word);
		    HML.put(lword, llist);
		}
	    }
	}
	catch (IOException e) {
	    System.out.println(e);
	}
    }

    public static String sortword(String w) {
	char[] word = w.toCharArray();
	Arrays.sort(word);
	String wordStr = new String(word);
	return wordStr;
    }
    public static String leastAna(String word) {
	String sword = word.toLowerCase();
	return sortword(sword);
    }

    public static void query(String word) {
	String lword = leastAna(word);
	if (HML.containsKey(lword)){
	    System.out.println("THe anagrams for \""+word+"\" are:");
	    for (String s : HML.get(lword)) {
		System.out.println(s);
	    }
	}
	else {
	    System.out.println("There is no anagrams for \""+word+"\".");
	}
    }
}
