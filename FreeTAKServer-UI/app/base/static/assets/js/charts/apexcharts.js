var options = {
	series: [0, 0, 0],
	chart: {
		height: 390,
		type: "radialBar",
	},
	plotOptions: {
		radialBar: {
			offsetY: 0,
			startAngle: 0,
			endAngle: 270,
			hollow: {
				margin: 5,
				size: "30%",
				background: "transparent",
				image: undefined,
			},
			dataLabels: {
				name: {
					show: false,
				},
				value: {
					show: false,
				},
			},
			track: {
				background: "#272929",
			},
		},
	},
	colors: ["#278AED", "#2c75ff", "#004C9A"],
	labels: ["CPU", "RAM", "DISK"],
	legend: {
		show: true,
		floating: true,
		fontSize: "16px",
		position: "left",
		offsetX: 50,
		offsetY: 15,
		labels: {
			useSeriesColors: true,
		},
		markers: {
			size: 0,
		},
		formatter: function (seriesName, opts) {
			return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex];
		},
		itemMargin: {
			vertical: 3,
		},
	},
	responsive: [
		{
			breakpoint: 480,
			options: {
				legend: {
					show: true,
					floating: true,
					fontSize: "16px",
					position: "left",
					offsetX: 10,
					offsetY: 10,
					labels: {
						useSeriesColors: true,
					},
					markers: {
						size: 0,
					},
					formatter: function (seriesName, opts) {
						return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex];
					},
					itemMargin: {
						vertical: 3,
					},
				},
			},
		},
	],
};

// var chart = new ApexCharts(document.querySelector("#chart"), options);
// chart.render();
