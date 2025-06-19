# BotanixTestnet

Automated Faucet Coin Claiming for Botanix Testnet

## Overview

BotanixTestnet is a Python-based project designed to automate claiming testnet tokens for the Botanix EVM-compatible Spiderchain built on Bitcoin. Botanix Labs is pioneering Bitcoin Layer 2 scaling with its Spiderchain, an EVM-equivalent Layer 2 secured by decentralized multisig wallets (Orchestrator nodes) and leveraging Proof-of-Stake consensus while settling on Bitcoin’s base layer.

This repository provides scripts to help developers and testers easily acquire testnet coins from the Botanix faucet and interact with the Spiderchain testnet.

## About Botanix

- EVM-equivalent Layer 2 network built on Bitcoin  
- Uses Spiderchain: decentralized multisig wallets securing bridged BTC  
- Enables Ethereum-compatible dApp development on Bitcoin  
- Proof-of-Stake consensus with Bitcoin finality  
- Supports bridging BTC on and off the Layer 2 chain  

Learn more at [Botanix Labs website](https://botanixlabs.xyz/en/testnet) and explore the Aragog testnet, the latest Spiderchain testnet phase.

## Features

- Automated faucet claiming of Botanix testnet tokens  
- Python scripts for easy setup and usage  
- Supports testing and development on the Spiderchain Bitcoin L2  

## Getting Started

### Prerequisites

- Python 3.7 or higher  
- Install dependencies:

```
pip install -r requirements.txt
```

### Installation

1. Clone the repository:

```
git clone https://github.com/piobox2001/BotanixTestnet.git
cd BotanixTestnet
```

2. Install required Python packages as above.

3. Configure your testnet wallet address in the script (`botax.py`) or as instructed.

### Usage

Run the faucet claiming script:

```
python botax.py
```

This will interact with the Botanix faucet to request testnet tokens.

## Resources

- [Botanix Labs Testnet Portal](https://botanixlabs.xyz/en/testnet)  
- [Aragog Testnet Announcement](https://botanixlabs.xyz/en/blog/aragog-testnet-launch)  
- [Botanix Documentation and Roadmap](https://botanixlabs.xyz/en/roadmap)  
- [Add Botanix Testnet to MetaMask via Chainlist](https://chainlist.org/chain/3636)  

## Contributing

Contributions are welcome! Please open issues or submit pull requests to improve the scripts or add features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

