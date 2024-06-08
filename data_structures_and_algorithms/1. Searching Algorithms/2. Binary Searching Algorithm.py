"""
1. State the problem clearly. Identify the input & output formats.
    Write a program to find the position of a given number in a
    list of numbers arranged in decreasing order.

    Input:
        numbers = [13, 11, 10, 7, 4, 3, 1, 0]
        query = 7
    Output:
        position = 3

2. Come up with some example inputs & outputs. Try to cover all edge cases.
    i. The number query occurs somewhere in the middle of the list cards.
    ii. query is the first element in cards.
    iii. query is the last element in cards.
    iv. The list cards contains just one element, which is query.
    v. The list cards does not contain number query.
    vi. The list cards is empty.
    vii. The list cards contains repeating numbers.
    viii. The number query occurs at more than one position in cards.

3. Come up with a correct solution for the problem. State it in plain English.
    Binary Search Algorithm
    i. Find the middle element of the list.
    ii. If it matches queried number, return the middle position as the answer.
    iii. If it is less than the queried number, then search the first half of the list
    iv. If it is greater than the queried number, then search the second half of the list
    v. If no more elements remain, return -1.

4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algorithm's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
"""


def check_location(cards, query, mid_idx):
    mid_card = cards[mid_idx]
    if mid_card == query:
        if mid_idx - 1 >= 0 and cards[mid_idx - 1] == query:
            return "left"

        else:
            return "found"

    elif mid_card < query:
        return "left"

    elif mid_card > query:
        return "right"


def locate_card(cards, query):
    low_idx, high_idx = 0, len(cards) - 1

    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        mid_card = cards[mid_idx]

        if mid_card == query:

            return mid_idx

        elif mid_card < query:
            high_idx = mid_idx - 1
        elif mid_card > query:
            low_idx = mid_idx + 1


def locate_card_v2(cards, query):
    low_idx, high_idx = 0, len(cards) - 1

    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        card_check = check_location(cards, query, mid_idx)

        if card_check == "found":
            return mid_idx

        elif card_check == "left":
            high_idx = mid_idx - 1

        elif card_check == "right":
            low_idx = mid_idx + 1

    return -1


tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
         {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
         {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
         {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
         {'input': {'cards': [6], 'query': 6}, 'output': 0},
         {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
         {'input': {'cards': [], 'query': 7}, 'output': -1},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
          'output': 7},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                    'query': 6},
          'output': 2}]


if __name__ == "__main__":
    from utils.evaluate import evaluate_test_cases
    results = evaluate_test_cases(test_cases=tests, implementation=locate_card_v2)
    print(results)