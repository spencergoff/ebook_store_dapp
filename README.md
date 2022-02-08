# Decryption Service

The decryption service is defined in download_decrypt.py. It downloads a file with a given content ID from IPFS (a decentralized storage protocol) and decrypts it using a secret key. 

Eventually, the decryption will only occur if the user/wallet calling the service has been granted access to the file, as defined in a smart contract. 

The service is currently deployed on a centralized platform, AWS, until I can find a decentralized solution to storing the secret key. Specifically, it's deployed in a Docker-based Lambda runtime as defined in sam_template.yaml. The secret key is stored in AWS Secrets Manager. 

The file is pinned using Pinata, an IPFS pinning service. 


