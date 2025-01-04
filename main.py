import random


class WeightedRandom:

    def generate_numbers(
        self,
        weight: int,
        start: int,
        end: int,
        condition,
    ) -> int:
        if weight not in range(0, 101):
            raise ValueError("Weight must be between 0 and 100")
        valid_numbers = [n for n in range(start, end + 1, 1) if condition(n)]
        remain_numbers = [n for n in range(start, end + 1, 1) if not condition(n)]
        result = random.choices(valid_numbers, k=weight)
        result += random.choices(remain_numbers, k=100 - weight)
        return result

    def weight_on_odd(self, weight: int, start: int, end: int) -> int:
        numbers = self.generate_numbers(
            weight,
            start,
            end,
            lambda x: x % 2 != 0,
        )
        return random.choice(numbers)

    def weight_on_even(self, weight: int, start: int, end: int) -> int:
        numbers = self.generate_numbers(
            weight,
            start,
            end,
            lambda x: x % 2 == 0,
        )
        return random.choice(numbers)

    def weight_on_limit(self, weight: int, start: int, end: int, limit: dict):
        if limit.get("int") not in range(start, end + 1):
            raise ValueError(
                "The entered limit is outside the specified range",
            )
        if limit["dir"] == "up":
            numbers = self.generate_numbers(
                weight,
                start,
                end,
                lambda x: x > limit["int"],
            )
            return random.choice(numbers)

        if limit["dir"] == "down":
            numbers = self.generate_numbers(
                weight,
                start,
                end,
                lambda x: x < limit["int"],
            )
            return random.choice(numbers)
        raise ValueError("Enter Valid direction: up or down")
