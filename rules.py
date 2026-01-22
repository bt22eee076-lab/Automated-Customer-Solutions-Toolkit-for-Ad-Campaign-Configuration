def check_budget(budget):
    if budget < 100:
        return ("Very low daily budget may severely limit performance", "MEDIUM")
    return None


def check_bidding_strategy(strategy, conversion_tracking):
    if strategy == "MAX_CONVERSIONS" and conversion_tracking == "NO":
        return ("Max conversions bidding without conversion tracking enabled", "HIGH")
    return None


def check_targeting(targeting):
    if targeting == "BROAD":
        return ("Broad targeting may reduce relevance", "LOW")
    return None
