$(document).ready(function(){
    const create = $("#create");
    const cancel = $("#cancelCreate");

    const createModal = $("#ajouterModal");

    create.on("click",function(){
        createModal.removeClass("hidden");
    });

    cancel.on("click", function(){
        createModal.addClass("hidden");
    });
});