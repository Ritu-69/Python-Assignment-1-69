#include <stdio.h>

int main() {
    float num;
    int int_num;

    printf("Enter a floating-point number: ");
    scanf("%f", &num);

    // Explicit type casting
    int_num = (int)num;

    printf("Integer value: %d\n", int_num);
    return 0;
}
