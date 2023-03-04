import java.io.*;
import java.net.*;
public class SocketServer {
    public static void main(String args[])throws Exception{
        ServerSocket ss = new ServerSocket(3333);
        Socket s = ss.accept();

        DataOutputStream dout=new DataOutputStream(s.getOutputStream());
	DataInputStream din = new DataInputStream(s.getInputStream());
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	String str="",str2="";
	while(!str.equals("stop")) {
		str=din.readUTF();
		System.out.println("client says: "+str);
	//	str2=br.readLine();
		str2 = "name = smee";
		dout.writeUTF(str2);
		dout.flush();
            	str = "stop";
	}

        s.close();
        ss.close();
    }
}

