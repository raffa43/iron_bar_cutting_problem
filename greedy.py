def solve_greedy(
    bar_size: int, sorted_pieces_with_ratios: list[tuple[int, float]]
) -> list[int]:

    if bar_size <= 0:
        return []

    best_cut = None
    for piece_size, _ in sorted_pieces_with_ratios:
        if piece_size <= bar_size:
            best_cut = piece_size

            break

    if best_cut is None:
        return []

    next_cuts = solve_greedy(bar_size - best_cut, sorted_pieces_with_ratios)

    return [best_cut] + next_cuts


def greedy_solution(bar_size: int, price_data: dict[int, int]) -> list[int]:
    if bar_size <= 0:
        return "Bar size must be greater than 0."

    pieces_with_ratios = {}
    for piece_size, piece_price in price_data.items():
        ratio = piece_price / piece_size
        pieces_with_ratios[piece_size] = ratio

    pieces_with_ratios = sorted(
        pieces_with_ratios.items(),
        key=lambda item: (item[1], item[0]),
        reverse=True,
    )

    # print("Pieces sorted by ratio:")
    # for piece_size, ratio in pieces_with_ratios:
    #    print(f"Size: {piece_size}, Ratio: {ratio:.2f}")
    cuts = solve_greedy(bar_size, pieces_with_ratios)

    # print("Cuts: ", cuts)
    # print(f"Total profit: {sum(price_data[cut] for cut in cuts)}")
    return {"cuts": cuts, "total_profit": sum(price_data[cut] for cut in cuts)}
