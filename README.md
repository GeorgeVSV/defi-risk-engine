# DeFi RISK Engine

## Overview
DeFi RISK Engine is an **open-source risk modeling tool** for DeFi protocols, designed to assess institutional lending risks using raw on-chain data. The project focuses on **modular, autonomous, and scalable** risk computation, starting with Health Factor (HF) prediction.

## Key Features
- **Raw On-Chain Data** – No third-party APIs, ensuring institutional-grade reliability.
- **Modular OOP Architecture** – Separate classes for fetching, processing, and modeling.
- **Extensible Risk Models** – Initial focus on Health Factor (HF) calculations.
- **Open Source & Transparent** – Built in public for collaboration and industry credibility.
- **Integrated Data Collection** – Uses `DeFi Data Collectors` as a submodule for on-chain data.

## MVP Goals
The first milestone is to develop a **functional Risk Engine** that:
1. Fetches raw on-chain data directly (collateral price, loan value, liquidation threshold, etc.).
2. Identifies **institutional wallets** (hedge funds, investment firms).
3. Computes **historical Health Factor (HF)** for these wallets based on their positions.
4. Structures this data into a clean dataset for analysis.
5. Integrates an initial **Risk Model** to analyze HF trends and potential liquidation risks.

## Project Structure
```
-engine/
│── data_collectors/        # Submodule for fetching raw blockchain data
│── data_processing/        # Processes fetched data into structured format
│   ├── processor.py
│   ├── __init__.py
│
│── risk_core/              # Risk Engine logic (actual risk models)
│   ├── risk_model.py
│   ├── __init__.py
│
│── tests/                  # Unit tests for each module
│
│── config.py               # Configurations (RPCs, addresses)
│── requirements.txt        # Dependencies
│── README.md               # Documentation
│── .gitignore              # Ignore unnecessary files
```

## Installation
```bash
# Clone the repository
git clone --recursive https://github.com/yourusername/risk-engine.git
cd risk-engine

# Initialize and update submodules
git submodule update --init --recursive

# Install dependencies
pip install -r requirements.txt
```

## Usage
Updating the **[DeFi Data Collectors](https://github.com/GeorgeVSV/defi-data-collectors.git)** submodule
If the DeFi Data Collectors repo is updated, sync it in the Risk Engine:
```bash
git submodule update --remote
```

## Contributing
We welcome contributions! If you're interested in improving risk models or blockchain data processing, feel free to submit PRs or open discussions.

## License
[MIT License](LICENSE)

