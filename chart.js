//doughnut
  var ctxD = document.getElementById("doughnutChart").getContext('2d');
  var myLineChart = new Chart(ctxD, {
    type: 'doughnut',
    data: {
      datasets: [{
        data: [12, 200],
        backgroundColor: ["#4D5360", "#D3D3D3"],
        hoverBackgroundColor: ["#616774"]
      }]
    },
    options: {
      responsive: true
    }
  });
