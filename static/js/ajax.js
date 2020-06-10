// variable that keeps all the filter information

var send_data = {}

$(document).ready(function () {
    // reset all parameters on page load

    resetFilters();
    // bring all the data without any filters

    getAPIData();
    // get all countries from database via 

    // AJAX call into country select options

    getCategories();
    // get all varities from database via 

    // AJAX call into variert select options




    // on selecting the country option

    $('#categories').on('change', function () {
        // since province and region is dependent 

        // on country select, emty all the options from select input



        //get province of selected country

        getProvince(this.value);
        // get api data of updated filters

        getAPIData();
    });

    // on filtering the variety input


    // on filtering the province input



    // on filtering the region input

})




/**.
    Utility function to showcase the api data 
    we got from backend to the table content
**/
function putTableData(result) {
    // creating table row for each result and

    // pushing to the html cntent of table body of listing table

    let row;
    if (result["results"].length > 0) {
        $("#no_results").hide();
        $("#list_data").show();
        $("#listing").html("");
        $.each(result["results"], function (a, b) {
            row = "<tr> <td>" + b.country + "</td>" +
                "<td>" + b.taster_name + "</td>" +
                "<td title=\"" + b.title + "\">" + b.title.slice(0, 50) + "..." + "</td>" +
                "<td title=\"" + b.description + "\">" + b.description.slice(0, 60) + "..." + "</td>" +
                "<td>" + b.designation + "</td>" +
                "<td>" + b.points + "</td>" +
                "<td>" + b.price + "</td>" +
                "<td>" + b.province + "</td>" +
                "<td>" + b.region + "</td>" +
                "<td>" + b.winery + "</td>" +
                "<td>" + b.variety + "</td></tr>"
            $("#listing").append(row);
        });
    }
    else {
        // if no result found for the given filter, then display no result

        $("#no_results h5").html("No results found");
        $("#list_data").hide();
        $("#no_results").show();
    }

}

function getAPIData() {
    let url = $('#list_data').attr("url")
    $.ajax({
        method: 'GET',
        url: url,
        data: send_data,
        beforeSend: function () {
            $("#no_results h5").html("Loading data...");
        },
        success: function (result) {
            putTableData(result);
        },
        error: function (response) {
            $("#no_results h5").html("Something went wrong");
            $("#list_data").hide();
        }
    });
}

function getCountries() {
    // fill the options of countries by making ajax call

    // obtain the url from the countries select input attribute

    let url = $("#countries").attr("url");

    // makes request to getCountries(request) method in views

    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {

            countries_option = "<option value='all' selected>All Countries</option>";
            $.each(result["countries"], function (a, b) {
                countries_option += "<option>" + b + "</option>"
            });
            $("#countries").html(countries_option)
        },
        error: function (response) {
            console.log(response)
        }
    });
}
