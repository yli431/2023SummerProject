const dataUrl = '/dashboard/fetch-mean-house-value-of-chch-suburbs/';

fetch(dataUrl, {
    method: 'GET',
    headers: {
    },
}).then(response => {
    response.json().then(data => {
        let suburbNames = Object.keys(data.house_value_of_chchsuburbs_dict);
        const ctx = document.getElementById('house_value_of_chchsuburbs');
        const displayAllButton = document.getElementById('display_all_lines');
        const hideAllButton = document.getElementById('hide_all_lines');
        const displayDefaultButton = document.getElementById('display_default_lines');

        let myDataSet = [];

        for(let i=0; i < suburbNames.length; i++){
            let singleSuburb = data.house_value_of_chchsuburbs_dict[suburbNames[i]];
            let singleSuburbPrices = [];

            for (let j = 0; j < singleSuburb.length; j++) {
                singleSuburbPrices.push(singleSuburb[j].price);
            }

            myDataSet.push({
                label: suburbNames[i],
                data: singleSuburbPrices,
                fill: false,
                tension: 0.1,
                pointRadius: 1.5,
                hidden: true
            });
        }

        const startYear = 2000;
        const startMonth = 1; // January
        const endYear = 2024;
        const endMonth = 1; // January
        const yearMonthPairs = generateYearMonthPairs(startYear, startMonth, endYear, endMonth);

        const chartAreaBorder = {
            id: 'chartAreaBorder',
            beforeDraw(chart, args, options) {
              const {ctx, chartArea: {left, top, width, height}} = chart;
              ctx.save();
              ctx.strokeStyle = options.borderColor;
              ctx.lineWidth = options.borderWidth;
              ctx.setLineDash(options.borderDash || []);
              ctx.lineDashOffset = options.borderDashOffset;
              ctx.strokeRect(left, top, width, height);
              ctx.restore();
            }
          };

        let line_chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: yearMonthPairs,
                datasets: myDataSet
            },
            options: {
                plugins: {
                  chartAreaBorder: {
                    borderColor: 'grey',
                    borderWidth: 2,
                    borderDash: [5, 5],
                    borderDashOffset: 2,
                  }
                }
            },
            plugins: [chartAreaBorder]
        });

        let init_display_suburbs = [
            'Papanui', 
            'Christchurch Central', 
            'Ilam', 
            'Cashmere', 
            'New Brighton',
            'Kennedys Bush',
            'Phillipstown'
        ]

        line_chart.data.datasets.forEach(function(e) {
            if (init_display_suburbs.includes(e.label)) {
                e.hidden = false;
            }
        });

        line_chart.update();

        displayAllButton.addEventListener('click', function (e) {
            e.preventDefault()
        
            line_chart.data.datasets.forEach(function(e) {
                e.hidden = false;
            });
    
            line_chart.update();
        })

        hideAllButton.addEventListener('click', function (e) {
            e.preventDefault()
        
            line_chart.data.datasets.forEach(function(e) {
                e.hidden = true;
            });
    
            line_chart.update();
        })

        displayDefaultButton.addEventListener('click', function (e) {
            e.preventDefault()
        
            line_chart.data.datasets.forEach(function(e) {
                if (init_display_suburbs.includes(e.label)) {
                    e.hidden = false;
                }
                else {
                    e.hidden = true;
                }
            });
    
            line_chart.update();
        })
      })
  });


function generateYearMonthPairs(startYear, startMonth, endYear, endMonth) {
    let yearMonthPairs = [];

    // for (let year = 2000; year <= 2023; year++) {
    //     for (let month = 1; month <= 12; month++) {
    //         yearMonthPairs.push(month.toString() + "/" + year.toString());
    //     }
    // }
    let currentDate = new Date(startYear, startMonth - 1); // Month is zero-based

    while (currentDate <= new Date(endYear, endMonth - 1)) {
        const year = currentDate.getFullYear();
        // const month = currentDate.toLocaleString('default', { month: 'long' });
        const month = currentDate.getMonth();
        // yearMonthPairs.push(year.toString() + "." + month);
        yearMonthPairs.push((month + 1).toString() + "/" + year.toString());
        currentDate.setMonth(currentDate.getMonth() + 1);
    }

    return yearMonthPairs;
}
