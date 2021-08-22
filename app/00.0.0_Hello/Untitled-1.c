#include <stdio.h>
int main(void)
{
	int i;
  sum = sum + i;
  for(i=1; i<=20000; i++){
		if(i%3==0){
			printf("%d ", i);
		}else if(i%10==3){
			printf("%d ", i);
		}else if(i/10==3){
			printf("%d ", i);
		}
	}
	printf("\n");
	return 0;
}

#include <stdio.h>
int main(void)
{
  int a[10] = {3, 4, 2, 3, 2, 3, 1, 3, 4, 1};
  int i;
  int sum = 0;
  for (i = 0; i <= 9; i++)
    sum = sum + a[i];
  printf("sum=%d\n", sum);
  return 0;
}