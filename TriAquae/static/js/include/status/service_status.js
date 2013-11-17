$(function(){
  var render = function(data){
    $.each(data, function(group, hoststatus){
      var head = $("#widget-id-"+group + " h2");
      head.html(group);
      var table_group = $('table[group="'+group+'"]');
      $.each(hoststatus, function(ip, info){
        var tr_ip = $('tr[host="'+ip+'"]', table_group);
        $.each(info.fields, function(key, value){
          var td_dom = $('td[key="'+key+'"]', tr_ip);
          if(key == 'host_status'){
            var bar = $('div', td_dom);
            var span = $('span', td_dom);
            var last_status = span.html();
            bar.removeClass('host_status_'+last_status).addClass('host_status_'+value);
            span.html(value);
          } else
          td_dom.html(value);
        });
      });
    });
  };
  var refresh = function(){
    var api = window.location.href;
    $.getJSON(api, render);
    console.log(new Date());
  };
  var handle = setInterval(refresh, 30000);
});
