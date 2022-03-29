// SPDX-License-Identifier: MIT

pragma solidity ^0.8.4;

contract FilePermissions {

    address payable public owner;
    address[] public customers;
    uint256 price_of_file = 1000;

    constructor() {
        owner = payable(msg.sender);
    }

    function deposit() public payable {
        if (msg.value >= price_of_file && !is_customer(msg.sender)) {
            customers.push(msg.sender);
        }
    }

    function is_customer(address wallet_address) private view returns (bool) {
        for (uint256 i = 0; i < customers.length; i++) {
            if (customers[i] == wallet_address) {
                return true;
            }
        }
        return false;
    }

    function get_customers() public view returns (address[] memory) {
        return customers;
    }

    function get_contract_balance() public view returns (uint256) {
        return address(this).balance;
    }

    function remove_self_from_customers() external {
        for (uint256 i = 0; i < customers.length; i++) {
            if (customers[i] == msg.sender) {
                delete customers[i];
                break;
            }
        }
    }

}
