var theForm = document.forms["IQForm"];

// Set Starting Values
var categoryPrice = 0;
var speakersPrice = 0;
var audioQualityPrice = 0;
var TATPrice = 0;
var stylePrice = 0;
var timeStampPrice = 0;

var category = new Array();
category["none"] = 0;
category["general"] = 1.15;
category["legal"] = 1.25;
category["medical"] = 1.25;
category["personal"] = 1.15;
category["academic"] = 0.99;

var speakers = new Array();
speakers["1"] = 0;
speakers["2"] = 0;
speakers["3"] = 0.05;
speakers["4"] = 0.1;
speakers["10"] = 0.15;

var audioQuality = new Array();
audioQuality["bad"] = 0.1;
audioQuality["fair"] = 0.05;
audioQuality["good"] = 0;

var TAT = new Array();
TAT["24hr"] = 0.35;
TAT["48hr"] = 0.15;
TAT["standard"] = 0;

var transcriptStyle = new Array();
transcriptStyle["verbatim"] = 0.15;
transcriptStyle["intelligent-verbatim"] = 0;

var timeStamps = new Array();
timeStamps["y-stamps"] = 0.15;
timeStamps["n-stamps"] = 0;

function getCategoryPrice() {
    var default_price = 0;
    //this function finds the category price based on the dropdown selection
    //get a reference to the form id="IQForm"
    var theForm = document.forms["IQForm"];
    //get a reference to the select id="category"
    var selectedCategory = theForm.elements["category"];
    //set categoryPrice to value user chose
    categoryPrice = category[selectedCategory.value] || default_price;
    //return categoryPrice
    return categoryPrice;
}

function getSpeakersPrice() {
    var default_price = 0;
    var theForm = document.forms["IQForm"];
    var selectedSpeakers = theForm.elements["speakers"];
    speakersPrice = speakers[selectedSpeakers.value] || default_price;
    return speakersPrice;
}

function getAudioQualityPrice() {
    var default_price = 0;
    var theForm = document.forms["IQForm"];
    var selectedAudioQuality = theForm.elements["audio-quality"];
    audioQualityPrice = audioQuality[selectedAudioQuality.value] || default_price;
    return audioQualityPrice;
}

function getTATPrice() {
    var default_price = 0;
    var theForm = document.forms["IQForm"];
    var selectedTAT = theForm.elements["tat"];
    TATPrice = TAT[selectedTAT.value] || default_price;
    return TATPrice;
}

function getStylePrice() {
    var default_price = 0;
    var theForm = document.forms["IQForm"];
    var selectedStyle = theForm.elements["style"];
    stylePrice = transcriptStyle[selectedStyle.value] || default_price;
    return stylePrice;
}

function getTimeStampPrice() {
    var theForm = document.forms["IQForm"];
    //get reference to time stamp radios with name="stamps"
    var selectedTimeStamp = theForm.elements["stamps"];
    //loop through each radio button
    for (var i = 0; i < selectedTimeStamp.length; i++) {
        //if radio button is checked
        if (selectedTimeStamp[i].checked) {
            //get selected items value
            timeStampPrice = timeStamps[selectedTimeStamp[i].value];
            //break loop if match is found
            break;
        }
    }
    return timeStampPrice;
}

function getMinutes() {
    var theForm = document.forms["IQForm"];
    var minutes = theForm.elements["audio-minutes"];
    var howmany = 1;
    //if textbox is not blank
    if (minutes.value != "") {
        howmany = parseInt(minutes.value) || howmany;
    }
    return howmany;
}

function isMinutesValid() {
    var valid = true;
    var theForm = document.forms["IQForm"];
    var minutes = theForm.elements["audio-minutes"];

    if (minutes.value == "" || minutes.value == 1) {
        valid = false;
    }
    return valid;
}

function calculateTotal() {
    console.log("Category:" + getCategoryPrice());
    console.log("Speakers:" + getSpeakersPrice());
    console.log("AudioQual:" + getAudioQualityPrice());
    console.log("TAT:" + getTATPrice());
    console.log("Style:" + getStylePrice());
    console.log("TimeSt:" + getTimeStampPrice());
    console.log("Minutes:" + getMinutes() + " and type:" + typeof getMinutes());

    var multiplier = parseFloat(getCategoryPrice()) + parseFloat(getSpeakersPrice()) + parseFloat(getAudioQualityPrice()) + parseFloat(getTATPrice()) + parseFloat(getStylePrice()) + parseFloat(getTimeStampPrice());
    console.log("Multiplier: " + multiplier.toFixed(2));

    var total = parseFloat(getMinutes()) * parseFloat(multiplier);
    console.log("Total:" + total.toFixed(2));

    console.log("**********************************************");

    //display cost per minute (eg. multiplier)
    document.getElementById('minuteCost').innerHTML =
        String(multiplier.toFixed(2));

    if (isMinutesValid()) {
        //display total cost (eg. total)
        document.getElementById('total-cost').style.display='block';
        document.getElementById('totalCost').innerHTML =
            String(total.toFixed(2));
    }
    else {
        document.getElementById('total-cost').style.display='none';
    }


}