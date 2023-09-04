# Transaction Generator

This project can generate randomized cryptocurrency transactions or token bridges between specified wallet addresses. It is intended to provide sample transaction data for testing purposes.

## Overview

The application is structured as follows:

- `config.py` - Defines configuration settings like wallet addresses, API keys, etc
- `utils.py` - Helper functions for generating random values 
- `send.py` - Logic for sending direct Ethereum transactions
- `bridge.py` - Logic for bridging ERC20 tokens across chains
- `app.py` - The main application loop

## Usage

1. Update `config.py` with your Infura project ID, wallet addresses, and other settings.  

2. Implement the transaction and token bridge logic in `send.py` and `bridge.py`. Refer to the Web3 and protocol docs.

3. Run `python app.py` to start generating randomized transactions.

The app continually loops, randomly selecting wallet pairs, amounts, and delays between transfers.

## Monitoring

- The script currently outputs simple logging messages.

- For advanced monitoring, integration with tools like Prometheus is recommended. 

## Configuration

The `config.py` file contains several settings that can be tuned:

- `WALLETS` - List of wallet addresses to choose from
- `TOKEN_ADDRESS` - Contract address of the token to send
- `MIN_AMOUNT` - Minimum random amount to transfer
- `MAX_AMOUNT` - Maximum random amount to transfer  
- ...

## Troubleshooting

Errors from the transaction and bridging logic are caught and logged. Some common issues:

- Invalid wallet private keys or insufficient funds  
- Network issues connecting to Infura
- Errors in the underlying send/bridge implementations
- Incorrect nonce values if transactions are not sequenced properly

## Future Improvements

Possible enhancements include:

- Web UI for configuring and monitoring
- Dynamic wallet and token selection
- Failure injection for robustness testing
- Scheduled execution via cron/Celery/Kubernetes

Let me know if you have any other questions!