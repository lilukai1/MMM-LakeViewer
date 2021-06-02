/// MMM-P2000.js
///"""copied from: https://forum.magicmirror.builders/topic/9591/python-in-to-the-magic-mirror"""

Module.register("MMM-LakeViewer", {
  getDom: function() {
    var e = document.createElement("div")
    e.id = "DISPLAY"
    return e
  },
  notificationReceived: function(notification, payload, sender) {
    switch(notification) {
      case "DOM_OBJECTS_CREATED":
        var timer = setInterval(()=>{
          this.sendSocketNotification("GIVE_ME_DATA")
        }, 1000)
        break
    }
  },
  socketNotificationReceived: function(notification, payload) {
    switch(notification) {
      case "HERE_IS_DATA":
        var e = document.getElementById("DISPLAY")
        e.textContent = payload

        var temp, outflow, description;
        var content = JSON.parse(payload)
        var description = `${content.description}`        
        temp = ` temp is: ${content.temp}.  `;
        outflow = `Spillway: ${content.outflow}. `;
        var texts = temp+outflow
        e.textContent = `${description} temp is ${content.temp}.  Spillway ${content.outflow}.`
        break
    }
  },
})