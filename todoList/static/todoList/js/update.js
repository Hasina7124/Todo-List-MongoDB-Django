$(document).ready(function () {
    const btnModify = $("#update");
    var index = $("input:checkbox").length;
    var chkd =[];
    const id = $("#id");
    $(":checkbox").on("change",function(){
        var check;
        const btnUpdate = $("#update");
        for(let i = 0; i<index; i++){
            check = $('.task'+i);
            if(check.is(":checked")){
                chkd.push(check.val());
            }
        }
        $("#id").attr("value", chkd[0]);
        $("#inputAchever").attr("value", chkd[0]);
    });
});