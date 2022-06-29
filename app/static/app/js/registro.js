
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

    $('#correo').on("input", function(){
        if($('#correo').val() == ""){
            $('#correo').removeClass("ok")
            $('#correo').addClass("error")
            $("#mensaje2").show()
        } else {
            $("#correo").removeClass("error")
            $("#correo").addClass("ok")
            $("#mensaje2").hide()
        }
    });

    $('#passwordinput').on("input", function(){
        if($('#passwordinput').val() == ""){
            $("#passwordinput").removeClass("ok")
            $("#passwordinput").addClass("error")
            $("#mensaje3").show()
        } else {
            $("#passwordinput").removeClass("error")
            $("#passwordinput").addClass("ok")
            $("#mensaje3").hide()
        }
    });
    
    $('#form1').submit(function(){
        if($('#username').val() == ""){
            alert('El usuario está vacío')
            event.preventDefault()
        } else if($('#passwordinput').val() == ""){
            alert('La contraseña está vacía')
            event.preventDefault()
        } else if($('#correo').val() == ""){
            alert('El correo está vacía')
            event.preventDefault()
        } else {
            alert('Formulario enviado')
        }
    })
})