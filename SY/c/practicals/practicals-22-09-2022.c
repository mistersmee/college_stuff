#include <stdio.h>

int
main()
{
        int num, i, j, flag = 0;
        printf("Enter a number:");
        scanf("%d", &num);
        printf("The numbers which are prime until %d are:", num);
        for (i = 1; i <= num; i++) {
                flag = 0;
                for (j = 2; j < i; j++) {
                        if (i % j == 0) {
                                flag++;
                                break;
                        }
                }
                if (flag == 0 & i != 1) {
                        printf("\n%d", i);
                }

        }
}
