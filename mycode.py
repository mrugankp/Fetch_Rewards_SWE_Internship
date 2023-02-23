import csv
import sys

def spend_points(points_to_spend, filename):
    # Step 2: Read the CSV file and store transactions in a list of dicts
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        transactions = [row for row in reader]

    # Step 3: Sort the transactions by timestamp in ascending order
    transactions.sort(key=lambda t: t['timestamp'])
    # Step 4: Create a dictionary to keep track of point balances
    balances = {}
    for transaction in transactions:
        balances[transaction['payer']] = balances.get(transaction['payer'], 0) + int(transaction['points'])

    # Step 5: Spend the points
    spent = {}
    for transaction in transactions:
        payer = transaction['payer']
        points = int(transaction['points'])
        timestamp = transaction['timestamp']
        if points_to_spend > 0:
            spendable_points = min(points_to_spend, points)
            balances[payer] -= spendable_points
            spent[payer] = spent.get(payer, 0) - spendable_points
            points_to_spend -= spendable_points
        if points_to_spend == 0:
            break

    # Step 6: Print the final balances
    for payer, balance in balances.items():
        print(f'{payer}: {balance}')

    return spent


if __name__ == '__main__':
    points_to_spend = int(sys.argv[1])
    filename = sys.argv[2]
    spend_points(points_to_spend, filename)