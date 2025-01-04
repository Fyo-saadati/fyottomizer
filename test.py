from main import WeightedRandom


def test_weighted_random():
    weighted = WeightedRandom()
    evens = 0
    for i in range(1000):
        n = weighted.weight_on_even(25, 0, 1999)
        if n % 2 == 0:
            evens += 1
    print(f"even weight: 25/ evens percentage={evens/10}")

    odds = 0
    for i in range(1000):
        n = weighted.weight_on_odd(43, 0, 1999)
        if n % 2 != 0:
            odds += 1
    print(f"odd weight: 43/ odds percentage={odds/10}")

    up = 0
    for i in range(1000):
        n = weighted.weight_on_limit(60, 200, 3000, {"dir": "up", "int": 400})
        if n > 400:
            up += 1
    print(f"up weight: 60/ ups percentage={up/10}")

    down = 0
    for i in range(1000):
        n = weighted.weight_on_limit(
            10,
            200,
            3000,
            {"dir": "down", "int": 300},
        )
        if n < 300:
            down += 1
    print(f"down weight: 10/ downs percentage={down/10}")


if __name__ == "__main__":
    test_weighted_random()
