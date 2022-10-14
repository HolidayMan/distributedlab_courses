from random import randint
from timeit import timeit


def generate_key(length):
    return randint(0, 2 ** length)


def brute_force(key, length):
    for i in range(2 ** length):
        if i == key:
            return i


def main():
    length = int(input('Enter key length: '))
    print("Key space:", 2 ** length)
    generated_key = generate_key(length)
    print("Generated key:", hex(generated_key))
    generated_key_for_brute_force = generate_key(16)
    timeit_globals = {**globals(), **locals()}
    print(f"Time for bruteforcing 16-bit key {hex(generated_key_for_brute_force)}:",
          timeit('brute_force(generated_key_for_brute_force, 16)', number=1, globals=timeit_globals))
    generated_key_for_brute_force = generate_key(32)
    timeit_globals = {**globals(), **locals()}
    print(f"Time for bruteforcing 32-bit key {hex(generated_key_for_brute_force)}:",
          timeit('brute_force(generated_key_for_brute_force, 32)', number=1, globals=timeit_globals))


if __name__ == '__main__':
    main()