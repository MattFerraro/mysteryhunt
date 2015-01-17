import pipe


def main():
    results = pipe.get_existing_results("stage4.json")
    unpaired = []

    for result in results:
        msg = result['msg']
        letter = str(msg.split(" ")[3].split("'")[1])
        unpaired.append(letter)
        print letter

    print set(unpaired)
    hist = {x: unpaired.count(x) for x in set(unpaired)}
    print hist

if __name__ == '__main__':
    main()
