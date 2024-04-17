
const init = async (year, state) => {

  let data_1 = await (await fetch('/api/v1.0/charitable_data')).json();
  let data_2 = await (await fetch('/api/v1.0/rate_of_charitable_returns')).json();


  if (state == undefined) {

    let states = [... new Set(data_1.map(states => states[2]))];

    state = states[0];

    // populating states
    document.getElementById('states').innerHTML = '';
    states.forEach(state => {
      document.getElementById('states').innerHTML += `<option>${state}</option>`
    });
  };


  let filter_index = Object.entries(data_2.State).filter(arr => arr[1] == state).map(arr => arr[0]);
  
  let amounts = Object.entries(data_2.Rate_of_Returns_claiming_Charitable_Contribution)
    .filter(arr => filter_index.includes(arr[0]))
    .map(arr => arr[1]);

  let agi_stubs = Object.entries(data_2.new_agi_stub)
    .filter(arr => filter_index.includes(arr[0]))
    .map(arr => arr[1]);

  let x_values = [... new Set(Object.values(data_2.year))];

  let data = []

  let trace = {}

  for (let i = 0; i < agi_stubs.length; i++) {
      trace[agi_stubs[i]] = 0
  }

  console.log(trace);

  let trace1 = {
    x: x_values,
    y: amounts,
    type: 'scatter'
  };

  let trace2 = {
    x: x_values,
    y: amounts,
    type: 'scatter'
  };


  Plotly.newPlot('charts', data, { width: '60%' });

};

init();