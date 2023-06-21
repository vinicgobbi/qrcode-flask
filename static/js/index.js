let section = document.querySelector("section")
function qrhtml(type) {
    if (type == 'link'){
        section.innerHTML = `<form name="infos" action="/generate_link" method="post">
    <label for="infos" class="label" id="label">Link:</label>
    <input type="text" class="infos" id="infos" name="link">

    <div>
        <button id="enviar" class="enviar" type="submit">Gerar QR Code</button>
    </div>
</form>
    `
    }else{
        section.innerHTML = `<form id="form" name="infos" action="/generate_email" method="post">
    <label for="infos" class="label" id="label">Destinatário:</label>
    <input type="text" class="infos" id="infos" name="destinatario">

    <label for="infos" class="label" id="label">Assunto:</label>
    <input type="text" class="infos" id="infos" name="assunto">

    <label for="infos" class="label" id="label">Texto:</label>
    <textarea name="texto" id="email" cols="50" rows="10" wrap="hard"></textarea>
    <div>
        <button id="enviar" class="enviar" type="submit">Gerar QR Code</button>
    </div>
</form>`
    }
}

