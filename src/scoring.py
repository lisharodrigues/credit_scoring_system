import numpy as np
import pandas as pd

def score_wallets(df):
    df = df.copy()

    # Normalize components and calculate weighted score
    df['score'] = (
        np.clip(df['repay_to_borrow_ratio'], 0, 1) * 300 +
        (1 - np.clip(df['liquidation_ratio'], 0, 1)) * 300 +
        np.clip(df['total_deposit'] / 100000, 0, 1) * 200 +
        np.clip(df['active_days'] / 365, 0, 1) * 200
    )

    df['score'] = df['score'].round().astype(int)
    return df[['wallet', 'score']]
