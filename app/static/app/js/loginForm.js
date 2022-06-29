$(document).ready(function(){
    $('#username').on("input", function(){
        if($('#username').val() == ""){
            $('#username').removeClass("ok")
            $('#username').addClass("error")
            $("#mensaje").show()
        } else {
            $("#username").removeClass("error")
            $("#username").addClass("ok")
            $("#mensaje").hide()
        }
    });

    $('#passwordinput').on("input", function(){
        if($('#passwordinput').val() == ""){
            $("#passwordinput").removeClass("ok")
            $("#passwordinput").addClass("error")
            $("#mensaje2").show()
        } else {
            $("#passwordinput").removeClass("error")
            $("#passwordinput").addClass("ok")
            $("#mensaje2").hide()
        }
    });
    
    $('#form1').submit(function(){
        if($('#username').val() == ""){
            alert('El usuario está vacío')
            event.preventDefault()
        } else if($('#passwordinput').val() == ""){
            alert('La contraseña está vacía')
            event.preventDefault()
        } else {
            alert('Formulario enviado')
        }
    })
})