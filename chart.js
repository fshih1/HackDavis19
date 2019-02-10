//doughnut
  var ctxD = document.getElementById("doughnutChart").getContext('2d');
  var myLineChart = new Chart(ctxD, {
    type: 'doughnut',
    data: {
      labels: ["Malignant", "Benign"],
      datasets: [{
        data: [48, 52],
        backgroundColor: ["#4D5360", "#D3D3D3"],
        hoverBackgroundColor: ["#616774"]
      }]
    },
    options: {
      responsive: true
    }
  });
