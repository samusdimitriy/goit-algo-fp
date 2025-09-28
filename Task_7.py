import random
from collections import Counter
import matplotlib.pyplot as plt


THEORETICAL_PROBABILITIES = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def simulate_rolls(count):
    results = Counter()
    for _ in range(count):
        total = random.randint(1, 6) + random.randint(1, 6)
        results[total] += 1
    return results


def calculate_probabilities(results, simulations):
    return {total: results[total] / simulations for total in range(2, 13)}


def build_table(simulations):
    counts = simulate_rolls(simulations)
    probabilities = calculate_probabilities(counts, simulations)

    table = []
    for total in range(2, 13):
        monte_carlo = probabilities[total]
        analytical = THEORETICAL_PROBABILITIES[total]
        difference = abs(monte_carlo - analytical)
        table.append(
            {
                "sum": total,
                "count": counts[total],
                "monte_carlo": monte_carlo,
                "analytical": analytical,
                "difference": difference,
            }
        )

    return table


def display_table(table, simulations):
    print(f"Simulations: {simulations}")
    print("Sum | Count | Monte Carlo % | Analytical % | Difference %")
    print("-" * 57)
    for row in table:
        print(
            f"{row['sum']:>3} | {row['count']:>5} | "
            f"{row['monte_carlo'] * 100:>13.2f} | "
            f"{row['analytical'] * 100:>12.2f} | "
            f"{row['difference'] * 100:>11.2f}"
        )


def plot_results(table):
    sums = [row["sum"] for row in table]
    monte_carlo_probs = [row["monte_carlo"] for row in table]
    analytical_probs = [row["analytical"] for row in table]

    width = 0.35
    positions = range(len(sums))

    plt.bar(
        [pos - width / 2 for pos in positions],
        monte_carlo_probs,
        width=width,
        label="Monte Carlo",
        color="#2E8BC0",
    )
    plt.bar(
        [pos + width / 2 for pos in positions],
        analytical_probs,
        width=width,
        label="Analytical",
        color="#B1D4E0",
    )

    plt.xticks(list(positions), sums)
    plt.xlabel("Sum of dice")
    plt.ylabel("Probability")
    plt.title("Dice sum probabilities: Monte Carlo vs Analytical")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    simulations = 50_000
    table = build_table(simulations)
    display_table(table, simulations)
    plot_results(table)


if __name__ == "__main__":
    main()
