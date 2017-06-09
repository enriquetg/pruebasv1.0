$(document).foundation()

var handleSearchInput = function(event) {
     if (event.keyCode == 13 || event.type=="click"){
         return handleSubmitSearch();
     }
     return false;
 };

 var handleSubmitSearch = function() {
     var qs = $('#id_rpp, #id_search').serialize();
     $(location).attr('href', '?' + qs);
     return false;
 };