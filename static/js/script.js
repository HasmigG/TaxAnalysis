
const init = async () => {
    console.log('Test Test 1 2 3');
    let data = await (await fetch('/api/v1.0/charitable_data')).json();
    let years = [... new Set(data.map(states => states[1]))];
    let states = [... new Set(data.map(states => states[2]))];



    console.log(
        data[0]
    );

    // populating years
    document.getElementById('years').innerHTML = '';
    years.forEach(year => {
        document.getElementById('years').innerHTML += `<option>${year}</option>`
    });

    // populating states
    document.getElementById('states').innerHTML = '';
    states.forEach(state => {
        document.getElementById('states').innerHTML += `<option>${state}</option>`
    });



    var xValue = ['Product A', 'Product B', 'Product C'];

var yValue = [20, 14, 23];

var trace1 = {
  x: xValue,
  y: yValue,
  type: 'bar',
  text: yValue.map(String),
  textposition: 'auto',
  hoverinfo: 'none',
  marker: {
    color: 'rgb(158,202,225)',
    opacity: 0.6,
    line: {
      color: 'rgb(8,48,107)',
      width: 1.5
    }
  }
};

let data1 = [trace1];

let layout = {
  title: 'January 2013 Sales Report',
  barmode: 'stack'
};

Plotly.newPlot('charts', data1, layout);
};

init();