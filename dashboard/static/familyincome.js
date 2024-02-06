
const dataUrl = '/dashboard/fetch-family-income-data/';

fetch(dataUrl, {
    method: 'GET',
    headers: {
    },
}).then(response => {
    response.json().then(data => {
      
      const ctx = document.getElementById('family_income');
      let family_income_akl = []
      let family_income_excl_akl = []
      for (let i=0; i<data.family_income.length; i++) {

          if (data.family_income[i]["region"] === "Auckland") {
            family_income_akl.push(data.family_income[i]["family_income"])
          } else {
            family_income_excl_akl.push(data.family_income[i]["family_income"])
          }
      }

      let halfLength = Math.ceil(data.family_income.length / 2);
      let firstHalfOfYears = data.family_income.slice(0, halfLength);

      new Chart(ctx, {
          type: 'bar',
          data: {
              labels: firstHalfOfYears.map(row => row.year),
              datasets: [
                {
                //   type: 'line',
                    label: 'family_income_excl_AKL',
                    data: family_income_excl_akl,
                    borderWidth: 1
                },
                {
                    label: 'family_income_AKL',
                    data: family_income_akl,
                    borderWidth: 1
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

