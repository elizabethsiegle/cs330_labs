import java.nio.charset.Charset;
import java.nio.file.*;
import java.util.*;
import java.io.*;
import java.net.URL;
import java.lang.Math;

public class Hash{

	static int[] indexes; 
	static int N;

    public static void main(String[] args){
		N = 50000;
		int collision = 1;
		while(collision!=0){
			indexes = new int[N];
			for(int i = 0; i < N; i++) {
				indexes[i] = 0;
			}
			readFile("http://cs.brynmawr.edu/Courses/cs206/fall2016/DataFiles/uszipcodes.csv");
			collision = countColLoadFactor();	
			N += 50000;	
		}	
    }

    public static void readFile(String FileName) {
		try{
			URL fileURL = new URL(FileName);
			Scanner sc = new Scanner(fileURL.openStream());
			sc.nextLine();
			while(sc.hasNextLine()){
				String line = sc.nextLine();
				String[] words = line.split(",");
				indexes[Math.abs(words[0].hashCode())%N]++;
			}
		} catch (Exception e) {
			e.printStackTrace();
		}	

	}

	public static int countColLoadFactor() {
		int collision = 0;
		int load = 0;
		for (int i = 0; i < N; i++) {
			
			if (indexes[i] > 0) {
				load += indexes[i];
				collision += indexes[i]-1;
			}
		}
		double lf = (load+0.0)/N;
		System.out.println("Number of collisions for array of size "+N+" is "+collision+".");
		System.out.println("Load Factor for array of size "+N+" is "+lf+".");
		System.out.println("");
		return collision;	
	}
}
