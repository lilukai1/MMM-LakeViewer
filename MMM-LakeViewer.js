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
        
        var meldescription = `${content.lakes.MelvernLake.description}`        
        var meltemp = ` temp is: ${content.lakes.MelvernLake.temp}.  `;
        var meloutflow = `Spillway: ${content.lakes.MelvernLake.outflow}. `;
        var pomdescription = `${content.lakes.PomonaLake.description}`        
        var pomtemp = ` temp is: ${content.lakes.PomonaLake.temp}.  `;
        var pomoutflow = `Spillway: ${content.lakes.PomonaLake.outflow}. `;
        e.textContent = `${content.MelvernLake.description} temp is ${content.MelvernLake.temp}.  Spillway ${content.MelvernLake.outflow}.
        ${content.PomonaLake.description} temp is ${content.PomonaLake.temp}.  Spillway ${content.PomonaLake.outflow}.`
        break
    }
  },
})