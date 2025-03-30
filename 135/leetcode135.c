#include <stdio.h>
#include <stdlib.h>

int candy(int* ratings, int ratingsSize) {
    if (ratingsSize == 0) return 0;

    unsigned candies[ratingsSize];
    int sum = 0;

    // Initialize the candies array with 1 candy for each child
    for (unsigned i = 0; i < ratingsSize; i++) {
        candies[i] = 1;
    }

    // Left-to-right pass
    for (unsigned i = 1; i < ratingsSize; i++) {
        if (ratings[i] > ratings[i - 1]) {
            candies[i] = candies[i - 1] + 1;  // Give more candy if rating is higher than the previous child
        }
    }

    // Right-to-left pass
    for (int i = ratingsSize - 2; i >= 0; i--) {
        if (ratings[i] > ratings[i + 1]) {
            candies[i] = (candies[i] > candies[i + 1] + 1) ? candies[i] : candies[i + 1] + 1;
            // Ensure candies[i] is greater than candies[i+1] + 1
        }
    }

    // Sum the total candies
    for (unsigned i = 0; i < ratingsSize; i++) {
        sum += candies[i];
    }

    return sum;
}

int main(int argc, char *argv[]) {
    int size = argc - 1;
    int ratings[size];

    // Convert the command line arguments to integers
    for (int i = 0; i < size; i++) {
        ratings[i] = atoi(argv[i + 1]);
    }

    int result = candy(ratings, size);
    printf("Minimum candies required: %d\n", result);
    return 0;
}
