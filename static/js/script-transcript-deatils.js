var theForm = document.forms["TDForm"];

var category = new Array();
category["none"] = 0;
category["General"] = 1.15;
category["Legal"] = 1.25;
category["Medical"] = 1.25;
category["Personal"] = 1.15;
category["Academic"] = 0.99;

var style = new Array();
style["none"] = 0;
style["IntelligentVerbatim"] = 0;
style["Verbatim"] = 0.15;

var speakers = new Array();
speakers["none"] = 0;
speakers["1"] = 0;
speakers["2"] = 0;
speakers["3"] = 0.05;
speakers["4"] = 0.1;
speakers["10"] = 0.15;


var timestamps = new Array();
timestamps["none"] = 0;
timestamps["None"] = 0;
timestamps["SpeakerChange"] = 0.15;
timestamps["2Minutes"] = 0.15;


var tat = new Array();
tat["none"] = 0;
tat["24"] = 0.35;
tat["48"] = 0.15;
tat["Standard"] = 0;


var audioQuality = new Array();
audioQuality["none"] = 0;
audioQuality["Bad"] = 0.1;
audioQuality["Fair"] = 0.05;
audioQuality["Good"] = 0;

function getCategoryPrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedCategory = theForm.elements["category"];
    categoryPrice = category[selectedCategory.value] || default_price;
    return categoryPrice;
}

function getStylePrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedStyle = theForm.elements["style"];
    stylePrice = style[selectedStyle.value] || default_price;
    return stylePrice
}

function getSpeakerPrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedSpeakers = theForm.elements["speakers"];
    speakersPrice = speakers[selectedSpeakers.value] || default_price;
    return speakersPrice
}

function getTimeStampPrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedTimeStamp = theForm.elements["timestamps"];
    timeStampPrice = timestamps[selectedTimeStamp.value] || default_price;
    return timeStampPrice
}

function getTatPrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedTAT = theForm.elements["tat"];
    tatPrice = tat[selectedTAT.value] || default_price;
    return tatPrice
}

function getAudioQualPrice() {
    var default_price = 0;
    var theForm = document.forms["TDForm"];
    var selectedAudioQual = theForm.elements["audio-quality"];
    audioQualPrice = audioQuality[selectedAudioQual.value] || default_price;
    return audioQualPrice
}

function getMinutes() {

    var timeContent = document.getElementById('total-time');
    var test = timeContent.textContent;
    console.log("text Content:" + test);
    var totalTime = parseInt(timeContent.textContent);
    return totalTime
}

function calculateTotal() {
    console.log("Category:" + getCategoryPrice());
    console.log("Speakers:" + getSpeakerPrice());
    console.log("AudioQual:" + getAudioQualPrice());
    console.log("TAT:" + getTatPrice());
    console.log("Style:" + getStylePrice());
    console.log("TimeSt:" + getTimeStampPrice());
    console.log("Minutes:" + getMinutes() + " and type:" + typeof getMinutes());

    var multiplier = parseFloat(getCategoryPrice()) + parseFloat(getSpeakerPrice()) + parseFloat(getAudioQualPrice()) + parseFloat(getTatPrice()) + parseFloat(getStylePrice()) + parseFloat(getTimeStampPrice());
    console.log("Multiplier: " + multiplier.toFixed(2));

    var total = parseFloat(getMinutes()) * parseFloat(multiplier);
    console.log("Total:" + total.toFixed(2));

    console.log("**********************************************");

    document.getElementById('minuteCost').innerHTML =
        String(multiplier.toFixed(2));

    document.getElementById('total-cost').style.display='block';
        document.getElementById('totalCost').innerHTML =
            String(total.toFixed(2))
}



