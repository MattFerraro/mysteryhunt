import requests
import json
import os


def get_existing_results():
    with open("results.json", "r") as f:
        results = json.load(f)
    return results


def save_results(results):
    with open("results.json", "w") as f:
        json.dump(results, f)


def main(results):
    start_index = 0
    if len(results) > 0:
        last_result = results[-1]
        start_index = last_result['input'] + 1

    for i in range(start_index, start_index + 10000):
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
