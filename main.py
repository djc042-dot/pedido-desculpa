from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Eu preciso te falar isso...</title>
    <style>
        body {
            background: linear-gradient(to right, #ff758c, #ff7eb3);
            font-family: Arial, sans-serif;
            text-align: center;
            color: white;
            padding: 60px;
        }
        .box {
            background: rgba(0,0,0,0.35);
            padding: 40px;
            border-radius: 20px;
            max-width: 600px;
            margin: auto;
        }
        button {
            background: white;
            color: #ff4d6d;
            border: none;
            padding: 15px 25px;
            font-size: 16px;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 25px;
        }
        button:hover {
            background: #ffe0e6;
        }
    </style>
</head>
<body>

    <div class="box">
        <h1>Eu errei... e reconheço isso 😔</h1>

        <p>
            Eu fiquei pensando muito em tudo que aconteceu...<br><br>

            Eu sei que minhas atitudes te machucaram,
            e eu assumo isso de verdade.<br><br>

            Eu não tô aqui só pra pedir desculpa...<br>
            tô aqui porque eu entendi que preciso mudar.<br><br>

            Eu tô disposto a ser melhor, aprender com meus erros
            e agir diferente daqui pra frente.<br><br>

            Eu sei que palavras não provam nada,
            mas eu quero te mostrar isso com atitudes.<br><br>

            Você é muito importante pra mim ❤️
        </p>

        <button onclick="mostrarMensagem()">
            Me dá uma chance de mostrar que eu posso ser melhor?
        </button>

        <p id="resposta" style="margin-top:20px;"></p>
    </div>

    <script>
        function mostrarMensagem() {
            document.getElementById("resposta").innerHTML =
            "Eu não espero resposta agora... só queria que você soubesse disso ❤️";
        }
    </script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)