

const dataUrl = '/dashboard/fetch-house-value-growth-data/';

fetch(dataUrl, {
    method: 'GET',
    headers: {
    },
}).then(response => {
    response.json().then(data => {
      const ctx = document.getElementById('house_value_growth');
      // const config = {
      //   type: 'line',
      //   data: data,
      //   options: {
      //     animations: {
      //       radius: {
      //         duration: 400,
      //         easing: 'linear',
      //         loop: (context) => context.active
      //       }
      //     },
      //     hoverRadius: 12,
      //     hoverBackgroundColor: 'yellow',
      //     interaction: {
      //       mode: 'nearest',
      //       intersect: false,
      //       axis: 'x'
      //     },
      //     plugins: {
      //       tooltip: {
      //         enabled: false
      //       }
      //     }
      //   },
      // };
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
          animations: {
            radius: {
              duration: 400,
              easing: 'linear',
              loop: (context) => context.active
            }
          },
          hoverRadius: 12,
          hoverBackgroundColor: 'yellow',
          interaction: {
            mode: 'nearest',
            intersect: false,
            axis: 'x'
          },
          plugins: {
            tooltip: {
              enabled: false
            }
          }
        },
      });
    })
  });

