//(function(){
if (typeof CommandExecutePage == "undefined")
	CommandExecutePage={};	
	
(function(cmdObj){
	var command = "",remote_path = "",fileLists="";
	var username = "";
	cmdObj.runningcmd = false;
	cmdObj.track_mark =0;
	cmdObj.total_tasks =0;
	cmdObj.dangerousCmd = [];
	cmdObj.transfer_action=["SendFile","GetFile"];
	cmdObj.tags = [ "shutdown", "restart", "df", "cat", "du", "top", "iostat" ];	
	cmdObj.executeCommand =function(_command,_username,_computers,remotepath,filelists){
		command = _command;
		username = _username;
		remote_path = remotepath;
		fileLists = filelists;
		cmdObj.total_tasks = 0;
		cmdObj.track_mark  = 0;
		$("#totalnum").html(cmdObj.total_tasks);
		$("#failednum").html(0);
                $("#successnum").html(0); 
		if(cmdObj.transfer_action.indexOf(_command) != -1){
		//	command = _command;
		//	username = _username;
		//	remote_path = remotepath;
		//	fileLists = filelists;
		        $.post('/transferFile/', {IPLists:_computers.toString(),UserName:_username,command:_command,FileLists:filelists.toString(),RemotePath:remotepath}, function(data) {
                        	var json_data = JSON.parse(data);
	                        var totalNum = json_data.TotalNum,trackmark=json_data.TrackMark;
        	                cmdObj.total_tasks = parseInt(totalNum);
                	        cmdObj.track_mark = trackmark;
							cmdObj.runningcmd = true;
							$("#totalnum").html(cmdObj.total_tasks);
							$( "#progressbar .progress-label" ).text("0%");
                	});
		
		}
		else{
		        $.post('/runCmd/', {IPLists:_computers.toString(),UserName:_username,command:_command }, function(data) {
                      		var json_data = JSON.parse(data);
	                        var totalNum = json_data.TotalNum,trackmark=json_data.TrackMark;
        	                cmdObj.total_tasks = parseInt(totalNum);
                	        cmdObj.track_mark = trackmark;
							cmdObj.runningcmd = true;
							$("#totalnum").html(cmdObj.total_tasks);
							$( "#progressbar .progress-label" ).text("0%");
                	});
		}
		var updateProgress = cmdObj.InitProgressbar();
		setTimeout(updateProgress,2000);
		$("#stopprocess").attr("disabled",false);	
	};	
		
	cmdObj.stopExecution = function(){
		$.get('/stopExecution/',{TrackMark:cmdObj.track_mark},function(data){
			cmdObj.runningcmd = false;
			$("#stopprocess").attr("disabled",true);
		});
	};
	cmdObj.popDia = function(command,username,computers,remotepath,filelists) {
		var timertick =5,diagbody =  $("#dialog_body");
		if(computers.length == 0){
			diagbody.html("Please choose computers first.");
			$( "#dialog-confirm" ).dialog({
				resizable: false,
				height:240,
			//	width:500,
				modal: true,
				buttons: {
					"OK": function() {
							$( this ).dialog( "close" );
					}
				}	
			});
		return;			
		}
		if(command==""||typeof command =="undefined"){
			diagbody.html("You should type valid command first");
			$( "#dialog-confirm" ).dialog({
				resizable: false,
				height:240,
				modal: true,
				buttons: {
					"OK": function() {
							$( this ).dialog( "close" );
					}
				}
					
			});	

		}else{
			if((cmdObj.transfer_action)[0].indexOf(command) != -1 && filelists.length == 0){
        	                          diagbody.html("You should choose files first");
                	                $( "#dialog-confirm" ).dialog({
                        	                resizable: false,
                                	        height:240,
                                        	modal: true,
	                                        buttons: {
        	                                "OK": function() {
                	                                        $( this ).dialog( "close" );
                        	                	}
                               			 }

                               		 });
				return;

                        }
			var str= $("<div><p style='font-weight:bold;font-size:16px'> The command  ' "+ command +"' will be run in " +timertick+" seconds automatically!</p> <span id='cmdtimer' style='margin-left:46%;color:#ff6600;font-size:40px'>"+timertick+"</span></div>");	
			diagbody.html(str);
			var timer = setInterval(function(){
				var bodycontent = diagbody.find("#cmdtimer");
				timertick -=1;
				bodycontent.html(timertick);
				if(timertick==0){
					clearInterval(timer);
					$("#dialog-confirm").dialog("close");
					cmdObj.executeCommand(command,username,computers,remotepath,filelists);
				}
			},1000);
			
			$( "#dialog-confirm" ).dialog({
				resizable: false,
				height:260,
				modal: true,
				close:function(event,ui){
					clearInterval(timer);
				},
				buttons: {
					"Execute immediately": function() {
						$( this ).dialog( "close" );
						clearInterval(timer);
						cmdObj.executeCommand(command,username,computers,remotepath,filelists);
					},
					Cancel: function() {
						$( this ).dialog( "close" );
						clearInterval(timer);
					}
				}
			});
		}
	};
	cmdObj.InitProgressbar = function(){
		var progressbar0 = $( "#progressbar" ),progressLabel = $( "#progressbar .progress-label" );
		progressbar0.css("display","block");
		var mytimer;
//		var totalnum = cmdObj.total_tasks;
		progressbar0.progressbar({
			value: false,
			change: function() {
				progressLabel.text(progressbar0.progressbar("value") + "%" );
			},
			complete: function() {
				progressLabel.text( "Complete!" );
				$("#stopprocess").attr("disabled",true);  
				cmdObj.runningcmd = false;
				clearTimeout(mytimer); 
			}
		});
		var progressbarValue = progressbar0.find( ".ui-progressbar-value" );
		progressbarValue.css({"background": '#0e90d2'});
		progressLabel.css({"color":"#000"});
		return(function sendXHR(){
			if(cmdObj.runningcmd) {
				$.ajax({
					url: "/cmd_result/",
					data: {"TrackMark": cmdObj.track_mark,"TotalTasks":cmdObj.total_tasks},
					type:"GET",
					async:false,
					timeout:3000,
					success: function( data ) {
						var jsondata = JSON.parse(data);
						var val = progressbar0.progressbar( "value" ) || 0;
						var failnum=0,successnum = 0;
						var htmlstr = "";
						for (var key in jsondata)
						{
							if(key == "result_count")
							{
								successnum = (jsondata[key])[0];
								failnum = (jsondata[key])[1];						
							}else{ 
								if(jsondata[key][3] == "Success"){
									var len = jsondata[key][2].length;
									var kk = jsondata[key][2].substr(2,len -8);
									var arr = kk.replace(/\\n/g,"<br />");
									htmlstr += "<div style='color:green'>" + jsondata[key][0] + ","+jsondata[key][1] +"<br /></div>";
									htmlstr += arr +","+jsondata[key][3]+","+jsondata[key][4];		
									htmlstr +="<br />"
								}else{
									htmlstr +="<div style='color:red'>" + jsondata[key].join() + "</div>";
								//	htmlstr +="<br />";
								}
							}
						}

						$("#execution_process pre").html(htmlstr);
						//.parent().click(cmdObj.showProcessRet);
						$("#failednum").html(failnum);//.parent().click(cmdObj.showFailedLists);
						$("#successnum").html(successnum);				//todoif(failnum)
						mytimer = setTimeout( sendXHR,1000); 
						if(cmdObj.total_tasks != 0) 
							progressbar0.progressbar("value",parseInt((failnum + successnum)/cmdObj.total_tasks * 100));
					},
					error:function(XMLHttpRequest,textStatus,errorThrown){
						cmdObj.runningcmd = false;
						clearTimeout(mytimer);
					}                       
				});
			}
			else
			{
				clearTimeout(mytimer);
			}
		}); 
	};
	cmdObj.showSuccessLists = function(){
		$.get("/getSuccessLists/",{TrackMark:cmdObj.track_mark},function(data){
			var lists = JSON.parse(data);
			var len = lists.length;
			var ulele = $("<ul style='list-style-type:none'></ul>");
			for(var i=0;i<len;i++)
			{
				var li_checkbox=$("<li><input type='checkbox' name='failedip' value ='"+lists[i]+"'/> "+lists[i]+" </li>");
				ulele.append(li_checkbox);
			}
			$("#execution_success p").html("").append(ulele);//.parent().css("display","block");	
		});

	};

	 cmdObj.showFailedLists = function(){
               $.get("/getFailedLists/",{TrackMark:cmdObj.track_mark},function(data){
                        var lists = JSON.parse(data);
                        var len = lists.length;
                        var ulele = $("<ul style='list-style-type:none'></ul>");
                        for(var i=0;i<len;i++)
                        {
                                var li_checkbox=$("<li><input type='checkbox' name='failedip' value ='"+lists[i]+"'/> "+lists[i]+" </li>");
                                ulele.append(li_checkbox);
                        }
                        var allchecked =$("<input type='button' id='selectall' class='btn btn-primary' style='margin:0 10px 0 0' value='select all'/>");
			var allunchecked = $("<input type='button' id='unselectall'  class='btn btn-primary' style='margin:0 10px 0 0' value='unselect all'/>");
                        var reAct = $("<input type='button' id='reActCmd' class='btn btn-primary' style='margin:0 10px 0 0' value='Re-Execute'/>");

                        $("#execution_failed p").html("").append(ulele).append(allchecked).append(allunchecked).append(reAct);
                        $("#selectall").click(cmdObj.selectAll);
						$("#unselectall").click(cmdObj.unselectAll);
                        $("#reActCmd").click(function(){
                                var machine = [];
                                $("input:checked").each(function(i,n){
                                        machine.push($(this).val());
                                });
                                cmdObj.popDia(command,username,machine,remote_path,fileLists);
                        });
                });

        };
	cmdObj.showProcessRet = function(){

	};
	cmdObj.selectAll = function(){
		$("#execution_failed input[type='checkbox']").each(function(ele){
		/*	never use	$(this).attr("checked",true);
			use $(this).prop("checked")
		*/
			$(this).prop("checked", true);
		});
	};
	cmdObj.unselectAll = function(){
		$("#execution_failed input[type='checkbox']").each(function(ele){
			$(this).prop("checked", false);
		});

	};
	
	//value lists should be an array containing keys
	cmdObj.makeOptions = function(valueLists){
		var optionHtml="";
		$.each(valueLists,function(i,n){
			var opt = "<option value='"
				+ valueLists[i] 
				+ "'>"
				+ valueLists[i]
				+"</option>";
			
			optionHtml += opt;			
		});
		return optionHtml;
	};
	cmdObj.fileLists = [];
	//return an array containing all the option value
	cmdObj.getOptions = function(selectId){
		var selectEle = $("#"+selectId);
		var optionValues=[];
		$("#"+selectId+" option").each(function(i,n){
			optionValues.push($(this).attr("value"));
		});
		return optionValues;
	};
//	 $("#totalnum").parent().click(cmdObj.showProcessRet);
    $("#failednum").parent().click(cmdObj.showFailedLists);
	$("#successnum").parent().click(cmdObj.showSuccessLists);
	$.get("/getDangerousCmd/",function(data){
		cmdObj.dangerousCmd = JSON.parse(data);
	});	
	/*$(window).unload(function(){
		console.log("hello");
		if(!cmdObj.runningcmd){
			var diagbody =  $("#dialog_body");
			diagbody.html("Are  you sure you are leaving this page during running command?");
			$( "#dialog-confirm" ).dialog({
					resizable: false,
					height:240,
					modal: true,
					buttons: {
						"Yes": function() {
							$( this ).dialog( "close" );
							//cmdObj.executeCommand(command,username,computers,remotepath,filelists);
						},
						Cancel: function() {
							$( this ).dialog( "close" );
						}
					}
				});
		
		}	
		
	});*/
	$(window).bind('beforeunload',function(){
	console.log("beforeunload event is triggered");
	console.log("cmdobj.runningcmd:"+ cmdObj.runningcmd);
		if(cmdObj.runningcmd)
			return 'You are running command now';
	});  
	$(window).bind('unload',function(){
	console.log("unload event is triggered");
		console.log("cmdobj.runningcmd:"+ cmdObj.runningcmd);
		if(cmdObj.runningcmd)
			cmdObj.stopExecution();
	});
})(CommandExecutePage);

