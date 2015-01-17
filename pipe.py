import requests
import json
import re


def get_existing_results(infile="results.json"):
    with open(infile, "r") as f:
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


def f3(input_str):
    # The product of the digits is < 119
    product = 1
    for letter in input_str:
        if letter.isdigit():
            val = int(letter)
        else:
            val = ord(letter) - 55
        product *= val

    return product < 119


def main(inputs):
    results = []
    for inp in inputs:
        try:
            r = requests.get(
                'http://www.20000puzzles.com/dynamic/puzzle/pipe/query?input={}'
                        .format(inp),
                auth=('adphi', 'hunter2'))
            output = r.json()['result']['output']

            if "Success" in output:
                data = {
                    "result": "success",
                    "input": inp
                }
            else:
                stage_index = output.index("Error in stage")
                stage = output[stage_index + 15: stage_index + 16]
                msg = str(output[stage_index + 18:])

                data = {
                    "result": "failure",
                    "stage": int(str(stage)),
                    "msg": msg,
                    "input": inp
                }
            results.append(data)
            print data

        except KeyboardInterrupt:
            break
    return results

if __name__ == '__main__':
    with open("valid_inputs.txt", "r") as f:
        inputs = f.read().split("\n")
    save_results(main(inputs))
