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
        var e = document.getElementById("DISPLAY").innerHTML = `Loading Water Data....`
        // e.textContent = payload

        var temp, outflow, description;
        var content = JSON.parse(payload);
        
        var laketext = `${content.lakes.MelvernLake.description} temp is ${content.lakes.MelvernLake.temp}.  Spillway ${content.lakes.MelvernLake.outflow} cfm.<br>`;
        var riverjson = content.rivers;
        var rivertext = ``;
        for (let i = 0; i < riverjson.length; i++) {
          var rtext = `${i.description} is ${i.height} above guage with ${i.flow} cfm flow. <br>`
          rivertext += rtext;
        }

        e.innerHTML = 
        `Current Lake and River Conditions<br>
        ${laketext}
        ${rivertext}
        `;

        
        break
    }
  },
})