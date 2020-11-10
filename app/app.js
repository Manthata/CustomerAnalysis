const express = require("express")
const app = express()
// const redis = require('redis');
    /* Values are hard-coded for this example, it's usually best to bring these in via file or environment variable for production */


//npm installations 
const bodyParser = require("body-parser")
const path = require("path")
const mongoose = require("mongoose")
// module for allowing us to access evironment variables
require("dotenv").config();



// Utilities
const rootDir = require("./utils/path")


//middleware 
const admin = require("./routes/admin");
const socket = require("./routes/socket");


app.set('view engine', 'ejs')
app.set('views', 'views')
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(rootDir, "public")))
app.use(admin)

// const client = redis.createClient({
//     port: 6379,           // replace with your port
//     host: "redis_server"        // replace with your hostanme or IP address
//     //password: 'your password',    // replace with your password
//     // optional, if using SSL
//     // use `fs.readFile[Sync]` or another method to bring these values in
//     // tls: {
//     //     key: stringValueOfKeyFile,
//     //     cert: stringValueOfCertFile,
//     //     ca: [stringValueOfCaCertFile]
//     // }
// });

// lets get the uri from env variable
DB_URI = "mongodb+srv://admin:Thesquarerootof9=3@cluster0.3lgkr.mongodb.net/CustomerData"
const port = 5000;
console.log(DB_URI)

 mongoose
    .connect(DB_URI, { useNewUrlParser: true }, { useUnifiedTopology: true } )
.then(results =>  {
    const server = app.listen(port, () => {
        console.log("running on Port: " + port)
    });
    const io = require("./routes/socket").init(server);
    // const redisAdapter = require('socket.io-redis');
    // io.adapter(redisAdapter({ host: 'localhost', port: 6379 }));
    
})
.catch(err => {
    console.log(err)
    alternative()
})

  alternative = () =>{
     const server = app.listen(port, () => {
          console.log("running on port: " + port)
      });
      const io = require("./routes/socket").init(server);
    //   const redisAdapter = require('socket.io-redis');
    //   io.adapter(redisAdapter({ host: 'localhost', port: 6379 }));
  }

