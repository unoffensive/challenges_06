#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    // Check if the dummy process is still running
    if (system("ps -p $(pgrep sleep) > /dev/null") == 0) {
        printf("Process is still running.\n");
    } else {
        printf("Process has finished.\n");
    }

    return 0;
}
