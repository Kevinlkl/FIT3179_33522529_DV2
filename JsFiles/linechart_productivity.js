// Use a path relative to index.html (no leading slash)
var vg_1 = "Idioms/linechart_productivity.vg.json";

vegaEmbed("#multiline_chart_productivity", vg_1).then(function(result) {
    // Access the Vega view instance 
    // (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);