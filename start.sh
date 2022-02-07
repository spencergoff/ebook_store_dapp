function main {
    python3 get_secret.py
    gpg --yes --batch --passphrase=$secret_value test.txt.gpg
}

main