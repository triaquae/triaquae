$(function(){
  var render = function(data){
    var host = data[0];
    // host_status,ping_status,last_check,attemp_count,
    var keys = ['host_status', 'ping_status','last_check','attempt_count','breakdown_count','up_count','availability'];
    $.each(host.fields, function(k, v){
      console.log(new Date());
      $('td[key="'+k+'"]').html(v);
    });
  };
  var refresh = function(){
    $("#s2 img,#s3 img").each(function(){
	var src= $(this).attr("src");
	var orsrc= src.split("?")[0];
       $(this).attr("src",orsrc+"?time="+new Date().getTime());

     });
  };
  setInterval(refresh, 120000);
});
