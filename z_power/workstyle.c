#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int num_processes = 5;  // Number of child processes to create
    pid_t pid;

    printf("Starting dummy processes...\n");

    for (int i = 0; i < num_processes; i++) {
        pid = fork();

        if (pid < 0) {
            // Fork failed
            perror("fork");
            exit(EXIT_FAILURE);
        } else if (pid == 0) {
            // Child process
            execlp("sleep", "sleep", "99999", NULL);
            // The following lines will only execute if execlp fails
            perror("execlp");
            exit(EXIT_FAILURE);
        }
    }

    printf("Dummy processes started.\n");

    // Parent process waits for all child processes to complete
    for (int i = 0; i < num_processes; i++) {
        wait(NULL);  // Wait for each child process to terminate
    }

    return 0;
}
