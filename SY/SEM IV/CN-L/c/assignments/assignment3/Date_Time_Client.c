#include <stdio.h>
#include <sys/types.h>//socket
#include <sys/socket.h>//socket
#include <string.h>//memset
#include <stdlib.h>//sizeof
#include <netinet/in.h>//INADDR_ANY
#define PORT 8000
#define SERVER_IP "127.0.0.1"
#define MAXSZ 100

int main()
{
    int sockfd;	//to create socket
    struct sockaddr_in serverAddress;	//client will connect on this
    int n;
    char msg[MAXSZ];


	//create socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);

	//initialize the socket addresses
    memset(&serverAddress, 0, sizeof(serverAddress));

    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = inet_addr(SERVER_IP);
    serverAddress.sin_port = htons(PORT);

	//client  connect to server on port
    connect(sockfd, (struct sockaddr *) &serverAddress, sizeof(serverAddress));
	//send to sever and receive from server

    while (1)
    {

        read(sockfd, msg, MAXSZ);

        printf("Date & Time Received :%s\n", msg);
    }

    return 0;
}
