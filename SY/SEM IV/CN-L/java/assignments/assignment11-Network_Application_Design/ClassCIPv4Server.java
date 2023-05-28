import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.InetAddress;

public class ClassCIPv4Server {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(1234);
            System.out.println("Server started and listening on port 1234...");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected: " + clientSocket.getInetAddress());

                Thread clientThread = new Thread(() -> {
                    try {
                        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

                        String ipAddress = in.readLine();
                        String networkId = getNetworkId(ipAddress);
                        String hostId = getHostId(ipAddress);

                        out.println("Network ID: " + networkId);
                        out.println("Host ID: " + hostId);

                        clientSocket.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                });

                clientThread.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String getNetworkId(String ipAddress) {
        try {
            String[] octets = ipAddress.split("\\.");

            int networkId = Integer.parseInt(octets[0]);

            if (networkId >= 192 && networkId <= 223) {
                return octets[0] + "." + octets[1] + "." + octets[2] + ".0";
            } else {
                return "Invalid IP address format";
            }
        } catch (NumberFormatException e) {
            return "Invalid IP address format";
        }
    }

    private static String getHostId(String ipAddress) {
        try {
            String[] octets = ipAddress.split("\\.");

            int networkId = Integer.parseInt(octets[0]);

            if (networkId >= 192 && networkId <= 223) {
                return octets[3];
            } else {
                return "Invalid IP address format";
            }
        } catch (NumberFormatException e) {
            return "Invalid IP address format";
        }
    }
}
