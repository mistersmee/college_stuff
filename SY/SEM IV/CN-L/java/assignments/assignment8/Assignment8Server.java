// SimpleServer.java: a simple server program
import java.net.*;
import java.io.*;

public class Assignment8Server {
    public static void main(String args[]) throws IOException {
        // Register service on port 1234
        ServerSocket s = new ServerSocket(1234);
        Socket s1 = s.accept(); // Wait and accept a connection
        // Get a communication stream associated with the socket
        InputStream s1In = s1.getInputStream();
        DataInputStream dis = new DataInputStream(s1In);


        int arr1[] = new int[5];

        for (int i= 0; i < 4; i++) {
            arr1[i] = dis.readInt();
        }

        System.out.println("Received array is:");
        for (int i = 0; i < 4; i++) {
           System.out.print(arr1[i] + " ");
        }

        // Close the connection, but not the server socket
        s1.close();
        s.close();
    }
}
