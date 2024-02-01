// import Chart from './chart.js/auto'

const dataUrl = '/dashboard/fetch-rental-growth-data/';

fetch(dataUrl, {
    method: 'GET',
    headers: {
    },
}).then(response => {
    response.json().then(data => {
      const ctx = document.getElementById('rental_growth');
      
      new Chart(ctx, {
          type: 'line',
          data: {
              labels: data.rental_growth.map(row => row.year),
              datasets: [
                {
                    label: 'average_rental_growth',
                    data: data.rental_growth.map(row => row.nz_avg_rental_growth),
                    borderWidth: 1
                },
                {
                    // type: 'bar',
                    label: 'AKL_rental_growth',
                    data: data.rental_growth.map(row => row.akl_avg_rental_growth),
                    borderWidth: 1
                },
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

