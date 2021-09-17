$(function() {
jQuery('#myform').submit(function(event){
        
    // alert(jQuery('#login-form').serialize());
    
    var formData = {
    text: $("#comment").val(),
};  
    jQuery.ajax({
        url:"/prediction",
        data:formData,
        type:'POST',
        dataType:'json',
        success:function(result){
            // alert(result.text).show();
          
            swal.fire({
                icon:'success',
                title: 'Genere Result',
                html: '<h5>"'+result.prediction+'"</h5>',
                background:'#000000',
                showConfirmButton:false,
                timer: 3000,
                // footer: '<a href="">Why do I have this issue?</a>'
              })
            // $('label[for="genre-result"]').text(result.prediction)
            console.log(result.prediction);
        }
    });
    
    event.preventDefault();
    // var $form =$(this),
    // email=$form.find("input[name='email']").val(),
    // email=$form.find("input[name='pass']").val(),
});
})