import pipe


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    return True


def main():
    results = pipe.get_existing_results("stage3.json")
    nums = []

    for result in results:
        msg = result['msg']
        nums.append(int(msg.split(" ")[1]))

    print "Any Primes: ", any(map(is_prime, nums))
    print "Min: ", min(nums)
    print "Max: ", max(nums)


if __name__ == '__main__':
    main()
