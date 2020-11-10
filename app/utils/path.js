const path = require("path");


// this allow us to get the root directory name 
module.exports = path.dirname(process.mainModule.filename);
