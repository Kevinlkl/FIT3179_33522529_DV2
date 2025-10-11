// Use a path relative to index.html (no leading slash)
var vg_1 = "Idioms/piechart_import_export_sector.vg.json";

vegaEmbed("#piechart_import_export", vg_1).then(function(result) {
    // Access the Vega view instance 
    // (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);