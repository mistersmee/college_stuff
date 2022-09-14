#include<stdio.h>

int
main()
{
   FILE * file;
	 FILE *fp;
   char str[500];
	 char str1;
	 //fprintf()
   if (file = fopen("hello.txt", "w")){
      if(fprintf(file, "Smee") >= 0)
      printf("Write operation successful");
   }
   fclose(file);
	//fscanf()
   if (file = fopen("hello.txt", "r")){
         while(fscanf(file,"%s", str)!=EOF){
         printf("%s", str);
      }
   }
   else
   printf("Error!");
   fclose(file);
  //fputc()
   if (file = fopen("hello.txt", "w")){
      fputc('T', file);
   }
   fclose(file);
	//fgetc()
	if (file = fopen("hello.txt", "r")){
      while((str1=fgetc(file))!=EOF)
      printf("%c",str);
   }
   fclose(file);
	//fputs()
	   if (file = fopen("hello.txt", "w")){
      if(fputs("smeesmee", file) >= 0)
      printf("String written to the file successfully...");
   }
   fclose(file);
	//fgets()
	  if (file = fopen("hello.txt", "r")){
      printf("%s", fgets(str, 50, file));
   }
   fclose(file);
	 //fseek()
   fp = fopen("file.txt","w+");
   fputs("Hello I am smee!", fp);

   fseek( fp, 7, SEEK_SET );
   fputs("Smee is me!", fp);
   fclose(fp);
	 return 0;
}

