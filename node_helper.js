/// node_helper.js
///"""copied from: https://forum.magicmirror.builders/topic/9591/python-in-to-the-magic-mirror"""

const spawn = require("child_process").spawn
var NodeHelper = require("node_helper")

module.exports = NodeHelper.create({
  socketNotificationReceived: function(notification, payload) {
    switch(notification) {
      case "GIVE_ME_DATA":
        this.job()
        break
    }
  },
  job: function() {
    // var process = spawn("python", ["/home/pi/MagicMirror/modules/MMM-LakeViewer/MMM-LakeViewer.py"])
    var process = spawn("python", ["C:/Users/Annie/Documents/GitHub/RaspberryPiProjects/MMM-LakeViewer/MMM-LakeViewer.py"])

    process.stdout.on("data", (data)=>{
      console.log(data)
      var result = String.fromCharCode.apply(null, new Uint16Array(data))
      // var result = data.
      myjson= JSON.parse(result)
      this.sendSocketNotification("HERE_IS_DATA", myjson)
      console.log(myjson.Data)
    })
  }
})