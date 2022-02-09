document.getElementById('connectButton', connect);

function connect() {
    ethereum
        .request({ method: 'eth_requestAccounts' })
        .then(function (accountInfo) {
            var address = accountInfo[0]
            alert('Account address: ' + address)
        })
        .catch((error) => {
            if (error.code === 4001) {
                // EIP-1193 userRejectedRequest error
                console.log('Please connect to MetaMask.');
            } else {
                console.error(error);
            }
        });
}
