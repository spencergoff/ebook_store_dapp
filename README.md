# Decryption Service

This service downloads a file with a given content ID from IPFS (a decentralized storage protocol) and decrypts it using a secret key. 

Decryption only occurs if the user/wallet calling the service has been granted access to the file, as defined in the smart contract.

A user can obtain access to the file by sending 1000 wei (the smallest denomination of Ethereum) to the smart contract.

The decryption service is defined in the decryption_service directory, and the business logic is in download_decrypt.py. 

The service is currently deployed on a centralized platform, AWS, until I can find a decentralized solution to storing the secret key. Specifically, it's deployed in a Docker-based Lambda function as defined in sam_template.yaml and Dockerfile. The secret key is stored in AWS Secrets Manager. 

The encrypted file is pinned using Pinata, an IPFS pinning service, to ensure that it is always available. 


