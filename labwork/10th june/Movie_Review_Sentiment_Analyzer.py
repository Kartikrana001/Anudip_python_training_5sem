# Movie Review Sentiment Analyzer

reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# Task 1: Count sentiments
def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0

    for review in reviews:
        if "excellent" in review:
            excellent += 1

        elif "good" in review:
            good += 1

        elif "average" in review:
            average += 1

        elif "poor" in review:
            poor += 1

    print("Excellent Reviews:", excellent)
    print("Good Reviews:", good)
    print("Average Reviews:", average)
    print("Poor Reviews:", poor)

# Task 2: Find most common word
def most_common_word(reviews):
    words = []

    for review in reviews:
        words.extend(review.split())

    max_count = 0
    common_word = ""

    for word in words:
        count = words.count(word)

        if count > max_count:
            max_count = count
            common_word = word

    return common_word

# Task 3: Find longest review
def longest_review(reviews):
    longest = reviews[0]

    for review in reviews:
        if len(review) > len(longest):
            longest = review

    return longest

# Task 4: Display reviews with keyword
def reviews_with_keyword(reviews, keyword):
    print("Reviews containing", keyword)

    for review in reviews:
        if keyword in review:
            print(review)

# Function Calls
count_sentiments(reviews)

print("\nMost Common Word:")
print(most_common_word(reviews))

print("\nLongest Review:")
print(longest_review(reviews))

print()
reviews_with_keyword(reviews, "excellent")
