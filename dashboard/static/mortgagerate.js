// import Chart from './chart.js/auto'

const dataUrl = '/dashboard/fetch-mortgage-rate-data/';

fetch(dataUrl, {
    method: 'GET',
    headers: {
    },
}).then(response => {
    response.json().then(data => {
      
      const ctx = document.getElementById('mortgage_rate');      
      
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: data.mortgage_rates.map(row => row.date),
          datasets: [
            {
              label: '3-year-rates',
              data: data.mortgage_rates.map(row => row.three_year_rate),
              borderWidth: 1,
              pointRadius: false
            },
            {
              label: '4-year-rates',
              data: data.mortgage_rates.map(row => row.four_year_rate),
              borderWidth: 1,
              pointRadius: false
            },
            {
              label: '5-year-rates',
              data: data.mortgage_rates.map(row => row.five_year_rate),
              borderWidth: 1,
              pointRadius: false
            }
          ]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    })
  });

