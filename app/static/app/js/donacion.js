$(document).ready(function(){
    $('#emailinput').on("input", function(){
        if($('#emailinput').val() == ""){
            $('#emailinput').removeClass("ok")
            $('#emailinput').addClass("error")
            $("#mensaje").show()
        } else {
            $("#emailinput").removeClass("error")
            $("#emailinput").addClass("ok")
            $("#mensaje").hide()
        }
    });

    $('#monto').on("input", function(){
        if($('#monto').val() == ""){
            $("#monto").removeClass("ok")
            $("#monto").addClass("error")
            $("#mensaje2").show()
        } else {
            $("#monto").removeClass("error")
            $("#monto").addClass("ok")
            $("#mensaje2").hide()
        }
    });

    $('#numerotarjeta').on("input", function(){
        if($('#numerotarjeta').val() == "" || $('#numerotarjeta').val().length != 16){
            $("#numerotarjeta").removeClass("ok")
            $("#numerotarjeta").addClass("error")
            $("#mensaje3").show()
        } else {
            $("#numerotarjeta").removeClass("error")
            $("#numerotarjeta").addClass("ok")
            $("#mensaje3").hide()
        }
    });

    $('#cvv').on("input", function(){
        if($('#cvv').val() == "" || $('#cvv').val().length != 3){
            $("#cvv").removeClass("ok")
            $("#cvv").addClass("error")
            $("#mensaje4").show()
        } else {
            $("#cvv").removeClass("error")
            $("#cvv").addClass("ok")
            $("#mensaje4").hide()
        }
    });

    $('#fecha').on("input", function(){
        if($('#fecha').val() == "" || $('#fecha').val().length != 5){
            $("#fecha").removeClass("ok")
            $("#fecha").addClass("error")
            $("#mensaje5").show()
        } else {
            $("#fecha").removeClass("error")
            $("#fecha").addClass("ok")
            $("#mensaje5").hide()
        }
    });
    
    $('#donar').submit(function(){
        if($('#emailinput').val() == ""){
            alert('El email está vacío')
            event.preventDefault()
        } else if($('#monto').val() == ""){
            alert('El monto está vacío')
            event.preventDefault()
        } else if($('#numerotarjeta').val() == ""){
            alert('La tarjeta está vacía')
            event.preventDefault()
        } else if($('#cvv').val() == ""){
            alert('El CVV está vacío')
            event.preventDefault()
        } else if($('#fecha').val() == ""){
            alert('La fecha de vencimiento está vacía')
            event.preventDefault()
        } else {
            alert('Formulario enviado')
        }
    })
})