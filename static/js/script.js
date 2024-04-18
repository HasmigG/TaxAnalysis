
const init = async (state) => {

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

  console.log(data_1[0]);

  let filter_index = Object.entries(data_2.State).filter(arr => arr[1] == state).map(arr => arr[0]);

  let rates = Object.entries(data_2.Rate_of_Returns_claiming_Charitable_Contribution)
    .filter(arr => filter_index.includes(arr[0]))
    .map(arr => arr[1]);

  let agi_stubs = [... new Set(Object.entries(data_2.new_agi_stub).map(arr => arr[1]))];

  agi_ids = {};

  agi_stubs
    .map(x => `AGI_BRAKET_${x}`)
    .forEach(key => agi_ids[key] = []);

  var agi_index = 1
  rates.forEach(rate => {
    agi_ids[`AGI_BRAKET_${agi_index}`].push(rate);

    agi_index++;
    if (agi_index > 6) {
      agi_index = 1;
    }
  });

  let data = []

  let years = [... new Set(Object.values(data_2.year))];


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


  Plotly.newPlot('charts', data, {title: "<b>% of Total Returns Claiming Charitable Contributions</b>", width: '60%' });
};

init();