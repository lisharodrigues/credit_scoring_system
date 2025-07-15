import matplotlib.pyplot as plt
import os

def save_distribution_plot(scores_df, output_path):
    plt.figure(figsize=(10, 6))
    bins = list(range(0, 1100, 100))
    plt.hist(scores_df['score'], bins=bins, edgecolor='black', color='skyblue')
    plt.title("Credit Score Distribution")
    plt.xlabel("Score Range")
    plt.ylabel("Number of Wallets")
    plt.grid(True, linestyle='--', alpha=0.6)

    # Save the plot
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
