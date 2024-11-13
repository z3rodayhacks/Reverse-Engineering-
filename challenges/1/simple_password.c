#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    // Check if an argument is provided
    if (argc < 2) {
        puts("Usage: ./a.out <your_input>");
        return 1; // Return an error code
    }

    // Compare the first argument with "cyberyeti"
    if (strcmp("cyberyeti", argv[1]) == 0) {
        puts("You win!");
    } else {
        puts("Try again :(");
    }

    return 0; // Return success
}
