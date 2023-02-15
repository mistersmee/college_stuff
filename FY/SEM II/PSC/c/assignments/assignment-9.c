#include <stdio.h>
#include<string.h>

void isPalindrome(char str[])
{
    // Start from leftmost and rightmost corners of str
    int l = 0;
    int h = strlen(str) - 1;

    // Keep comparing characters while they are same
    while (h > l)
    {
	if (str[l++] != str[h--])
	{
	    printf("%s is not a palindrome\n", str);
	    return;
	}
    }
    printf("%s is a palindrome\n", str);
}

int
q1()
{
    char a[10];
    int i = 0;
    printf("Enter a string:");
    fgets(a, 10, stdin);

    printf("\nThe length of the string a is: %lu", strlen(a) - 1);

    while( a[i] != '\0' ) {
	if ( a[i] == 'a' ) {
	    a[i] = 'm';
	}
	i++;
    }

    printf("\nAfter replacing 'a' in string with 'm', we get: %s", a);

    return 0;
}

int q2()
{
    isPalindrome("Aseem");
    isPalindrome("abba");
    isPalindrome("baab");

    return 0;
}

int
q3()
{
    char input[10];
    int length = 0;

    printf("Enter a string:");
    fgets(input, 10, stdin);

    while( input[length] != '\0' ) {
	length++;
    }

    printf("%i\n", length - 1 );
    return 0;
}
int
q4()
{
    char s1[10], s2[100], i;

    printf("Enter a string:");
    fgets(s1, 10, stdin);

    printf("string s1 : %s\n", s1);

    for (i = 0; s1[i] != '\0'; ++i) {
	s2[i] = s1[i];
    }

    s2[i] = '\0';

    printf("String s2 : %s", s2);

    return 0;
}

int
main()
{
    q1();
    q2();
    q3();
    q4();
    return 0;
}


