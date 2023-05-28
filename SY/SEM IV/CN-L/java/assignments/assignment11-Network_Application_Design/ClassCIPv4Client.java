import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class ClassCIPv4Client {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 1234);
            System.out.println("Connected to server...");

            BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in));
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            System.out.print("Enter a Class C IPv4 address (192.0.0.0 - 223.255.255.255): ");
            String ipAddress = consoleReader.readLine();

            out.println(ipAddress);

            String networkId = in.readLine();
            String hostId = in.readLine();

            System.out.println("Network ID: " + networkId);
            System.out.println("Host ID: " + hostId);

            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
