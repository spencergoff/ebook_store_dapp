// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/FilePermissions.sol";

contract TestFilePermissions {

    uint public initialBalance = 1 ether;
    event LogAddressArray(string arrayName, address[] addressArray);
    event LogOwner(address payable owner);
    FilePermissions filePermissions = FilePermissions(DeployedAddresses.FilePermissions());
    
    function testNewSender_whenSendingSufficientFunds_shouldBeAddedToCustomers() public {
        filePermissions.deposit{value:1002}();
        address[] memory actualCustomers = filePermissions.get_customers();
        address[] memory expectedCustomers = new address[](1);
        expectedCustomers[0] = address(this);
        emit LogAddressArray("actualCustomers", actualCustomers);
        emit LogAddressArray("expectedCustomers", expectedCustomers);
        Assert.equal(actualCustomers, expectedCustomers, "Error: New sender wasn't added to customers[]");
    }

    function testNewSender_whenSendingInsufficientFunds_shouldNotBeAddedToCustomers() public {
        filePermissions.remove_self_from_customers();
        filePermissions.deposit{value:999}();
        address[] memory actualCustomers = filePermissions.get_customers();
        address[] memory expectedCustomers = new address[](1);
        expectedCustomers[0] = address(0x0000000000000000000000000000000000000000);
        emit LogAddressArray("actualCustomers", actualCustomers);
        emit LogAddressArray("expectedCustomers", expectedCustomers);
        Assert.equal(actualCustomers, expectedCustomers, "Error: Unpaid customer was added to customers[]");
    }
}