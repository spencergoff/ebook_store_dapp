document.getElementById('connectButton', connect);

function connect() {
    alert('Made it to connect()');
    ethereum
        .request({ method: 'eth_requestAccounts' })
        .then(function (accountInfo) {
            var address = accountInfo[0];
            alert('Account address: ' + address);
            var api_request = new XMLHttpRequest();
            alert('Trying to open api_request...');
            api_request.open('GET', 'https://i4d36m961a.execute-api.us-west-2.amazonaws.com/Prod?address=123', true);  // `false` makes the request synchronous
            alert('Trying to send api_request...')
            api_request.send()

            api_request.onload = function () {
                alert('Made it inside onload')
                alert('request.status: ' + api_request.status + ' | request.responseText: ' + api_request.responseText);
            };

            api_request.onprogress = function (event) {
                alert('Made it inside onprogress')
                alert('request.status: ' + api_request.status + ' | request.responseText: ' + api_request.responseText);
            };

            api_request.onerror = function () {
                alert('Made it inside onerror')
                alert('request.status: ' + api_request.status + ' | request.responseText: ' + api_request.responseText);
            };
        })
        .catch((error) => {
            alert('Error: ' + error.code)
            if (error.code === 4001) {
                // EIP-1193 userRejectedRequest error
                console.log('Please connect to MetaMask.');
            } else {
                console.error(error);
            }
        });
}
