$(function() {
    var getABCFromForm = function() {
        var abc = "%abc-2.1\n";
        abc += "X: 1\n";
        abc += "T: " + $('#titleField').val() + "\n";
        abc += "C: " + $('#composerField').val() + "\n";
        abc += "O: " + $('#originField').val() + "\n";
        abc += "M: " + $('#meterField').val() + "\n";
        abc += "L: " + $('#unitNoteLengthField').val() + "\n";
        abc += "K: " + $('#keyField').val() + "\n";
        abc += $('#staves').val() + "\n";
        return abc;    
    };

    var updateABCPreview = function() {
        do_svg(getABCFromForm(), 
               document.getElementById('previewContainer'));
    };
    
    $('#staves').keyup(updateABCPreview);
    $('input').keyup(updateABCPreview);
});