$(document).ready(function () {
    let $loadingIndicatorElement = $(".loading-indicator");
    let $resultTableElement = $(".result-table");
    let $noResultElement = $(".no-result");

    $("button").click(function () {
        $loadingIndicatorElement.removeClass("d-none");
        $resultTableElement.addClass("d-none");
        $noResultElement.addClass("d-none");
        let inputString = $("input").val();
        let url = "tracks/" + inputString;
        $.get(url, function (data, status) {
            console.log(data, status);
            $loadingIndicatorElement.addClass("d-none");
            if (data.length > 0) {
                $resultTableElement.removeClass("d-none");
                let htmlResult = "";
                for (let item of data) {
                   htmlResult += "<tr><td>"+ item.artistName + "</td><td>" + item.trackName + "</td><td><img src=\"" + item.coverUrl + "\" alt=\""+ item.trackName +"\"></td><td><a href=\""+ item.previewUrl + "\" >Listen Preview</a></td></tr>";
                }
                $("tbody").html(htmlResult);
            } else {
                $noResultElement.removeClass("d-none");
            }
        });
    });
});