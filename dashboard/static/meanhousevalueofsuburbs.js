const dataUrl = '/dashboard/fetch-mean-house-value-of-chch-suburbs/';

fetch(dataUrl, {
    method: 'GET',
    headers: {
    },
}).then(response => {
    response.json().then(data => {

        // const numberOfColors = 90;
        let suburbNames = Object.keys(data.house_value_of_chchsuburbs_dict);
        const ctx = document.getElementById('house_value_of_chchsuburbs');
        const generatedColors = generateRGBColors(suburbNames.length);

        // let single_suburb = data.house_value_of_chchsuburbs_dict["Addington"]
        // console.log(single_suburb);

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
                // borderColor: generatedColors[i],
                tension: 0.1,
                pointRadius: 1.5
                // pointHoverRadius: 0
            });
        }

        // console.log(single_suburb_prices);

        const startYear = 2000;
        const startMonth = 1; // January
        const endYear = 2024;
        const endMonth = 1; // January

        const yearMonthPairs = generateYearMonthPairs(startYear, startMonth, endYear, endMonth);
        console.log(yearMonthPairs);

        new Chart(ctx, {
            type: 'line',
            data: {
                labels: yearMonthPairs,
                datasets: myDataSet
                // datasets: [{
                //     label: 'Addington',
                //     data: single_suburb_prices,
                //     fill: false,
                //     borderColor: 'rgb(75, 192, 192)',
                //     tension: 0.1
                // }]
            },
            
            // options: {
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
        });
        

    //   for (var key of keys) {
    //     let suburb_house_price = data.house_value_of_chchsuburbs_dict[key]
    //     // console.log(suburb_house_price)
    //     const formattedDates = suburb_house_price.map(entry => `${entry.month}/${entry.year}`)
    //     // console.log("1111111111111")
    //     console.log(formattedDates)
    //     new Chart(ctx, {
    //         type: 'line',
    //         data: {
    //             labels: formattedDates,
    //             datasets: [
    //                 {
    //                     label: 'price',
    //                     data: data.house_value_of_chchsuburbs_dict[key].map(row => row.price),
    //                     borderWidth: 1
    //                 },
    //             ]},
    //             options: {
    //                 scales: {
    //                     y: {
    //                         beginAtZero: true
    //                     }
    //             }}
    //         });
    //     }
      })
  });


function generateYearMonthPairs(startYear, startMonth, endYear, endMonth) {
    let yearMonthPairs = [];
    let currentDate = new Date(startYear, startMonth - 1); // Month is zero-based

    while (currentDate <= new Date(endYear, endMonth - 1)) {
        const year = currentDate.getFullYear();
        const month = currentDate.toLocaleString('default', { month: 'long' });
        yearMonthPairs.push(year.toString() + "." + month);
        currentDate.setMonth(currentDate.getMonth() + 1);
    }

    return yearMonthPairs;
}

function generateRGBColors(numColors) {
    const colors = [];

    for (let i = 0; i < numColors; i++) {
    //   const red = Math.floor((i * 255) / (numColors - 1));
    //   const green = Math.floor((i * 255) / (numColors - 1));
    //   const blue = Math.floor((i * 255) / (numColors - 1));
        const red = 255 - i + 10;
        const green = 255 - i +5;
        const blue = i + 30;

        const color = `rgb(${red}, ${green}, ${blue})`;
        colors.push(color);
    }

    return colors;
  }