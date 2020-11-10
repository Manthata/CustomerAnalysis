// const cv = require('opencv')
const height = 100; // height
const width = 100; // width
const devicePort = 0;
const rootDir = require("../utils/path");
const bufferConv = require("../utils/bufferConverter")
const io = require('../routes/socket');
const socket = require("../routes/socket");
const { emit } = require("process");


const FPS = 23;
// const vCap = new cv.VideoCapture(devicePort)
// vCap.set(cv.CAP_PROP_FRAME_WIDTH, 300)
// vCap.set(cv.CAP_PROP_FRAME_HEIGHT, 300)
exports.gethome = (req, res, next) => {
    const cvNameSpace = io.getIO().of("/cv")
    const webNameSpace = io.getIO().of("/web")
    const websock = []
   

    // connect to the web client channel 
    webNameSpace.on("connect", socket => {
        websock.push({
            "socketID": socket.id,
            "socketObject": socket
        })
        socket.on("hello", data => {
            //console.log(websock[0]["socketObject"])
            console.log(data)
        })
        // socket.on("cv2server", data => {
        //     console.log(data)
        // })
        console.log("[INFO] web clinet connected")
    })           // connect to the cv channel 
    cvNameSpace.on("connect", socket => {
        console.log("[INFO] cv app connected")
        let client = []
        websock.forEach(element => {
            client = element["socketObject"]
           // console.log(client.length())
        });
        socket.on("cv2server", data => {
            client.emit("image", data)
            //console.log("[INFO] we are in the stream")
            // console.log(socket)
        })

    })


    // io.getIO().on("connect", socket => {
    //     socket.on("cv2server", (message) => {
    //         console.log(message.image)
    //         io.getIO.emit("image", message)
    //         // web.emit("image", message)
    //     })
    //     console.log("[INFO]connected to the cv client")

    // })

    res.render("live")
        
}

exports.getLive = (req, res, next) => {
    
}


