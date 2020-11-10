let io;

module.exports = {
    init: httpServer => {
        io = require("socket.io")(httpServer)
        return io
    },
    getIO: () => {
        if(!io) {
            throw new Error('io not initialized')
        }
        return io
    },
    // getCv: route => {
    //     io.of(route, socket => {
    //         console.log("[Connected to the cv app]")

    //         return socket

    //     })
    // }
}