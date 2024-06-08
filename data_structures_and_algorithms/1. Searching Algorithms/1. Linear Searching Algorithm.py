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
    Linear Search Algorithm:
    i. Create a variable position with the value 0.
    ii. Check whether the number at index position in card equals query.
    iii. If it does, position is the answer and can be returned from the function
    iv. If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
    v. If the number was not found, return -1.

4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algorithm's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
"""


def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position

        position += 1

    position = -1
    return position


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
    from utils.evaluate import  evaluate_test_cases
    results = evaluate_test_cases(test_cases=tests, implementation=locate_card)
    print(results)