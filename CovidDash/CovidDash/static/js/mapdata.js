readFile = function () {
    var request = new XMLHttpRequest();
    request.open("GET", "https://data.ct.gov/api/views/bfnu-rgqt/rows.csv", false);
    request.send(null);

    var csvData = new Array();
    var jsonObject = request.responseText.split(/\r?\n|\r/);
    for (var i = 0; i < jsonObject.length; i++) {
        csvData.push(jsonObject[i].split(','));
    }
    var newcsvData = new Array();
    //console.log(newcsvData.push(csvData[0]));
    for (var i = csvData.length - 9; i < csvData.length; i++) {
        newcsvData.push(csvData[i]);
    }
    return newcsvData;
}

var data = new Array();
this.data = this.readFile();
this.data.forEach(function (entry) {
    if (entry[1] === "1")
        county1 = entry;
    if (entry[1] === "2")
        county2 = entry;
    if (entry[1] === "3")
        county3 = entry;
    if (entry[1] === "4")
        county4 = entry;
    if (entry[1] === "5")
        county5 = entry;
    if (entry[1] === "6")
        county6 = entry;
    if (entry[1] === "7")
        county7 = entry;
    if (entry[1] === "8")
        county8 = entry;

})

var simplemaps_statemap_mapdata = {
        main_settings: {
            //General settings
            width: "600", //'700' or 'responsive'
            background_color: "#FFFFFF",
            background_transparent: "yes",
            popups: "detect",
            state_description: "",
            state_color: "#88A4BC",
            state_hover_color: "#3B729F",
            state_url: "",
            border_size: 1.5,
            border_color: "#ffffff",
            all_states_inactive: "no",
            all_states_zoomable: "no",

            //Location defaults
            location_description: "Location description",
            location_color: "#FF0067",
            location_opacity: 0.8,
            location_hover_opacity: 1,
            location_url: "",
            location_size: 25,
            location_type: "square",
            location_border_color: "#FFFFFF",
            location_border: 2,
            location_hover_border: 2.5,
            all_locations_inactive: "no",
            all_locations_hidden: "no",

            //Label defaults
            label_color: "#ffffff",
            label_hover_color: "#ffffff",
            label_size: 20,
            label_font: "Arial",
            hide_labels: "no",
            hide_eastern_labels: false,
            manual_zoom: "yes",
            back_image: "no",
            arrow_box: "no",
            navigation_size: "40",
            navigation_color: "#f7f7f7",
            navigation_border_color: "#636363",
            initial_back: "no",
            initial_zoom: -1,
            initial_zoom_solo: "no",
            region_opacity: 1,
            region_hover_opacity: 0.6,
            zoom_out_incrementally: "yes",
            zoom_percentage: 0.99,
            zoom_time: 0.5,

            //Popup settings
            popup_color: "white",
            popup_opacity: 0.9,
            popup_shadow: 1,
            popup_corners: 5,
            popup_font: "12px/1.5 Verdana, Arial, Helvetica, sans-serif",
            popup_nocss: "no",

            //Advanced settings
            div: "map",
            auto_load: "yes",
            rotate: "0",
            url_new_tab: "yes",
            images_directory: "default",
            import_labels: "no",
            fade_time: 0.1,
            state_image_url: "",
            state_image_position: "",
            location_image_url: ""
        },
        state_specific: {
            "09001": {
                name: this.county1[2],
                description:
                    "Total Cases -  " + this.county1[3] +
                    "; Total Deaths - " + this.county1[5] +
                    "; Confirmed Cases - " + this.county1[8] +
                    "; Hospitalized- " + this.county1[7]
            },
            "09003": {
                name: this.county2[2],
                description:
                    "Total Cases -  " + this.county2[3] +
                    "; Total Deaths - " + this.county2[5] +
                    "; Confirmed Cases - " + this.county2[8] +
                    "; Hospitalized- " + this.county2[7]
            },
            "09005": {
                name: this.county3[2],
                description:
                    "Total Cases -  " + this.county3[3] +
                    "; Total Deaths - " + this.county3[5] +
                    "; Confirmed Cases - " + this.county3[8] +
                    "; Hospitalized- " + this.county3[7]
            },
            "09007": {
                name: this.county4[2],
                description:
                    "Total Cases -  " + this.county4[3] +
                    "; Total Deaths - " + this.county4[5] +
                    "; Confirmed Cases - " + this.county4[8] +
                    "; Hospitalized- " + this.county4[7]
            },
            "09009": {
                name: this.county5[2],
                description:
                    "Total Cases -  " + this.county5[3] +
                    "; Total Deaths - " + this.county5[5] +
                    "; Confirmed Cases - " + this.county5[8] +
                    "; Hospitalized- " + this.county5[7]
            },
            "09011": {
                name: this.county6[2],
                description:
                    "Total Cases -  " + this.county6[3] +
                    "; Total Deaths - " + this.county6[5] +
                    "; Confirmed Cases - " + this.county6[8] +
                    "; Hospitalized- " + this.county6[7]
            },
            "09013": {
                name: this.county7[2],
                description:
                    "Total Cases -  " + this.county7[3] +
                    "; Total Deaths - " + this.county7[5] +
                    "; Confirmed Cases - " + this.county7[8] +
                    "; Hospitalized- " + this.county7[7]
            },
            "09015": {
                name: this.county8[2],
                description:
                    "Total Cases -  " + this.county8[3] +
                    "; Total Deaths - " + this.county8[5] +
                    "; Confirmed Cases - " + this.county8[8] +
                    "; Hospitalized- " + this.county8[7]
            },
        },
        locations: {}
        ,
        labels: {}
        ,
        regions: {}
    }
;


