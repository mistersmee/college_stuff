// SimpleClient.java: a simple client program
import java.net.*;
import java.util.Scanner;
import java.io.*;

public class AM37CGPAClient {
    public static void main(String args[]) throws IOException {
        Scanner userInput = new Scanner(System.in);
        // Open your connection to a server, at port 1234
        Socket s1 = new Socket("localhost",1234);
        // Get an input file handle from the socket and read the input
        OutputStream outToServer = s1.getOutputStream();
        DataOutputStream out = new DataOutputStream(outToServer);

        System.out.println("Enter your CGPA:");

        Double x = userInput.nextDouble();

        out.writeDouble(x);
        
        InputStream s1In = s1.getInputStream();
        DataInputStream dis = new DataInputStream(s1In);

        Double percentmarks = dis.readDouble();

        System.out.println("The percentage marks for given CGPA is: " + percentmarks);

        // When done, just close the connection and exit
        dis.close();
        s1In.close();
        s1.close();
        userInput.close();
    }
}