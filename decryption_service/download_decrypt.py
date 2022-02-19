import json
import boto3
import requests
from web3 import Web3
from cryptography.fernet import Fernet

def main(event, context):
    print(f'event: {event}')
    content_id = 'QmXjvurAQ3MLpxGQM6NvdgPC8uK1YndmEBmRzCEJJUgEz2'
    test_string_comparison()
    requester_wallet_address = extract_address_from_event(event)
    requester_has_access = check_if_requester_has_access(requester_wallet_address)
    print(f'requester_has_access: {requester_has_access}')
    if requester_has_access == True:
        key = get_key('ebook_decryption_secret')
        decrypted_message = decrypt_content_with_key(content_id, key)
        body = f'The secret message is: {decrypted_message}'
    else:
        body = 'You do not have access to view the secret message. Try sending 1000 wei to 0x0147fe45f5d96a6d0055bc89721f25da514e6aac'
    headers = {
        'Access-Control-Allow-Origin': 'http://ebookstoredappbucket.s3-website-us-west-2.amazonaws.com'
    }
    response = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': headers,
        'body': body
    }
    print(f'response: {response}')
    return response

def test_string_comparison():
    string1 = '0xasdf'
    string2 = '0xasdf'
    print(f'string1: {string1} | string2: {string2}')
    if string1 == string2:
        print('The strings are equal!')
    else:
        print('The strings are NOT equal.')

def extract_address_from_event(event):
    address = str(event['queryStringParameters']['address'])
    print(f'Requester address: {address}')
    return address

def check_if_requester_has_access(requester_wallet_address):
    print(f'Checking if requester has access: {requester_wallet_address}')
    deployed_contract_address = Web3.toChecksumAddress('0x0147fe45f5d96a6d0055bc89721f25da514e6aac')
    contract_file_path = 'permissions.sol'
    application_binary_interface = get_application_binary_interface(contract_file_path)
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/e5b0c5087555433a8b4e82cc739bc0ab'))
    deployed_contract = w3.eth.contract(address=deployed_contract_address, abi=application_binary_interface)
    wallet_addresses_with_permission = list(deployed_contract.functions.get_customers().call())
    print(f'wallet_addresses_with_permission: {wallet_addresses_with_permission}')
    if str(wallet_addresses_with_permission[0]).strip() != str(requester_wallet_address).strip():
        print('The requesting wallet does NOT have permission to access the secret message.')
        print(f'str(wallet_addresses_with_permission[0]).strip(): {str(wallet_addresses_with_permission[0]).strip()} | str(requester_wallet_address).strip(): {str(requester_wallet_address).strip()}')
        print(f'len(requester_wallet_address): {len(requester_wallet_address)} | len(wallet_addresses_with_permission[0]): {len(wallet_addresses_with_permission[0])}')
        return False
    else:
        print('The requesting wallet has permission to access the secret message.')
        return True

def get_application_binary_interface(contract_file_path):
    with open('compiled_contract.json', 'r') as file:
        compiled_sol = json.load(file)
    application_binary_interface = compiled_sol['contracts'][contract_file_path]['FilePermissions']['abi']
    return application_binary_interface

def decrypt_content_with_key(content_id, key):
    f = Fernet(key)
    url = f'https://ipfs.io/ipfs/{content_id}'
    print(f'Trying to get encrypted message from: {url}')
    encrypted_message = requests.get(url).text
    encrypted_message_as_bytes = encrypted_message.encode('utf-8')
    decrypted_message = f.decrypt(encrypted_message_as_bytes)
    print(f'decrypted_message: {decrypted_message}')
    return decrypted_message

def get_key(secret_name):
    print(f'Made it to get_secret with secret_name: {secret_name}')
    region_name = 'us-west-2'
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    secret_payload = client.get_secret_value(SecretId=secret_name)
    secret_value = extract_secret_from_payload(secret_name, secret_payload)
    return secret_value

def extract_secret_from_payload(secret_name, secret_payload):
    try:
        all_secrets = json.loads(secret_payload['SecretString'])
    except:
        secret_value = secret_payload['SecretString']
    else:
        secret_value = all_secrets[secret_name]
    return secret_value

def encrypt_message(message):
    print(f'message to encrypt: {message}')
    encrypted_file_path = '/tmp/fernet_encrypted.txt'
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message)
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_message)
        print(f'Wrote the encrypted message to {encrypted_file_path}')

if __name__ == '__main__':
    main(None, None)