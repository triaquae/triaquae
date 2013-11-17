$(function(){
	if($(".expanded a").attr("href") != "\/file_transfer"){
		$(".expanded").removeClass("expanded");
		$(".current").removeClass("current");
		var _parent = $("a[href='\/file_transfer']").parent();
		_parent.addClass("expanded");
		_parent.parents("li").addClass("current");
	}
	CommandExecutePage.fileLists = [];//CommandExecutePage.getOptions("fileLists");
	$.get("/getFileLists/",function(data){
		var jsonData = JSON.parse(data);
		for(var key in jsonData){
			var value = jsonData[key];
			if($.isArray(value))
				value = value.join(" | ");
			var  _list = key +" | "+value;
			var arr = [];
			arr.push(_list);
			CommandExecutePage.fileLists.push(_list);
		}
		$("#fileTransferDiv #fileLists").html(CommandExecutePage.makeOptions(CommandExecutePage.fileLists));
		$("#fileTransferDiv #filterFiles").autocomplete({
			source: function( request, response ) {
				  var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( request.term ), "i" );
				  response( $.grep(fileLists, function( item ){
					  return matcher.test( item );
				  }) );
			  }
		
		});
	});
	$.get('/AllUsers/',function(data){
                var usrCount =JSON.parse(data);
		 $("#invokeUser").append(CommandExecutePage.makeOptions(usrCount));
        });

	$("#fileTransferDiv #filterFiles").keyup(function(){
		var _text = $(this).val();
		//var allopt = CommandExecutePage.getOptions("fileLists");
		var  patt = new RegExp("^"+_text);
		var filelist = CommandExecutePage.fileLists;
		$.each(filelist,function(i,n){
			if( patt.exec(filelist[i]) == null){
				var ele = $("#fileLists option[value='"+filelist[i]+"']");
				if(ele.length >0)
					ele.detach();
			}else{
				var ele = $("#fileLists option[value='"+filelist[i]+"']");
				var ele1 = $("#selectedFiles option[value='"+filelist[i]+"']");
				if(ele.length ==0 && ele1.length==0){
					//$("#fileLists").add("<option value='"+CommandExecutePage.fileLists[i]+">"+CommandExecutePage.fileLists[i]+"</option>");//
					var obj = document.getElementById("fileLists"); 
					obj.add(new Option(filelist[i],filelist[i])); 
				}
			}
			
		});
		
	});
    $("#fileTransferDiv #chooseall").click(function(){
		var opt = CommandExecutePage.getOptions("fileLists");
		var  options =[];
		$.each(opt,function(i,n){
			var _opt = (opt[i].split(" "))[0];
			options.push(_opt);	
		});

		$("#selectedFiles").append(CommandExecutePage.makeOptions(options));
		$("#fileLists").html("");
		return false;
    });
    $("#fileTransferDiv #removeall").click(function(){
		var opt = CommandExecutePage.getOptions("selectedFiles");
		var options =[];
		$.each(opt,function(i,n){
			var files = CommandExecutePage.fileLists;
			for(var key in files){
				if(files[key].indexOf(opt[i]) != -1)
					options.push(files[key]);
			}
				
		});
		$("#fileLists").append(CommandExecutePage.makeOptions(options));
		$("#selectedFiles").html("");
		return false;
    });
    $("#movetoright").click(function(){
		var ori_value = $("#fileLists option:selected");
//		var new_value =[], arr_index = [];
		var obj0 = document.getElementById("selectedFiles"),obj1 = document.getElementById("fileLists");
		if(ori_value.length ==0 )
			return false;
		$.each(ori_value,function(i,n){
			var _value = $(this).val();
			var index = $(this).index();
			_value = _value.split(" ");
//			new_value.push(_value[0]);
			obj0.add(new Option(_value[0],_value[0]));
//			arr_index.push(index);
			obj1.options.remove(index);
		});
	return false;
    });
    $("#movetoleft").click(function(){	
		var ori_value = $("#selectedFiles option:selected");
		var obj0 = document.getElementById("selectedFiles"),obj1 = document.getElementById("fileLists");
		if(ori_value.length > 0){
		//	var obj = document.getElementById("fileLists");
			var files = CommandExecutePage.fileLists;
			$.each(ori_value,function(i,n){
				var _value = $(this).val();
				var index = $(this).index();
				
				for (var key in files)
					if(files[key].indexOf(_value) != -1)
						_value = files[key]; 
				obj1.add(new Option(_value,_value)); 
				obj0.options.remove(index); 
			});
		}
		return false;
    });
   $("#transferFileBtn").click(function(){
	var usr = $("#invokeUser").val();
	var  action = $("#invokeAction").val();
	var  fileLists = CommandExecutePage.getOptions("selectedFiles");
	var remotePath = $("#remotepath").val();
	var computers = getDatas();
        CommandExecutePage.popDia(action,usr,computers,remotePath,fileLists);
	return false;

   });
 $("#stopprocess").click(function(){CommandExecutePage.stopExecution();return false;});

});



