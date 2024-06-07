#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    // Wait for 1 minute (60 seconds)
    sleep(60);

    // Check if the dummy process is still running
    if (system("pgrep sleep > /dev/null") == 0) {
        printf("Process is still running.\n");
    } else {
        printf("Process has finished. Flag: CTF{Y0u_K1ll_Z_PS}\n");
    }

    return 0;
}
