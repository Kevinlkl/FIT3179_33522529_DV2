var vg_1 = "HW9_map.vg.json";

vegaEmbed("#cloropleth_map", vg_1).then(function(result) {
    // Access the Vega view instance 
    // (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);