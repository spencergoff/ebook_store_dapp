document.getElementById('connectButton', connect);

function connect() {
    console.log('Handling connect() event');
    ethereum
        .request({ method: 'eth_requestAccounts' })
        .then(function (accountInfo) {
            var address = accountInfo[0];
            console.log('The requester\'s wallet address is: ' + address);
            var api_request = new XMLHttpRequest();
            url = 'https://i4d36m961a.execute-api.us-west-2.amazonaws.com/Prod?address=' + address
            api_request.open('GET', url, true);  // `true` makes the request asynchronous
            alert('Trying to send api_request to ' + url)
            api_request.send()

            api_request.onload = function () {
                console.log('Loading...')
            };

            api_request.onprogress = function (event) {
                console.log('Progressing...')
            };

            api_request.onerror = function () {
                alert('There was an error. request.status: ' + api_request.status + ' | request.responseText: ' + api_request.responseText)
            };
        })
        .catch((error) => {
            alert('Error: ' + error.code)
            if (error.code === 4001) {
                console.log('Please connect to MetaMask.');
            } else {
                console.error(error);
            }
        });
}
