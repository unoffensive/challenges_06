#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    printf("Starting dummy process...\n");

    // Start a dummy process (sleep for 30 seconds)
    if (fork() == 0) {
        execlp("sleep", "sleep", "99999", NULL);
        // The following lines will only execute if execlp fails
        perror("execlp");
        exit(EXIT_FAILURE);
    }

    printf("Dummy process started.\n");

    return 0;
}
