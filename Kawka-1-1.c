#include <stdio.h>
#include <stdlib.h>

int multiply(int a, int b) {
    int result = 0;

    while (b != 0) {
        if (b & 1) {
            result += a;
        }
        a <<= 1;
        b >>= 1;
    }

    return result;
}

int divide(int dividend, int divisor) {
    if (divisor == 0) {
        printf("Error: Division by zero\n");
        return 0;
    }

    int quotient = 0;
    int sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1;

    dividend = abs(dividend);
    divisor = abs(divisor);

    while (dividend >= divisor) {
        dividend -= divisor;
        quotient++;
    }

    return sign * quotient;
}

int main() {
    int a, b;
    char operator;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    printf("Enter an operator (+, -, *, /): ");
    scanf(" %c", &operator);

    switch (operator) {
        case '+':
            printf("%d + %d = %d\n", a, b, a + b);
            break;
        case '-':
            printf("%d - %d = %d\n", a, b, a - b);
            break;
        case '*':
            printf("%d * %d = %d\n", a, b, multiply(a, b));
            break;
        case '/':
            if (b != 0) {
                printf("%d / %d = %d\n", a, b, divide(a, b));
            } else {
                printf("Error: Division by zero\n");
            }
            break;
        default:
            printf("Error: Invalid operator\n");
    }

    return 0;
}