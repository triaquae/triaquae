$(document).ready(function () {
    $.getJSON(
    	"/GetServers",
        function (json) {
        window['t'] = $("#tree1").ligerTree({
               nodeDraggable: false,
               data: json,
               idFieldName: "id",
               parentIDFieldName: "pid"
            });
         });
         manager = $("#tree1").ligerGetTreeManager();
     });
    var getManager = (function () {
        var manager = null;
        return function doGet() {
       	       if (!manager) {
                   manager = $("#tree1").ligerGetTreeManager();
               }
		return manager;
	 }
       })();
function getDatas(){
	 if(manager){
//		 alert(1);
	 }
	 var nodes =getManager().getChecked();
	 var text=[];
	 for(var i=0;i<nodes.length;i++){
		if(!nodes[i].data.bgroup) 
			text.push(nodes[i].data.ip);
	 }
	// alert(text.join(","));
	return text;
 }  
