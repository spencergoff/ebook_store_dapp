import json
import boto3
import gnupg
import pickle
import requests

print('Executing the global commands...')
gpg = gnupg.GPG(verbose=True)
file_hash = 'QmdLMnwpbi8xPFcpRGqsfHCRGVgovV3yAv8fUtoug66Wqj'
encrypted_file_path = '/tmp/encrypted_file.txt'
decrypted_file_path = '/tmp/decrypted_file.txt'
gpg.encoding = 'utf-8'


def main(event, context):
    download_file()
    decrypt_the_file()

def download_file():
    file_response = requests.get(f'https://ipfs.io/ipfs/{file_hash}')
    print(f'file_response.text: {file_response.text}')
    with open(encrypted_file_path, 'w') as f:
        f.write(file_response.text)

def decrypt_the_file():
    print('Made it to decrypt_file!')
    secret = get_secret('ebook_decryption_secret')
    print(f'len(secret): {len(secret)}')
    with open(encrypted_file_path, 'r+') as f:
        encrypted_string = str(f.read())
    print(f'encrypted_string: {encrypted_string}')
    f = open(decrypted_file_path,"w+").close()
    decryption = gpg.decrypt(message=encrypted_string, passphrase=secret, always_trust=True)
    print(f'decryption.status: {decryption.status} | decryption.ok: {decryption.ok} | decryption.data: {decryption.data}')
    with open(decrypted_file_path, 'w+') as f:
        f.write(str(decryption))
        print(f'decrypted_file: {f.read()}')

def get_secret(secret_name):
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

if __name__ == '__main__':
    main(None, None)