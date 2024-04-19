$(document).ready(function() {
    var map = L.map('map').setView([37.8, -96], 4);
  
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
  
    var heatmapLayer;
  
    function updateHeatmap(year) {
      $.getJSON('/heatmap_data?year=' + year, function(data) {
        if (heatmapLayer) {
          map.removeLayer(heatmapLayer);
        }
        var heatmapData = {};
        data.forEach(function(entry) {
          heatmapData[entry.State] = entry.Charitable_Amt;
        });
        heatmapLayer = L.geoJson(statesData, {
          style: function(feature) {
            return {
              fillColor: getColor(heatmapData[feature.properties.abbr]),
              weight: 2,
              opacity: 1,
              color: 'white',
              dashArray: '3',
              fillOpacity: 0.7
            };
          }
        }).addTo(map);
      });
    }
  
    function getColor(d) {
      return d > 1000000 ? '#800026' :
             d > 500000  ? '#BD0026' :
             d > 200000  ? '#E31A1C' :
             d > 100000  ? '#FC4E2A' :
             d > 50000   ? '#FD8D3C' :
             d > 20000   ? '#FEB24C' :
             d > 10000   ? '#FED976' :
                            '#FFEDA0';
    }
  
    $('#year-dropdown').change(function() {
      var selectedYear = $(this).val();
      updateHeatmap(selectedYear);
    });
  
    // Initialize heatmap with default year
    updateHeatmap($('#year-dropdown').val());
  });
  