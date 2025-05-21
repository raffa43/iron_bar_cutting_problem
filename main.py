from dynamic_top_down import dynamic_top_down_solution
from greedy import greedy_solution

PRICE_DATA = {
    1: 1,
    2: 2,
    3: 8,
    4: 11,
    5: 14,
    6: 15,
    7: 16,
    8: 18,
    9: 19,
    10: 19,
    11: 20,
    12: 21,
}

if __name__ == "__main__":
    print("Greedy Solution:")
    greedy_result = greedy_solution(12, PRICE_DATA)

    print("\nDynamic Programming Top-Down Solution:")
    dynamic_top_down_solution = dynamic_top_down_solution(12, PRICE_DATA)
