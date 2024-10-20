#include <stdio.h>

#define PI 3.14159

double calculate_circle_area(double radius) {
    double area = PI * radius * radius;
    return area;
}

int main() {
    double radius, area;

    printf("Enter the radius of the circle: ");
    scanf("%lf", &radius);

    area = calculate_circle_area(radius);

    printf("The area of the circle with radius %.2lf is %.2lf\n", radius, area);

    return 0;
}
