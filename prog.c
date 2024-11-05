#include <stdio.h>

int main() {
    char name[50];  // Array to hold the name

    // Ask for the user's name
    printf("What's your name? ");
    fgets(name, sizeof(name), stdin);  // Read the input

    // Print the greeting
    printf("Hello, %s! Welcome to C programming.\n", name);

    return 0;
}
