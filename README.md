# Web Client

To interact with this project, users can go to http://ebookstoredappbucket.s3-website-us-west-2.amazonaws.com/. 

![Screen Shot 2022-02-19 at 10 45 09 AM](https://user-images.githubusercontent.com/14855088/154814611-c75c2f07-d067-46f2-818f-3539e7e139cf.png)

A user with the MetaMask plugin installed and logged in can click the "Download content" button and see an alert that either displays the decrypted secret message or informs them that they don't have access and should send wei to the smart contract.

![Screen Shot 2022-02-19 at 10 49 52 AM](https://user-images.githubusercontent.com/14855088/154814752-2b160747-7f65-492e-af4b-02672f66667b.png)

The code for this client is in the "client" directory. It is currently deployed in an AWS S3 bucket, but I'm planning to migrate it to IPFS or similar in the future to make it more decentralized. 

# Smart Contract

The core of this project is a smart contract written in Solidity and deployed to the Ethereum-based testnet Görli.

The contract accepts payments in Eth and if the amount sent is at least 1000 wei, then the sender obtains permission to see the decrypted message (eventually this will be entire files such as ebooks and PDFs). 

There are functions that allow other services to check the balance of the contract, get the list of customers (i.e. the wallet addresses with permission to see the secret message), and deposit Eth.

This smart contract is defined in contract/permissions.sol. At the time of this writing, info about the latest deployment can be found at https://goerli.etherscan.io/address/0x0147fe45f5d96a6d0055bc89721f25da514e6aac.

# Decryption Service

This service is invoked by the client when the "Download content" button is clicked. It asks the smart contract if the user has permission to view the secret message and if they do, then the service downloads the file (the "secret message") from IPFS (a decentralized storage protocol) and decrypts it using the secret key. 

A user can obtain permission to view the secret message by sending 1000 wei (the smallest denomination of Ethereum) to the smart contract.

The decryption service is defined in the decryption_service directory, and the business logic is in download_decrypt.py. 

The service is currently deployed on a centralized platform, AWS, until I can find a decentralized solution to storing the secret key. Specifically, it's deployed in a Docker-based Lambda function as defined in sam_template.yaml and decryption_service/Dockerfile. The secret key is stored in AWS Secrets Manager. 

The encrypted file is pinned using Pinata, an IPFS pinning service, to ensure that it is always available.


