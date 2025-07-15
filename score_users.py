print("🔥 If you see this, the script is definitely running.")
import os
import pandas as pd
from src.preprocess import load_and_engineer_features
from src.scoring import score_wallets
from src.utils import save_distribution_plot

# Set file paths
INPUT_PATH = 'data/user_transactions.json'
OUTPUT_CSV = 'outputs/wallet_scores.csv'
OUTPUT_PLOT = 'outputs/score_distribution.png'


def main():
    # Load and preprocess
    print("\nLoading and preprocessing data...")
    features_df = load_and_engineer_features(INPUT_PATH)

    # Score
    print("\nScoring wallets...")
    scores_df = score_wallets(features_df)

    # Save outputs
    os.makedirs('outputs', exist_ok=True)
    scores_df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nSaved scores to: {OUTPUT_CSV}")

    # Plot and save distribution
    save_distribution_plot(scores_df, OUTPUT_PLOT)
    print(f"Saved score distribution plot to: {OUTPUT_PLOT}")


if __name__ == '__main__':
    main()
