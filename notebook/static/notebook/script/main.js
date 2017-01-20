function ShowTable() {
    ShowWindow();
}

function ShowWindow() {
    if ($('.globalFlag').val() == 0) { /*окно отображается один раз после входа*/
        $('.popup .close_window, .overlay').click(function (){
            $('.popup, .overlay').css({'opacity':'0', 'visibility':'hidden'});
        });
        $('.popup, .overlay').css({'opacity':'1', 'visibility':'visible'});
       }
    }