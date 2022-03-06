$(function () {
    // https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html
    //var json_data = document.getElementById('survey-count-data').textContent;
    // the information in this tag is no longer being used, so remove the content from the page
    //document.getElementById('survey_count').remove()

    //console.log(json_data)
    //console.log(survey_count)

  // SURVEY CHARTS
  // line chart
  var $chartSurveyCount = $("#chartSurveyCount");
  var $surveyTotal = $("#surveyTotal");
  $.ajax({
    url: $chartSurveyCount.data("url"),
    success: function (data) {

    if (data.data.length == undefined || data.data.length == 0) {
        var surveySum = 0;

        $surveyTotal.text(surveySum);

        var fsctx1 = $chartSurveyCount[0].getContext("2d");
        fsctx1.fillStyle = "white";
        fsctx1.font = "bold 18px Arial";
        fsctx1.fillText("There are 0 surveys.", (canvas.width / 2) - 17, (canvas.height / 2) + 8);
    } else {

        var surveySum = data.data.reduce((partialSum, a) => partialSum + a, 0);

        //console.log(surveySum);
        $surveyTotal.text(surveySum);

        var fsctx1 = $chartSurveyCount[0].getContext("2d");

          new Chart(fsctx1, {
            type: "line",
            data: {
              labels: data.labels,
              datasets: [{
                  label: "Survey Count",
                  tension: 0.4,
                  borderWidth: 0,
                  pointRadius: 2,
                  pointBackgroundColor: "#e3316e",
                  borderColor: "#e3316e",
                  borderWidth: 3,
                  backgroundColor: 'transparent',
                  data: data.data,
                  maxBarThickness: 6
                }],
            },
            options: {
              responsive: true,
              maintainAspectRatio: false,
              plugins: {
                legend: {
                  display: false,
                }
              },
              interaction: {
                intersect: false,
                mode: 'index',
              },
              scales: {
                y: {
                  grid: {
                    drawBorder: false,
                    display: true,
                    drawOnChartArea: true,
                    drawTicks: false,
                    borderDash: [5, 5]
                  },
                  ticks: {
                    display: true,
                    padding: 10,
                    color: '#b2b9bf',
                    font: {
                      size: 11,
                      family: "Open Sans",
                      style: 'normal',
                      lineHeight: 2
                    },
                  }
                },
                x: {
                  grid: {
                    drawBorder: false,
                    display: true,
                    drawOnChartArea: true,
                    drawTicks: true,
                    borderDash: [5, 5]
                  },
                  ticks: {
                    display: true,
                    color: '#b2b9bf',
                    padding: 10,
                    font: {
                      size: 11,
                      family: "Open Sans",
                      style: 'normal',
                      lineHeight: 2
                    },
                  }
                },
              },
            },
          });
        }

    }
  });

  // bar chart
  var $chartSurveySiteCount = $("#chartSurveySiteCount");
  $.ajax({
    url: $chartSurveySiteCount.data("url"),
    success: function (data) {

    var fsctx2 = $chartSurveySiteCount[0].getContext("2d");

    new Chart(fsctx2, {
	type: "bar",
	data: {
	  labels: data.labels,
	  datasets: [{
		label: "Surveys by Site",
		weight: 5,
		borderWidth: 0,
		borderRadius: 4,
		backgroundColor: '#3A416F',
		data: data.data,
		fill: false,
		maxBarThickness: 35
	  }],
	},
	options: {
	  responsive: true,
	  maintainAspectRatio: false,
	  plugins: {
		legend: {
		  display: false,
		}
	  },
	  scales: {
		y: {
		  grid: {
			drawBorder: false,
			display: true,
			drawOnChartArea: true,
			drawTicks: false,
			borderDash: [5, 5]
		  },
		  ticks: {
			display: true,
			padding: 10,
			color: '#9ca2b7'
		  }
		},
		x: {
		  grid: {
			drawBorder: false,
			display: false,
			drawOnChartArea: true,
			drawTicks: true,
		  },
		  ticks: {
			display: true,
			color: '#9ca2b7',
			padding: 10
		  }
		},
	  },
	},
  });

    }
  });

  // Pie chart
  var $chartSurveySystemCount = $("#chartSurveySystemCount");
  $.ajax({
    url: $chartSurveySystemCount.data("url"),
    success: function (data) {

    var colors = palette(['tol', 'qualitative'], data.labels.length)
    colors = colors.map(i => '#' + i);

    var fsctx3 = $chartSurveySystemCount[0].getContext("2d");

    new Chart(fsctx3, {
      type: "pie",
      data: {
        labels: data.labels,
        datasets: [{
          label: "Survey Count",
          weight: 9,
          cutout: 0,
          tension: 0.9,
          pointRadius: 2,
          borderWidth: 2,
          backgroundColor: colors,
          data: data.data,
          fill: false
        }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'left',
          }
        },
        interaction: {
          intersect: false,
          mode: 'index',
        },
        scales: {
          y: {
            grid: {
              drawBorder: false,
              display: false,
              drawOnChartArea: false,
              drawTicks: false,
            },
            ticks: {
              display: false
            }
          },
          x: {
            grid: {
              drawBorder: false,
              display: false,
              drawOnChartArea: false,
              drawTicks: false,
            },
            ticks: {
              display: false,
            }
          },
        },
      },
    });

    }
  });

  // Field Sample CHARTS
  // line chart
  var $chartFieldSampleCount = $("#chartFieldSampleCount");
  var $fieldSampleTotal = $("#fieldSampleTotal");
  var $filterTotal = $("#filterTotal");
  var $subCoreTotal = $("#subCoreTotal");
  $.ajax({
    url: $chartFieldSampleCount.data("url"),
    success: function (data) {

    if (data.fieldsample_data.length == undefined || data.fieldsample_data.length == 0) {
        var fieldSampleSum = 0;
        var filterSum = 0;
        var subCoreSum = 0;

        $fieldSampleTotal.text(fieldSampleSum);
        $filterTotal.text(filterSum);
        $subCoreTotal.text(subCoreSum);

        var fsctx4 = $chartFieldSampleCount[0].getContext("2d");
        fsctx4.fillStyle = "white";
        fsctx4.font = "bold 18px Arial";
        fsctx4.fillText("There are 0 field samples.", (canvas.width / 2) - 17, (canvas.height / 2) + 8);
    } else {

        var fieldSampleSum = data.fieldsample_data.reduce((partialSum, a) => partialSum + a, 0);
        var filterSum = data.filter_data.reduce((partialSum, a) => partialSum + a, 0);
        var subCoreSum = data.subcore_data.reduce((partialSum, a) => partialSum + a, 0);

        //console.log(surveySum);
        $fieldSampleTotal.text(fieldSampleSum);
        $filterTotal.text(filterSum);
        $subCoreTotal.text(subCoreSum);

        var fsctx4 = $chartFieldSampleCount[0].getContext("2d");

          new Chart(fsctx4, {
            type: "line",
            data: {
              labels: data.count_labels,
              datasets: [{
                  label: "Filter Count",
                  tension: 0.4,
                  borderWidth: 0,
                  pointRadius: 2,
                  pointBackgroundColor: "#e3316e",
                  borderColor: "#e3316e",
                  borderWidth: 3,
                  backgroundColor: 'transparent',
                  data: data.filter_data,
                  maxBarThickness: 6
                },
                {
                  label: "SubCore Count",
                  tension: 0.4,
                  borderWidth: 0,
                  pointRadius: 2,
                  pointBackgroundColor: "#3A416F",
                  borderColor: "#3A416F",
                  borderWidth: 3,
                  backgroundColor: 'transparent',
                  data: data.subcore_data,
                  maxBarThickness: 6
                },

              ],
            },
            options: {
              responsive: true,
              maintainAspectRatio: false,
              plugins: {
                legend: {
                  display: false,
                }
              },
              interaction: {
                intersect: false,
                mode: 'index',
              },
              scales: {
                y: {
                  grid: {
                    drawBorder: false,
                    display: true,
                    drawOnChartArea: true,
                    drawTicks: false,
                    borderDash: [5, 5]
                  },
                  ticks: {
                    display: true,
                    padding: 10,
                    color: '#b2b9bf',
                    font: {
                      size: 11,
                      family: "Open Sans",
                      style: 'normal',
                      lineHeight: 2
                    },
                  }
                },
                x: {
                  grid: {
                    drawBorder: false,
                    display: true,
                    drawOnChartArea: true,
                    drawTicks: true,
                    borderDash: [5, 5]
                  },
                  ticks: {
                    display: true,
                    color: '#b2b9bf',
                    padding: 10,
                    font: {
                      size: 11,
                      family: "Open Sans",
                      style: 'normal',
                      lineHeight: 2
                    },
                  }
                },
              },
            },
          });

        }

    }
  });

  // Pie chart
  var $chartFilterTypeCount = $("#chartFilterTypeCount");
  $.ajax({
    url: $chartFilterTypeCount.data("url"),
    success: function (data) {

    var colors = palette(['tol', 'qualitative'], data.labels.length)
    colors = colors.map(i => '#' + i);

    var fsctx5 = $chartFilterTypeCount[0].getContext("2d");

    new Chart(fsctx5, {
      type: "pie",
      data: {
        labels: data.labels,
        datasets: [{
          label: "Filter Count",
          weight: 9,
          cutout: 0,
          tension: 0.9,
          pointRadius: 2,
          borderWidth: 2,
          backgroundColor: colors,
          data: data.data,
          fill: false
        }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'left',
          }
        },
        interaction: {
          intersect: false,
          mode: 'index',
        },
        scales: {
          y: {
            grid: {
              drawBorder: false,
              display: false,
              drawOnChartArea: false,
              drawTicks: false,
            },
            ticks: {
              display: false
            }
          },
          x: {
            grid: {
              drawBorder: false,
              display: false,
              drawOnChartArea: false,
              drawTicks: false,
            },
            ticks: {
              display: false,
            }
          },
        },
      },
    });

    }
  });

  // bar chart
  var $chartFilterSiteCount = $("#chartFilterSiteCount");
  $.ajax({
    url: $chartFilterSiteCount.data("url"),
    success: function (data) {

    var fsctx6 = $chartFilterSiteCount[0].getContext("2d");

    new Chart(fsctx6, {
	type: "bar",
	data: {
	  labels: data.labels,
	  datasets: [{
		label: "Filters by Site",
		weight: 5,
		borderWidth: 0,
		borderRadius: 4,
		backgroundColor: '#3A416F',
		data: data.data,
		fill: false,
		maxBarThickness: 35
	  }],
	},
	options: {
	  responsive: true,
	  maintainAspectRatio: false,
	  plugins: {
		legend: {
		  display: false,
		}
	  },
	  scales: {
		y: {
		  grid: {
			drawBorder: false,
			display: true,
			drawOnChartArea: true,
			drawTicks: false,
			borderDash: [5, 5]
		  },
		  ticks: {
			display: true,
			padding: 10,
			color: '#9ca2b7'
		  }
		},
		x: {
		  grid: {
			drawBorder: false,
			display: false,
			drawOnChartArea: true,
			drawTicks: true,
		  },
		  ticks: {
			display: true,
			color: '#9ca2b7',
			padding: 10
		  }
		},
	  },
	},
  });

    }
  });

  // Pie chart
  var $chartFilterSystemCount = $("#chartFilterSystemCount");
  $.ajax({
    url: $chartFilterSystemCount.data("url"),
    success: function (data) {

    var colors = palette(['tol', 'qualitative'], data.labels.length)
    colors = colors.map(i => '#' + i);

    var fsctx7 = $chartFilterSystemCount[0].getContext("2d");

    new Chart(fsctx7, {
      type: "pie",
      data: {
        labels: data.labels,
        datasets: [{
          label: "Survey Count",
          weight: 9,
          cutout: 0,
          tension: 0.9,
          pointRadius: 2,
          borderWidth: 2,
          backgroundColor: colors,
          data: data.data,
          fill: false
        }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'left',
          }
        },
        interaction: {
          intersect: false,
          mode: 'index',
        },
        scales: {
          y: {
            grid: {
              drawBorder: false,
              display: false,
              drawOnChartArea: false,
              drawTicks: false,
            },
            ticks: {
              display: false
            }
          },
          x: {
            grid: {
              drawBorder: false,
              display: false,
              drawOnChartArea: false,
              drawTicks: false,
            },
            ticks: {
              display: false,
            }
          },
        },
      },
    });

    }
  });

});