# Wallet Credit Scoring

This project builds a robust, rule-based credit scoring system for wallets interacting with the Aave V2 DeFi protocol. It uses historical on-chain transaction behavior to generate credit scores between **0 and 1000**, where higher scores reflect responsible, non-exploitative activity.

---

## Project Structure

```
aave-credit-scoring/
├── data/                          # Input data (JSON file)
│   └── user_transactions.json
├── outputs/                       # Results
│   ├── wallet_scores.csv
│   └── score_distribution.png
├── src/                           # Modular logic
│   ├── preprocess.py              # JSON parser & feature engineer
│   ├── scoring.py                 # Rule-based credit score generator
│   └── utils.py                   # Plotting utilities
├── exploratory_analysis.ipynb     # Score analysis and distribution
├── score_users.py                 # Main runner script
├── requirements.txt               # Python dependencies
└── README.md                      # You're here
```

---

## Input

The input is a JSON file with raw transaction-level data for DeFi wallets. Each record includes wallet ID, action (`deposit`, `borrow`, `repay`, etc.), timestamp, and metadata nested under `actionData`.

Example:

```json
{
  "userWallet": "0x123...",
  "timestamp": 1612345678,
  "action": "deposit",
  "actionData": {
    "amount": "1000",
    "type": "stablecoin"
  }
}
```

---

## How It Works

1. **Preprocessing** (`src/preprocess.py`):

   * Flattens nested fields (`actionData`)
   * Converts timestamps
   * Computes features like total deposits, borrow amounts, repay ratios, etc.

2. **Scoring Logic** (`src/scoring.py`):

   * Scores wallets from 0–1000 based on:

     * Repay-to-borrow ratio
     * Liquidation ratio
     * Total deposits (normalized)
     * Active usage days

3. **Execution**:

```bash
# 1. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the pipeline
python score_users.py
```

---

## Output

* `outputs/wallet_scores.csv` – Wallets with final credit scores
* `outputs/score_distribution.png` – Score distribution plot

---

## Explore the Results

Open `exploratory_analysis.ipynb` to:

* Visualize score distribution
* Analyze high (≥800) vs. low (≤200) scorers

---

## Example Feature Calculations (per wallet)

* `num_txns`: Number of transactions
* `active_days`: Unique active days
* `repay_to_borrow_ratio`: Measures responsibility
* `liquidation_ratio`: Higher → riskier behavior

---

## Contributions & Extensions

* You can extend the scoring logic with machine learning (e.g., Random Forest)
* Add fraud detection heuristics
* Integrate real-time scoring using APIs

---

## Author Notes

* This project uses a simplified scoring model for clarity and interpretability.


---

