




function mainFunction() {
    let active = $(this)
    let img
    if(active.attr("id") === "button-dev"){
        img = $("#resume")
        $("#resume2").addClass("hide-this")
        img.removeClass("hide-this")
    }
    else {
        img = $("#resume2")
        $("#resume").addClass("hide-this")
        img.removeClass("hide-this")
     }
}

$(document).ready(function(){
    $('[name="resume-button-name"]').on('click', mainFunction)
})




