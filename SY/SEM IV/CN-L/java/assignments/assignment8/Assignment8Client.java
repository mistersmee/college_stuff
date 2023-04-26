// SimpleClient.java: a simple client program
import java.net.*;
import java.util.Scanner;
import java.io.*;

public class Assignment8Client {
    public static void main(String args[]) throws IOException {
        Scanner userInput = new Scanner(System.in);
        // Open your connection to a server, at port 1234
        Socket s1 = new Socket("localhost",1234);
        // Get an input file handle from the socket and read the input
        OutputStream outToServer = s1.getOutputStream();
        DataOutputStream out = new DataOutputStream(outToServer);

        int [] arr1 = new int [] {1, 2, 3, 4, 5};

        System.out.println("Elements of original array: ");
        for (int i = 0; i < arr1.length; i++) {
           System.out.print(arr1[i] + " ");
        }

        for (int i = 0; i < arr1.length; i++) {
           out.writeInt(arr1[i]);
        }

        s1.close();
        userInput.close();
    }
}
