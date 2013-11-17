$(function(){
	if($(".expanded a").attr("href") != "\/command_execution"){
        $(".expanded").removeClass("expanded");
		$(".current").removeClass("current");
		var _parent = $("a[href='\/command_execution']").parent();
		_parent.addClass("expanded");
		_parent.parents("li").addClass("current");
	}
	$.get('/AllCommands/',function(data){
		CommandExecutePage.tags = data.split('\n');
		$( "#appendedDropdownButton" ).autocomplete({
			source: function( request, response ) {
				  var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( request.term ), "i" );
				  response( $.grep(CommandExecutePage.tags, function( item ){
					  return matcher.test( item );
				  }) );
			  },
			minLength: 2,
			select: function( event, ui ) {
			//	log( ui.item ?
			//	"Selected: " + ui.item.label : "Nothing selected, input was " + this.value);
			},
			open: function() {
					$( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
			},
			close: function() {
					$( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
			}
		});
	});

	$.get('/AllUsers/',function(data){
		var usrCount =JSON.parse(data);
                var num = usrCount.length;
			
		for(var i=0;i<num;i++)
		{
			var listEle = $("<li></li>");
			listEle.data("UserName",usrCount[i]);
			listEle.html("Run as "+usrCount[i]);
			$("#invokeOperation").append(listEle);
		}
		if(num == 0)
			$("#invokeOperation").append("<span style='color:red'>No Valid User</span>");
                
	});

	$("#stopprocess").click(function(){CommandExecutePage.stopExecution();return false;});

	$("#invokeOperation").delegate("li","click",function(){
		var usr = $(this).data("UserName");
		var computers = getDatas();
		CommandExecutePage.popDia($('#appendedDropdownButton').val(),usr,computers);
	});
	 $("#appendedDropdownButton").keyup(function(){
		var _val = $(this).val();
		if(_val.replace(/\s/ig,"") != "" && CommandExecutePage.dangerousCmd.indexOf(_val) != -1)
			$(".alert").css("display","block");
		else
			$(".alert").css("display","none");
			
	});
});



