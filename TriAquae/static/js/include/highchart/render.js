$(document).ready(function(){
  function ptime(time){
    return time / 3600000 + ":05"
  };
  var opts = {
    xAxis: {
      title:{'text':'hour of day'},
      type: 'datetime',
      dateTimeLabelFormats:{day: '%H : %M'},
      title:{'text':'every hour'}
    },
    yAxis:{title:{'text':'cpu usage'}, max:100,min:0},
    title:{text:'Cpu usage'},
    tooltip: {
      formatter: function() {
        var t = new Date(this.x-8*3600000).toTimeString().replace(/.*(\d{2}:\d{2}:\d{2}).*/, "$1")
        return 'cpu usage at <b>' + t +'</b> is </br><b>' + this.y +' </b>';
      }
    }
  };
// cpu usage highchart

function render(d){
  opts.serials = [{'data' : d}];
  $('#cpuchart').highcharts(opts);
}
function loadCpu(){
  // get cpu info from server and render on page
  $.getJSON('/cpuusage', function(data){
    console.log(data);
    var d = [];
    $.each(data, function(k, v){
      var t = k.split(':');
      d.push([parseInt(t[0])*3600*1000+parseInt(t[1])*60*1000, v]);
    });
    opts.series = [{'data':d,  'pointInterval': 3600 * 1000, 'name':'Cpu Usage' }];
    console.log(opts);
    $('#cpuchart').highcharts(opts);
  });
}
loadCpu();
setInterval(loadCpu, 1000*5);
});
