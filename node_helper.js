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
    var process = spawn("python", ["/MagicMirror/modules/MMM-LakeViewer.py"])
    process.stdout.on("data", (data)=>{
      console.log(data)
      var result = String.fromCharCode.apply(null, new Uint16Array(data))
      this.sendSocketNotification("HERE_IS_DATA", data)
    })
  }
})