
const dataUrl = '/dashboard/fetch-house-value-change-data/';

fetch(dataUrl, {
    method: 'GET',
    headers: {
    },
}).then(response => {
    response.json().then(data => {
      
      const ctx = document.getElementById('house_value_and_change');      
      
      const mixedChart = new Chart(ctx, {
        data: {
          datasets: [
            {
              type: 'bar',
              label: 'values',
              data: data.house_value_and_change.map(row => row.values),
              borderWidth: 1
            },
            {
              type: 'line',
              label: 'twelve_month_change',
              data: data.house_value_and_change.map(row => row.twelve_month_change),
              borderWidth: 1
            },
            {
              type: 'line',
              label: 'three_month_change',
              data: data.house_value_and_change.map(row => row.three_month_change),
              borderWidth: 1
            }
          ],
          labels: data.house_value_and_change.map(row => row.areas),
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

