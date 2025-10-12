var vg_1 = "Idioms/heatmap_national_income.vg.json";

vegaEmbed("#heatmap_gdp_gni", vg_1).then(function(result) {
    // Access the Vega view instance 
    // (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);