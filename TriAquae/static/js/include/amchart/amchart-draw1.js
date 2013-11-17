if ($('#chartdiv').length) {
  var chartData = [{
    date : new Date(2012, 0, 1),
         sales : 227,
         duration : 408
  }, {
    date : new Date(2012, 0, 2),
         sales : 371,
         duration : 482
  }, {
    date : new Date(2012, 0, 3),
         sales : 433,
         duration : 562
  }, {
    date : new Date(2012, 0, 4),
         sales : 345,
         duration : 379
  }, {
    date : new Date(2012, 0, 5),
         sales : 480,
         duration : 501
  }, {
    date : new Date(2012, 0, 6),
         sales : 386,
         duration : 443
  }, {
    date : new Date(2012, 0, 7),
         sales : 348,
         duration : 405
  }, {
    date : new Date(2012, 0, 8),
         sales : 238,
         duration : 309
  }, {
    date : new Date(2012, 0, 9),
         sales : 218,
         duration : 287
  }, {
    date : new Date(2012, 0, 10),
         sales : 349,
         duration : 485
  }, {
    date : new Date(2012, 0, 11),
         sales : 603,
         duration : 890
  }, {
    date : new Date(2012, 0, 12),
         sales : 534,
         duration : 810
  }];

  var chart;

  AmCharts.ready(function() {
    // SERIAL CHART
    chart = new AmCharts.AmSerialChart();
    chart.pathToImages = "img/amchart/";
    chart.dataProvider = chartData;
    chart.categoryField = "date";
    chart.marginTop = 0;
    chart.autoMarginOffset = 5;

    // AXES
    // category axis
    var categoryAxis = chart.categoryAxis;
    categoryAxis.parseDates = true;
    // as our data is date-based, we set parseDates to true
    categoryAxis.minPeriod = "DD";
    // our data is daily, so we set minPeriod to DD
    categoryAxis.autoGridCount = false;
    categoryAxis.gridCount = 50;
    categoryAxis.gridAlpha = 0;
    categoryAxis.gridColor = "#000000";
    categoryAxis.axisColor = "#000";
    // we want custom date formatting, so we change it in next line
    categoryAxis.dateFormats = [{
      period : 'DD',
             format : 'DD'
    }, {
      period : 'WW',
             format : 'MMM DD'
    }, {
      period : 'MM',
             format : 'MMM'
    }, {
      period : 'YYYY',
             format : 'YYYY'
    }];

    // as we have data of different units, we create two different value axes
    // Duration value axis
    var durationAxis = new AmCharts.ValueAxis();
    durationAxis.title = "duration";
    durationAxis.gridAlpha = 0.05;
    durationAxis.axisAlpha = 0;
    durationAxis.inside = true;
    // the following line makes this value axis to convert values to duration
    // it tells the axis what duration unit it should use. mm - minute, hh - hour...
    durationAxis.duration = "mm";
    durationAxis.durationUnits = {
      DD : "d. ",
      hh : "h ",
      mm : "min",
      ss : ""
    };
    chart.addValueAxis(durationAxis);

    // sales value axis
    var salesAxis = new AmCharts.ValueAxis();
    salesAxis.title = "sales";
    salesAxis.gridAlpha = 0;
    salesAxis.position = "right";
    salesAxis.inside = true;
    salesAxis.unit = " sales";
    salesAxis.axisAlpha = 0;
    chart.addValueAxis(salesAxis);

    // GRAPHS
    // duration graph
    var durationGraph = new AmCharts.AmGraph();
    durationGraph.title = "duration";
    durationGraph.valueField = "duration";
    durationGraph.type = "line";
    durationGraph.valueAxis = durationAxis;
    // indicate which axis should be used
    durationGraph.lineColor = "#CC0000";
    durationGraph.balloonText = "[[value]]";
    durationGraph.lineThickness = 1;
    durationGraph.legendValueText = "[[value]]";
    durationGraph.bullet = "square";
    chart.addGraph(durationGraph);

    // sales graph
    var salesGraph = new AmCharts.AmGraph();
    salesGraph.valueField = "sales";
    salesGraph.title = "sales";
    salesGraph.type = "column";
    salesGraph.fillAlphas = 0.3;
    salesGraph.fillColors = ["#00438D", "#006AAC"];
    salesGraph.valueAxis = salesAxis;
    // indicate which axis should be used
    salesGraph.balloonText = "[[value]] sales";
    salesGraph.legendValueText = "[[value]] sales";
    salesGraph.lineColor = "#739BC5";
    salesGraph.lineAlpha = .7;
    chart.addGraph(salesGraph);

    // CURSOR
    var chartCursor = new AmCharts.ChartCursor();
    chartCursor.zoomable = false;
    chartCursor.categoryBalloonDateFormat = "DD";
    chartCursor.cursorAlpha = 0;
    chart.addChartCursor(chartCursor);

    // LEGEND
    var legend = new AmCharts.AmLegend();
    legend.bulletType = "round";
    legend.equalWidths = false;
    legend.valueWidth = 120;
    legend.color = "#000000";
    chart.addLegend(legend);

    // BAR
    /* var chartScrollbar = new AmCharts.ChartScrollbar();
       chartScrollbar.scrollbarHeight = 25;
       chartScrollbar.graph = salesGraph; // as we want graph to be displayed in the scrollbar, we set graph here
       chartScrollbar.graphType = "line"; // we don't want candlesticks to be displayed in the scrollbar
       chartScrollbar.gridCount = 5;
       chartScrollbar.color = "#FFFFFF";
       chart.addChartScrollbar(chartScrollbar);*/

    // WRITE
    chart.write("chartdiv");
  });
}
