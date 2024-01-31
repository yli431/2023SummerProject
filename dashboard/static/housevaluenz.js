
const dataUrl = '/dashboard/fetch-house-value-nz-data/';

fetch(dataUrl, {
    method: 'GET',
    headers: {
    },
}).then(response => {
    response.json().then(data => {
      const ctx = document.getElementById('house_value_nz');
      
      new Chart(ctx, {
          type: 'pie',
          data: {
              labels: data.house_value_nz.map(row => row.name),
              datasets: [
                {
                    label: 'year_2003',
                    data: data.house_value_nz.map(row => row.year_2003),
                    borderWidth: 1
                },
                {
                    // type: 'bar',
                    label: 'year_2004',
                    data: data.house_value_nz.map(row => row.year_2004),
                    borderWidth: 1
                },
                {
                    label: 'year_2005',
                    data: data.house_value_nz.map(row => row.year_2005),
                    borderWidth: 1
                },
                {
                    label: 'year_2006',
                    data: data.house_value_nz.map(row => row.year_2006),
                    borderWidth: 1
                },
                {
                    label: 'year_2007',
                    data: data.house_value_nz.map(row => row.year_2007),
                    borderWidth: 1
                },
                {
                    label: 'year_2008',
                    data: data.house_value_nz.map(row => row.year_2008),
                    borderWidth: 1
                },
                {
                    label: 'year_2009',
                    data: data.house_value_nz.map(row => row.year_2009),
                    borderWidth: 1
                },
                {
                    label: 'year_2010',
                    data: data.house_value_nz.map(row => row.year_2010),
                    borderWidth: 1
                },
                {
                    label: 'year_2011',
                    data: data.house_value_nz.map(row => row.year_2011),
                    borderWidth: 1
                },
                {
                    label: 'year_2012',
                    data: data.house_value_nz.map(row => row.year_2012),
                    borderWidth: 1
                },
                {
                    label: 'year_2013',
                    data: data.house_value_nz.map(row => row.year_2013),
                    borderWidth: 1
                },
                {
                    label: 'year_2014',
                    data: data.house_value_nz.map(row => row.year_2014),
                    borderWidth: 1
                },
                {
                    label: 'year_2015',
                    data: data.house_value_nz.map(row => row.year_2015),
                    borderWidth: 1
                },
                {
                    label: 'year_2016',
                    data: data.house_value_nz.map(row => row.year_2016),
                    borderWidth: 1
                },
                {
                    label: 'year_2017',
                    data: data.house_value_nz.map(row => row.year_2017),
                    borderWidth: 1
                },
                {
                    label: 'year_2018',
                    data: data.house_value_nz.map(row => row.year_2018),
                    borderWidth: 1
                },
                {
                    label: 'year_2019',
                    data: data.house_value_nz.map(row => row.year_2019),
                    borderWidth: 1
                },
                {
                    label: 'year_2020',
                    data: data.house_value_nz.map(row => row.year_2020),
                    borderWidth: 1
                },
                {
                    label: 'year_2021',
                    data: data.house_value_nz.map(row => row.year_2021),
                    borderWidth: 1
                },
                {
                    label: 'year_2022',
                    data: data.house_value_nz.map(row => row.year_2022),
                    borderWidth: 1
                },
                {
                    label: 'year_2023',
                    data: data.house_value_nz.map(row => row.year_2023),
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

