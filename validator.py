import csv
from rules import check_budget, check_bidding_strategy, check_targeting

def validate_campaigns(file_path):
    results = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            campaign = row["campaign_id"]
            issues = []

            budget_check = check_budget(int(row["budget"]))
            if budget_check:
                issues.append(budget_check)

            bidding_check = check_bidding_strategy(
                row["bidding_strategy"], row["conversion_tracking"]
            )
            if bidding_check:
                issues.append(bidding_check)

            targeting_check = check_targeting(row["targeting"])
            if targeting_check:
                issues.append(targeting_check)

            if issues:
                results.append((campaign, issues))

    return results


if __name__ == "__main__":
    findings = validate_campaigns("../data/campaign_config.csv")

    for campaign, issues in findings:
        print(f"\nCampaign {campaign}:")
        for issue, severity in issues:
            print(f" [{severity}] {issue}")
