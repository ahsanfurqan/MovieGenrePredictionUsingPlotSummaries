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
            $('label[for="genre-result"]').text('Genre = '+result.prediction)
            console.log(result.prediction);
        }
    });
    
    event.preventDefault();
    // var $form =$(this),
    // email=$form.find("input[name='email']").val(),
    // email=$form.find("input[name='pass']").val(),
});
})