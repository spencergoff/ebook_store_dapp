#!/bin/bash
set -ex

function main {
    file_hash="QmdLMnwpbi8xPFcpRGqsfHCRGVgovV3yAv8fUtoug66Wqj"
    check_internet_connection
    setup_ipfs
    #add_pinata_peers
    echo "~/.ipfs/config: "
    cat ~/.ipfs/config
    download_file
    decrypt_file
}

function check_internet_connection {
    connectivity=$(ping -q -c1 8.8.8.8 &>/dev/null && echo online || echo offline)
    echo "connectivity: $connectivity"
    # if [[ $connectivity == "offline" ]]; then
    #     exit 1
    # fi
}

function setup_ipfs {
    ipfs init
    ipfs daemon &
    sleep 2
}

function add_pinata_peers {
    original_ipfs_confg=$(cat ~/.ipfs/config)
    pinata_peers=$(cat pinata_peers.json)
    jq '.Peering.Peers = "$pinata_peers"' <<< "$original_ipfs_confg"
    echo "$original_ipfs_confg" > ~/.ipfs/config
}

function download_file {
    ipfs get $file_hash
}

function decrypt_file {
    echo "Trying to decrypt $file_hash..."
    gpg $file_hash
}

main
