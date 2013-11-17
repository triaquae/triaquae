// Stacked-to-Grouped Bars
// Credits to: http://bl.ocks.org/3943967

/*
 Switch between stacked and grouped layouts using sequenced transitions!  Animations
 reserve object constancy and allow the user to follow the data across views. Animation
 design by Heer and Robertson. Colors and data generation inspired by Byron and Wattenberg
 */

(function($) {

	function asyncEvent() {
		var dfd = new jQuery.Deferred();

		var n = 3, // number of layers
		m = 38, // number of samples per layer
		stack = d3.layout.stack(), layers = stack(d3.range(n).map(function() {
			return bumpLayer(m, .1);
		})), yGroupMax = d3.max(layers, function(layer) {
			return d3.max(layer, function(d) {
				return d.y;
			});
		}), yStackMax = d3.max(layers, function(layer) {
			return d3.max(layer, function(d) {
				return d.y0 + d.y;
			});
		});

		var margin = {
			top : 0,
			right : 0,
			bottom : 20,
			left : 0
		}, width = 700 - margin.left - margin.right, height = 300 - margin.top - margin.bottom;

		var x = d3.scale.ordinal().domain(d3.range(m)).rangeRoundBands([0, width], .08);

		var y = d3.scale.linear().domain([0, yStackMax]).range([height, 0]);

		var color = d3.scale.linear().domain([0, n - 1]).range(["#87BA17", "#4b99cb"]);

		var xAxis = d3.svg.axis().scale(x).tickSize(0).tickPadding(6).orient("bottom");

		var svg = d3.select("#d3-chart-1").append("svg").attr("width", width + margin.left + margin.right).attr("height", height + margin.top + margin.bottom)
		//added 2 new lines below
		// credit to: http://stackoverflow.com/questions/11942500/how-to-make-force-layout-graph-in-d3-js-responsive-to-screen-browser-size
		.attr("viewBox", "0 0 700 300").attr("preserveAspectRatio", "xMidYMid").append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

		var layer = svg.selectAll(".layer").data(layers).enter().append("g").attr("class", "layer").style("fill", function(d, i) {
			return color(i);
		});

		var rect = layer.selectAll("rect").data(function(d) {
			return d;
		}).enter().append("rect").attr("x", function(d) {
			return x(d.x);
		}).attr("y", height).attr("width", x.rangeBand()).attr("height", 0);

		rect.transition().delay(function(d, i) {
			return i * 10;
		}).attr("y", function(d) {
			return y(d.y0 + d.y);
		}).attr("height", function(d) {
			return y(d.y0) - y(d.y0 + d.y);
		});

		svg.append("g").attr("class", "x axis").attr("transform", "translate(0," + height + ")").call(xAxis);

		$('#grouped').click(function() {
			transitionGrouped();
		})
		$('#stacked').click(function() {
			transitionStacked();
		})
		function transitionGrouped() {
			y.domain([0, yGroupMax]);

			rect.transition().duration(500).delay(function(d, i) {
				return i * 10;
			}).attr("x", function(d, i, j) {
				return x(d.x) + x.rangeBand() / n * j;
			}).attr("width", x.rangeBand() / n).transition().attr("y", function(d) {
				return y(d.y);
			}).attr("height", function(d) {
				return height - y(d.y);
			});
		}

		function transitionStacked() {
			y.domain([0, yStackMax]);

			rect.transition().duration(500).delay(function(d, i) {
				return i * 10;
			}).attr("y", function(d) {
				return y(d.y0 + d.y);
			}).attr("height", function(d) {
				return y(d.y0) - y(d.y0 + d.y);
			}).transition().attr("x", function(d) {
				return x(d.x);
			}).attr("width", x.rangeBand());
		}

		// Return the Promise so caller can't change the Deferred
		return dfd.promise();
	}

	asyncEvent()

})(jQuery);

// Inspired by Lee Byron's test data generator.
function bumpLayer(n, o) {

	function bump(a) {
		var x = 1 / (.1 + Math.random()), y = 2 * Math.random() - .5, z = 10 / (.1 + Math.random());
		for (var i = 0; i < n; i++) {
			var w = (i / n - y) * z;
			a[i] += x * Math.exp(-w * w);
		}
	}

	var a = [], i;
	for ( i = 0; i < n; ++i)
		a[i] = o + o * Math.random();
	for ( i = 0; i < 5; ++i)
		bump(a);
	return a.map(function(d, i) {
		return {
			x : i,
			y : Math.max(0, d)
		};
	});
}

// Credit to: http://stackoverflow.com/questions/9400615/whats-the-best-way-to-make-a-d3-js-visualisation-layout-responsive

$(function() {
	var aspect = 700 / 300, chart = $("#d3-chart-1").find("svg");
	var targetWidth = ($("#d3-chart-1").width() - 10);
	chart.attr("width", targetWidth);
	chart.attr("height", targetWidth / aspect);
	$("#d3-chart-1 svg").width(targetWidth);
	$("#d3-chart-1 svg").height(targetWidth / aspect);

	$(window).on("resize", function() {
		var targetWidth = ($("#d3-chart-1").width() - 10);
		chart.attr("width", targetWidth);
		chart.attr("height", targetWidth / aspect);
		$("svg").width(targetWidth);
		$("svg").height(targetWidth / aspect);
	});
});
