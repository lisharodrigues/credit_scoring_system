import pandas as pd
import json
from datetime import datetime


def load_and_engineer_features(file_path):
    print("Loading data from:", file_path)
    
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Flatten the nested structure (merge actionData into top level)
    flattened = []
    for entry in data:
        flat = {
            'wallet': entry.get('userWallet'),
            'timestamp': entry.get('timestamp'),
            'action': entry.get('action').lower(),  # normalize case
        }

        action_data = entry.get('actionData', {})
        flat['amount'] = float(action_data.get('amount', 0))  # ensure numeric
        flat['type'] = action_data.get('type', '').lower()

        flattened.append(flat)

    df = pd.DataFrame(flattened)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df.dropna(subset=['amount'], inplace=True)

    # Group by wallet
    grouped = df.groupby('wallet')

    feature_list = []
    for wallet, group in grouped:
        record = {
            'wallet': wallet,
            'num_txns': len(group),
            'active_days': group['timestamp'].dt.date.nunique(),
            'total_deposit': group[group['action'] == 'deposit']['amount'].sum(),
            'total_borrow': group[group['action'] == 'borrow']['amount'].sum(),
            'total_repay': group[group['action'] == 'repay']['amount'].sum(),
            'num_liquidations': len(group[group['action'] == 'liquidationcall']),
        }

        # Derived ratios
        record['repay_to_borrow_ratio'] = record['total_repay'] / (record['total_borrow'] + 1e-6)
        record['liquidation_ratio'] = record['num_liquidations'] / (record['num_txns'] + 1e-6)

        feature_list.append(record)

    return pd.DataFrame(feature_list)
