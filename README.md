# Smart Contract

The core of this project is a smart contract written in Solidity and deployed to the Ethereum-based testnet Görli.

The contract accepts payments in Eth and if the amount sent is at least 1000 wei, then the sender obtains permission to see the secret message (more on this later). 

There are functions that allow other services to check the balance of the contract, get the list of customers (i.e. the wallet addresses with permission to see the secret message), and deposit Eth.

This smart contract is defined in contract/permissions.sol. At the time of this writing, info about the latest deployment can be found at https://goerli.etherscan.io/address/0x0147fe45f5d96a6d0055bc89721f25da514e6aac.

# Decryption Service

This service downloads a file with a given content ID from IPFS (a decentralized storage protocol) and decrypts it using a secret key. 

Decryption only occurs if the user/wallet calling the service has been granted access to the file, as defined in the smart contract.

A user can obtain access to the file by sending 1000 wei (the smallest denomination of Ethereum) to the smart contract.

The decryption service is defined in the decryption_service directory, and the business logic is in download_decrypt.py. 

The service is currently deployed on a centralized platform, AWS, until I can find a decentralized solution to storing the secret key. Specifically, it's deployed in a Docker-based Lambda function as defined in sam_template.yaml and Dockerfile. The secret key is stored in AWS Secrets Manager. 

The encrypted file is pinned using Pinata, an IPFS pinning service, to ensure that it is always available. 
