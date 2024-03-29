#include <stdio.h>
#include <sys/types.h>//socket
#include <sys/socket.h>//socket
#include <string.h>//memset
#include <stdlib.h>//sizeof
#include <netinet/in.h>//INADDR_ANY
#include <time.h>
#define PORT 8000
#define MAXSZ 100


int main()
{
    int sockfd;	//to create socket
    int newsockfd;	//to accept connection
    struct sockaddr_in serverAddress;	//server receive on this address
    struct sockaddr_in clientAddress;	//server sends to client on this address
    int n;
    char str[MAXSZ];
    int clientAddressLength;
	//create socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);

	//initialize the socket addresses
    memset(&serverAddress, 0, sizeof(serverAddress));

    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = htonl(INADDR_ANY);
    serverAddress.sin_port = htons(PORT);

	//bind the socket with the server address and port
    bind(sockfd, (struct sockaddr *) &serverAddress, sizeof(serverAddress));

	//listen for connection from client
    listen(sockfd, 5);

	//accept a connection
	printf("\n*****server waiting for new client connection:*****\n");

        clientAddressLength = sizeof(clientAddress);

        newsockfd = accept(sockfd, (struct sockaddr *) &clientAddress, &clientAddressLength);

    time_t tm;


    while (1)
    {


            tm= time(NULL);

            snprintf(str,sizeof(str),"%s",ctime(&tm));
            write(newsockfd,str, sizeof(str));
            printf("Date & Time Sent :%s\n", str);

    }	//close exterior while

    return 0;
}
