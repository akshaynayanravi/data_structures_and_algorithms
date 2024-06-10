import time


def evaluate_test_cases(test_cases, implementation):
    results = []
    for test_case in test_cases:
        result = dict()
        start_time = time.time()
        actual_output = implementation(**test_case["input"])
        time_taken = round(time.time() - start_time, 2)
        if actual_output == test_case["output"]:
            result["Status"] = "Passed"
        else:
            result["Status"] = "Failed"

        result["Input"] = test_case["input"]
        result["Expected Output"] = test_case["output"]
        result["Actual Output"] = actual_output
        result["Time Taken"] = time_taken
        results.append(result)

    return results
