

const dataUrl = '/dashboard/fetch-house-value-growth-data/';

fetch(dataUrl, {
    method: 'GET',
    headers: {
    },
}).then(response => {
    response.json().then(data => {
      const ctx = document.getElementById('house_value_growth');
      
      new Chart(ctx, {
          type: 'line',
          data: {
              labels: data.house_value_growth.map(row => row.year),
              datasets: [
                {
                    label: 'house_value_growth',
                    data: data.house_value_growth.map(row => row.nz_house_value_growth),
                    borderWidth: 1
                },
                {
                    // type: 'bar',
                    label: 'AKL_house_value_growth',
                    data: data.house_value_growth.map(row => row.akl_house_value_growth),
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

