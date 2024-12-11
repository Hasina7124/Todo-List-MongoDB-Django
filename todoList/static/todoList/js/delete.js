$(document).ready(function(){
    const dlt = $("#delete");
    var index = $("input:checkbox").length;
    
    var inputDelete = $("#inputDelete");
    var check;

    const btnUpdate = $("#update");
    const btnAchever = $("#achever");
    $(":checkbox").on("change" ,function(){
        var chkd = [];
        for(let i = 0; i<index; i++){
            check = $('.task'+i);
            if(check.is(":checked")){
                chkd.push(check.val());
            }
        }
        const checks = chkd.join(",");
        if(chkd.length == 1){
            btnUpdate.removeAttr("disabled");
            btnAchever.removeAttr("disabled");
        }
        else{
            btnUpdate.attr("disabled",true);
            btnAchever.attr("disabled",true);
        }
        inputDelete.attr("value", checks);
    });
    
});