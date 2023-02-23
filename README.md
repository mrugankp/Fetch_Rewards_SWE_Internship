# Fetch_Rewards_SWE_Internship
Take Home Test for Fetch Rewards SWE Internship

To run this code, save it as a Python script (e.g. mycode.py) and run it from the command line with the amount of points to spend and the filename of the CSV file as arguments, like this:


 ```python mycode.py 5000 transactions.csv ```

This should print the final balances and return a dictionary of the points spent by payer.


Our users have points in their accounts. Users only see a single balance in their account. But for reporting purposes, we actually track their
points per payer. In our system, each transaction record contains: payer (string), points (integer), timestamp (date).
For earning points, it is easy to assign a payer. We know which actions earned the points. And thus, which partner should be paying for the
points.

When a user spends points, they don't know or care which payer the points come from. But, our accounting team does care how the points are
spent. There are two rules for determining what points to "spend" first:
● We want the oldest points to be spent first (oldest based on transaction timestamp, not the order they’re received)
● We want no payer's points to go negative.

We expect your code to:
1. Read the transactions from a CSV file.
2. Spend points based on the argument using the rules above.
3. Return all payer point balances.

Example:

1. When you run your program, you will pass in 2 arguments, 1) which is the amount of points to spend 2) name of CSV file
For example, if you are using Python (you don’t have to use Python) to spend 5000 points, it would look like this:
python3 mycode.py 5000 transactions.csv

2. Your code will ingest a CSV file with an example sequence.
● "payer","points","timestamp"
● "DANNON",1000,"2020-11-02T14:00:00Z"
● "UNILEVER",200,"2020-10-31T11:00:00Z"
● "DANNON",-200,"2020-10-31T15:00:00Z"
● "MILLER COORS",10000,"2020-11-01T14:00:00Z"
● "DANNON",300,"2020-10-31T10:00:00Z"

3. After the points are spent, the output should return the following results:
{
"DANNON": 1000,
"UNILEVER": 0,
"MILLER COORS": 5300
}
