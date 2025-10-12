// Use a path relative to index.html (no leading slash)
var vg_1 = "Idioms/dotmap_msia_seaport.vg.json";
var vg_2 = "Idioms/dotmap_msia_airport.vg.json";

vegaEmbed("#dotmap_msia_seaport", vg_1).then(function(result) {
    // Access the Vega view instance 
    // (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

vegaEmbed("#dotmap_msia_airport", vg_2).then(function(result) {
    // Access the Vega view instance 
    // (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);