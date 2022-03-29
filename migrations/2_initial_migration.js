const FilePermissions = artifacts.require("FilePermissions");

module.exports = function (deployer) {
    deployer.deploy(FilePermissions);
};
