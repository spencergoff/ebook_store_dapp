import json
import boto3
import requests
from cryptography.fernet import Fernet

def main(event, context):
    content_id = 'QmXjvurAQ3MLpxGQM6NvdgPC8uK1YndmEBmRzCEJJUgEz2'
    key = get_key('ebook_decryption_secret')
    decrypted_message = decrypt_content_with_key(content_id, key)
    response = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'body': decrypted_message
    }
    return response

def decrypt_content_with_key(content_id, key):
    f = Fernet(key)
    url = f'https://ipfs.io/ipfs/{content_id}'
    print(f'Trying to get encrypted message from: {url}')
    encrypted_message = requests.get(url).text
    encrypted_message_as_bytes = encrypted_message.encode('utf-8')
    decrypted_message = f.decrypt(encrypted_message_as_bytes)
    print(f'decrypted_message: {decrypted_message}')
    decrypted_message

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