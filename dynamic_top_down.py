_NOT_COMPUTED = -1


def dynamic_top_down_solution(bar_size: int, price_data: dict[int, int]) -> list[int]:
    if bar_size <= 0:
        return "Bar size must be greater than 0."

    memo_profit = [_NOT_COMPUTED] * (bar_size + 1)
    memo_cut = [0] * (bar_size + 1)

    total_recursive_calls = 0

    def solver(current_size: int) -> int:
        nonlocal total_recursive_calls
        total_recursive_calls += 1
        if current_size == 0:
            return 0

        if memo_profit[current_size] != _NOT_COMPUTED:
            return memo_profit[current_size]

        current_max_profit_for_len = 0
        for piece_size in price_data.keys():
            if piece_size <= current_size:
                profit_from_remainder = solver(current_size - piece_size)

                potential_profit_with_this_cut = (
                    price_data[piece_size] + profit_from_remainder
                )

                if potential_profit_with_this_cut > current_max_profit_for_len:
                    current_max_profit_for_len = potential_profit_with_this_cut
                    memo_cut[current_size] = piece_size

        memo_profit[current_size] = current_max_profit_for_len
        return current_max_profit_for_len

    max_total_profit = solver(bar_size)

    optimal_cuts = []
    remaining_len = bar_size
    while remaining_len > 0:
        cut_made = memo_cut[remaining_len]
        remaining_len -= cut_made
        optimal_cuts.append(cut_made)

    # print(
    #     f"Memoized profit table: {memo_profit}\n"
    #     f"Memoized cut table: {memo_cut}\n"
    #     f"Cuts: {optimal_cuts}\n"
    #     f"Total profit: {max_total_profit}\n"
    #     f"Total recursive calls: {total_recursive_calls}"
    # )
    return {
        "cuts": optimal_cuts,
        "total_profit": max_total_profit,
        "total_recursive_calls": total_recursive_calls,
    }
    # return optimal_cuts
