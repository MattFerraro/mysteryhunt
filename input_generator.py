import pipe


def main():
    alphabet = [
        '2',
        '3',
        '5',
        '7',
        'B',
        'D',
        'H',
        'J',
        'N',
        'T',
        'V'
    ]
    candidates = []

    for let1 in alphabet:
        cand1 = let1

        if pipe.f3(cand1):
            candidates.append(cand1)
        else:
            continue

        for let2 in alphabet:
            cand2 = cand1 + let2

            if pipe.f3(cand2):
                candidates.append(cand2)
            else:
                continue

            for let3 in alphabet:
                cand3 = cand2 + let3

                if pipe.f3(cand3):
                    candidates.append(cand3)
                else:
                    continue

                for let4 in alphabet:
                    cand4 = cand3 + let4

                    if pipe.f3(cand4):
                        candidates.append(cand4)
                    else:
                        continue

                    for let5 in alphabet:
                        cand5 = cand4 + let5

                        if pipe.f3(cand5):
                            candidates.append(cand5)
                        else:
                            continue

                        for let6 in alphabet:
                            cand6 = cand5 + let6
                            if pipe.f3(cand6):
                                candidates.append(cand6)

    print candidates
    print len(candidates)
    save_file("\n".join(candidates))


def save_file(output_str, outfile="valid_inputs.txt"):
    with open(outfile, "w") as f:
        f.write(output_str)

if __name__ == '__main__':
    main()
