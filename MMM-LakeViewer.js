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
        // e.textContent = payload

        var temp, outflow, description;
        var content = JSON.parse(payload)
        
        e.innerHTML = `${content.lakes.MelvernLake.description} temp is ${content.lakes.MelvernLake.temp}.  Spillway ${content.lakes.MelvernLake.outflow}.<br>
        ${content.lakes.PomonaLake.description} temp is ${content.lakes.PomonaLake.temp}.  Spillway ${content.lakes.PomonaLake.outflow}.<br>
        Salt Creek is at ${content.SaltCreek.height} ft with ${content.SaltCreek.flow} cfm flow`
        break
    }
  },
})