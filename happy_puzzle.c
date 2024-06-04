#include <stdio.h>
#include <string.h>

int main() {
    int user_input;

    printf("Find the pattern in this sequence: 1, 4, 9, 16, 25, ...\n");
    printf("Enter the next number in the sequence: ");
    scanf("%d", &user_input);

    if (user_input == 36) {
        printf("Well done! Your flag is *Haad{Easy_doing}*.\n");
    } else {
        printf("Incorrect. Please try again.\n");
    }

    return 0;
}
