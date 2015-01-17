
import pipe

results = pipe.get_existing_results()

by_stage = {}
successes = []

for i in range(1, 8):
    by_stage[i] = []

for result in results:
    if 'stage' in result:
        by_stage[result['stage']].append(result)
    else:
        successes.append(result)


for i in range(1, 8):
    pipe.save_results(by_stage[i], "stage{}.json".format(i))

pipe.save_results(successes, "successes.json")
