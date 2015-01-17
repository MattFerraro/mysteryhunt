import requests
import json
import os
import re


def get_existing_results():
    with open("results.json", "r") as f:
        results = json.load(f)
    return results


def save_results(results, outfile="results.json"):
    with open(outfile, "w") as f:
        json.dump(results, f, indent=2)


f1_regex = re.compile('^[A-Z0-9]+$')


def f1(input_str):
    # Is uppercase letters/numbers only
    return f1_regex.match(input_str) is not None


def isprime(number):
    # Tells you if number is prime, only works if number < 36
    primes_under_36 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    if number in primes_under_36:
        return True
    else:
        return False


def f2(input_str):
    # Every char is a prime number. numbers 0-9 are themselves.
    # Letters A-Z = 10-36
    for letter in input_str:
        if letter.isdigit():
            val = int(letter)
        else:
            val = ord(letter) - 55
        if not isprime(val):
            return False
    return True


def main(results):
    start_index = 0
    if len(results) > 0:
        last_result = results[-1]
        start_index = last_result['input'] + 1

    for i in range(start_index, start_index + 100000):
        if f1(str(i)) and f2(str(i)):
            try:
                r = requests.get(
                    'http://www.20000puzzles.com/dynamic/puzzle/pipe/query?input={}'
                            .format(i),
                    auth=('adphi', 'hunter2'))
                output = r.json()['result']['output']

                if "Success" in output:
                    data = {
                        "result": "success",
                        "input": i
                    }
                else:
                    stage_index = output.index("Error in stage")
                    stage = output[stage_index + 15: stage_index + 16]
                    msg = str(output[stage_index + 18:])

                    data = {
                        "result": "failure",
                        "stage": int(str(stage)),
                        "msg": msg,
                        "input": i
                    }
                results.append(data)
                print data

            except KeyboardInterrupt:
                break
    return results

if __name__ == '__main__':
    if os.path.exists("results.json"):
        # resume!
        save_results(main(get_existing_results()))
    else:
        # start from scratch!
        save_results(main([]))
