
#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>

int main(){
  int sd1, sd2;
  char buffer[1024];
  struct sockaddr_in serverAddr;
  struct sockaddr_storage serverStorage;
  socklen_t addr_size;


  sd1 = socket(PF_INET, SOCK_STREAM, 0);

  serverAddr.sin_family = AF_INET;
  serverAddr.sin_port = htons(7891); // conversion
  serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
  memset(serverAddr.sin_zero, '\0', sizeof serverAddr.sin_zero);

  bind(sd1, (struct sockaddr *) &serverAddr, sizeof(serverAddr));


  if(listen(sd1,5)==0)
    printf("Listening\n");
  else
    printf("Error\n");


  addr_size = sizeof serverStorage;
  sd2 = accept(sd1, (struct sockaddr *) &serverStorage, &addr_size);

 printf("\n\nRequest recieved from Client & sending message of name");

  strcpy(buffer,"Name == Smee\n");
  send(sd2,buffer,13,0);

  return 0;
}
