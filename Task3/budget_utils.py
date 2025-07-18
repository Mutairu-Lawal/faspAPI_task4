from collections import defaultdict


def group_by_category(transactions):
    grouped = defaultdict(list)
    for tx in transactions:
        grouped[tx.category].append(tx.amount)
    return grouped


def calculate_totals(grouped_data):
    return {category: round(sum(amounts), 2) for category, amounts in grouped_data.items()}
