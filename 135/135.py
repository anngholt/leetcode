import sys

def candy(ratings):
    ratings_size = len(ratings)
    if ratings_size == 0:
        return 0

    # Initialize the candies array with 1 candy for each child
    candies = [1] * ratings_size
    total = 0

    # Left-to-right pass
    for i in range(1, ratings_size):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1  # Give more candy if rating is higher than previous child

    # Right-to-left pass
    for i in range(ratings_size - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)  # Ensure enough candy compared to right neighbor

    # Sum the total candies
    for c in candies:
        total += c

    return total

# Ensure this only runs when the script is executed directly
if __name__ == "__main__":
    # Skip the first command line argument (script name)
    args = sys.argv[1:]
    ratings = list(map(int, args))  # Convert arguments to integers

    result = candy(ratings)
    print("Minimum candies required:", result)
