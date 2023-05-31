function ajax(route) {
    // Prelevare il testo dalla TA 
    let TA = document.getElementById("TA");
    let testo = TA.value;

    if (testo) {
        //Invio testo alla rout
        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                //rimettere il testo nella TA
                TA.value = this.responseText;
                //document.getElementById('dina').innerHTML = this.responseText;
            }
        };
        xhttp.open("GET", route + "?text=" + testo, true);
        xhttp.send();
    }

    else{
        alert("non hai inserito il testo!!!!");
    }
}