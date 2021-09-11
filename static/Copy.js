function copyfunction(element,btn_id){
    var $temp = $("<input>");
    var btn=document.getElementById(btn_id)
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();
    btn.innerText='Copied';
    setTimeout(function() {
        btn.innerText='Copy';
      }, 4000);
}
