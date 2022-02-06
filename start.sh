function main {
    python3 download_decrypt.py
    gpg --yes --batch --passphrase=$secret_value test.txt.gpg
}

main