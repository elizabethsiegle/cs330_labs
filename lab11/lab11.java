import java.nio.charset.Charset; 
import java.nio.file.*; 
import java.util.*; 
import java.io.*; 
import java.net.URL; 
 
public class lab11{ 
    private static List<Integer> pred = new ArrayList<Integer>(); 
    private static List<Double> shortest= new ArrayList<Double>(); 
     
    public static void Dijkstra(Graph graph, int src) { 
        int numVert = graph.V(); 
         
        List<Integer> q = new ArrayList<Integer>(); 
        List<Integer> removed = new ArrayList<Integer>(); 
         
        for (int i = 0; i < numVert; i++) { 
            pred.add(-1); 
            shortest.add(Double.MAX_VALUE); 
            q.add(i); 
        } 
         
        shortest.set(src, (double) 0); 
         
        while (q.size() != 0) { 
            int top = -1; 
            double minVal = Collections.max(shortest); 
             
            for (int i = 0; i < shortest.size(); i++){ 
                if (q.size() < numVert){ 
                    if (q.contains(i)){ 
                        if (shortest.get(i) <= minVal){ 
                            minVal = shortest.get(i); 
                            top = i; 
                        } 
                    } 
                } else { 
                    if (shortest.get(i) < minVal){ 
                        minVal = shortest.get(i); 
                        top = i; 
                    } 
                } 
            } 
             
            int del = q.remove(q.indexOf(top)); 
            ArrayList<Edge> adjList = graph.getAdj(top); 
             
            for(Edge e: adjList) { 
                relax(e); 
            } 
        } 
    } 
     
    public static void printPath(Graph graph, int dest) { 
        String path = "Shortest path from 0 to " + Integer.toString(dest) + ": \n"; 
        List<Integer> pathList = new ArrayList<Integer>(); 
        int cur = dest; 
        pathList.add(cur); 
        while (cur != 0) { 
            cur = pred.get(cur); 
            pathList.add(cur); 
        } 
         
        for (int i = pathList.size() - 1; i >= 1; i--){ 
            int vert = pathList.get(i); 
            ArrayList<Edge> adj = graph.getAdj(vert); 
            for (Edge v: adj){ 
                if (v.to() == pathList.get(i-1)){ 
                    path = path + v.toString(); 
                } 
            } 
        } 
         
        System.out.println(path); 
    } 
     
    public static void relax(Edge e) { 
        int fr = e.from(); 
        int to = e.to(); 
        double wt = e.weight(); 
        if (shortest.get(fr) + wt < shortest.get(to)) { 
            shortest.set(to, shortest.get(fr) + wt); 
            pred.set(to, fr); 
        } 
    } 
     
    public static void main(String[] args) { 
        Graph graph = readFile("http://cs.brynmawr.edu/Courses/cs330/spring2017/mediumEWD.txt"); 
        Dijkstra(graph, 0); 
        System.out.println(graph); 
        Scanner sc = new Scanner(System.in); 
        System.out.print("Enter the destination vertex: ");
        int target = Integer.parseInt(sc.nextLine()); 
        printPath(graph, target); 
    } 
     
    public static Graph readFile(String FileName) { 
         
        try{ 
            URL fileURL = new URL(FileName); 
            Scanner sc = new Scanner(fileURL.openStream()); 
             
            int numV = Integer.parseInt(sc.nextLine()); 
            Graph graph = new Graph(numV); 
             
            sc.nextLine(); 
             
            while (sc.hasNextLine()) { 
                 String line = sc.nextLine(); 
                 System.out.println(line); 
                 String[] words = line.trim().split(" "); 
Edge e = new Edge(Integer.parseInt(words[0]), Integer.parseInt(words[1]), Double.parseDouble(words[2])); 
                 graph.addEdge(e); 
            } 
            return graph; 
        } catch (Exception e) { 
            e.printStackTrace(); 
        } 
        return null; 
    } 
}
