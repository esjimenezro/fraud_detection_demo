import pandas as pd


def customers_transactions_split(train_or_test='Train'):
    # Read data
    data = pd.read_csv(f"data/fraud{train_or_test}.csv", 
                       index_col=[0],
                       low_memory=False)
    # Customer columns
    customer_columns = ['first', 'last', 'gender', 'street', 'city', 'state',
                        'zip', 'lat', 'long', 'city_pop', 'job', 'dob']
    # Obtain customers data and remove from transaction data
    customers = data.groupby(by='cc_num')[customer_columns].agg('first').reset_index()
    transactions = data.drop(columns=customer_columns).copy()
    # Save split data
    customers.to_csv(f"data/customers{train_or_test}.csv", index=False)
    transactions.to_csv(f"data/transactions{train_or_test}.csv", index=False)