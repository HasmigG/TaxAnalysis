
const init = async (state) => {

  let data_1 = await (await fetch('/api/v1.0/charitable_data')).json();
  let data_2 = await (await fetch('/api/v1.0/rate_of_charitable_returns')).json();

  if (state == undefined) {

    let states = [... new Set(Object.values(data_1.State))];

    state = states[0];

    // populating states
    document.getElementById('states').innerHTML = '';
    states.forEach(state => {
      document.getElementById('states').innerHTML += `<option>${state}</option>`
    });
  };

  // State selection
  let filter_index = Object.entries(data_2.State).filter(arr => arr[1] == state).map(arr => arr[0]);

  // Filtering Charitable Amount based on state.
  let charitable_amt = Object.entries(data_1.Charitable_Amt)
    .filter(arr => filter_index.includes(arr[0]))
    .map(arr => arr[1]);

  // Filtering Total Returns Claiming Charitable Contributions based on state.
  let rates = Object.entries(data_2.Rate_of_Returns_claiming_Charitable_Contribution)
    .filter(arr => filter_index.includes(arr[0]))
    .map(arr => arr[1]);

  // Fitering All AGI Brakets
  let agi_stubs = [... new Set(Object.entries(data_2.new_agi_stub).map(arr => arr[1]))];

  // Container for AGI Brakets and coresponding rates data per year.
  let agi_ids = {};

  // Populating key and empty list in agi_ids container.
  agi_stubs
    .map(x => `AGI_Bracket_${x}`)
    .forEach(key => agi_ids[key] = []);

  // Populating values in agi_ids
  let agi_index = 1
  rates.forEach(rate => {
    agi_ids[`AGI_Bracket_${agi_index}`].push(rate);

    agi_index++;
    if (agi_index > 6) {
      agi_index = 1;
    }
  });

  // container for traces
  let data = []

  // X axis data
  let years = [... new Set(Object.values(data_2.year))];

  // Creating the traces
  Object.entries(agi_ids).forEach(([key,val]) => {
    data.push(
      {
        x: years,
        y: val,
        text:key,
        name: key,
        type: 'scatter'
              }
    )
  });

  Plotly.newPlot('chart_01', data, {title: "<b>% of Total Returns Claiming Charitable Contributions</b>", width: 800 });

  // Container for AGI Brakets and coresponding rates data per year.
  let amt_ids = {};

  // Populating key and empty list in agi_ids container.
  agi_stubs
    .map(x => `AGI_AMT_ID${x}`)
    .forEach(key => amt_ids[key] = []);
  
  // Populating values in agi_ids
  agi_index = 1
  charitable_amt.forEach(amt => {
    amt_ids[`AGI_AMT_ID${agi_index}`].push(amt);

    agi_index++;
    if (agi_index > 6) {
      agi_index = 1;
    }
  });

  console.log('agi: ',amt_ids);

  // Creating the traces
  Object.entries(amt_ids).forEach(([key,val]) => {
    data.push(
      {
        x: years,
        y: val,
        text:key,
        name: key,
        type: 'scatter'
              }
    )
  });

  Plotly.newPlot('chart_02', data, {title: "<b>Charitable Amount</b>", width: 800 });
};

init();