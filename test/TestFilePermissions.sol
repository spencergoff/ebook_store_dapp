// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/FilePermissions.sol";

contract TestFilePermissions {

    uint public initialBalance = 1 ether;
    event LogAddressArray(string arrayName, address[] addressArray);

    function testNewSender_whenSendingSufficientFunds_shouldBeAddedToCustomers() public {
        FilePermissions filePermissions = FilePermissions(DeployedAddresses.FilePermissions());
        filePermissions.deposit{value:1002}();
        address[] memory actualValue = filePermissions.get_customers();
        address[] memory expectedValue = new address[](1);
        expectedValue[0] = address(this);
        emit LogAddressArray("actualValue", actualValue);
        emit LogAddressArray("expectedValue", expectedValue);
        Assert.equal(actualValue, expectedValue, "Error: New sender wasn't added to customers[]");
    }
}