def prepare_items(items):
    return [(name, info["cost"], info["calories"]) for name, info in items.items()]


def summarize_selection(items, selection):
    lookup = {name: (cost, calories) for name, cost, calories in items}
    total_cost = sum(lookup[name][0] for name in selection)
    total_calories = sum(lookup[name][1] for name in selection)
    return total_cost, total_calories

def greedy_algorithm(items, budget):
    sorted_items = sorted(items, key=lambda item: item[2] / item[1], reverse=True)

    selected = []
    total_cost = 0
    total_calories = 0

    for name, cost, calories in sorted_items:
        if total_cost + cost > budget:
            continue
        selected.append(name)
        total_cost += cost
        total_calories += calories

    return {
        "selected_items": selected,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def build_dp_table(items, budget):
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    for i, (_, cost, calories) in enumerate(items, start=1):
        for b in range(budget + 1):
            if cost > b:
                dp[i][b] = dp[i - 1][b]
            else:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)

    return dp


def reconstruct_selection(items, budget, dp):
    selection = []
    b = budget

    for i in range(len(items), 0, -1):
        if dp[i][b] == dp[i - 1][b]:
            continue
        name, cost, _ = items[i - 1]
        selection.append(name)
        b -= cost

    selection.reverse()
    return selection


def dynamic_programming(items, budget):
    dp_table = build_dp_table(items, budget)
    selected = reconstruct_selection(items, budget, dp_table)

    cost, calories = summarize_selection(items, selected)

    return {
        "selected_items": selected,
        "total_cost": cost,
        "total_calories": calories,
    }


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 100

    prepared_items = prepare_items(items)

    greedy_result = greedy_algorithm(prepared_items, budget)
    dynamic_result = dynamic_programming(prepared_items, budget)

    greedy_output = "\n".join(
        [
            "Greedy algorithm:",
            f"Selected items: {greedy_result['selected_items']}",
            f"Total cost: {greedy_result['total_cost']}",
            f"Total calories: {greedy_result['total_calories']}",
        ]
    )

    dynamic_output = "\n".join(
        [
            "Dynamic programming:",
            f"Selected items: {dynamic_result['selected_items']}",
            f"Total cost: {dynamic_result['total_cost']}",
            f"Total calories: {dynamic_result['total_calories']}",
        ]
    )

    print(greedy_output)
    print()
    print(dynamic_output)


if __name__ == "__main__":
    main()
