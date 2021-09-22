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
            console.log(status);

            if (data.length > 0) {
                $resultTableElement.removeClass("d-none");

                let htmlResult = "";
                for (let item of data) {
                    htmlResult += "<tr>" +
                        "<td>" + item.artist + "</td>" +
                        "<td>" + item.track + "</td>" +
                        "<td><img src=\"" + item.album_image_url + "\" alt=\"" + item.track + "\"></td>" +
                        "<td><a href=\"" + item.preview_url + "\" >Listen Preview</a></td>" +
                        "</tr>";
                }

                $("tbody").html(htmlResult);
            } else {
                $noResultElement.removeClass("d-none");
            }
        }).always(function () {
            $loadingIndicatorElement.addClass("d-none");
        }).fail(function (xhr, status, message) {
            let responseMessage = xhr.responseJSON.message;
            $noResultElement.removeClass("d-none");
            $noResultElement.find("span").text(responseMessage);
            console.log(responseMessage);
        });
    });
});