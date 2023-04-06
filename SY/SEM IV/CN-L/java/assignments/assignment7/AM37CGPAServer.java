// SimpleServer.java: a simple server program
import java.net.*;
import java.io.*;

public class AM37CGPAServer {
    public static void main(String args[]) throws IOException {
        // Register service on port 1234
        ServerSocket s = new ServerSocket(1234);
        Socket s1=s.accept(); // Wait and accept a connection
        // Get a communication stream associated with the socket
        InputStream s1In = s1.getInputStream();
        DataInputStream dis = new DataInputStream(s1In);
        
        Double x = dis.readDouble();

        Double percentmarks = (x * 10) - 7.5;

        OutputStream s1out = s1.getOutputStream();
        DataOutputStream dos = new DataOutputStream (s1out);

        dos.writeDouble(percentmarks);

        // Close the connection, but not the server socket
        dos.close();
        s1out.close();
        s1.close();
        s.close();
    }
}