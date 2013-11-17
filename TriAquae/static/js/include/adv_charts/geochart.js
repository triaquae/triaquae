var map; 
google.load('visualization', '1', {'packages': ['geochart', 'corechart']});
google.setOnLoadCallback(drawRegionsMap); 

function drawRegionsMap() {
    var data = google.visualization.arrayToDataTable([
      ['Country', 'Users'],
      ['Germany', 200],
      ['Australia', 500],
      ['United States', 1300],
      ['Brazil', 400],
      ['Canada', 580],
      ['France', 600],
      ['RU', 1700]
    ]);

    var options = {};

    var chart = new google.visualization.GeoChart(document.getElementById('geomap'));
    chart.draw(data, options);
};

