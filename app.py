from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Love Message</title>
    <style>
        body {
            background: radial-gradient(circle, rgba(255,182,193,1) 20%, rgba(255,105,180,1) 60%, rgba(255,20,147,1) 100%);
            text-align: center;
            font-family: 'Comic Sans MS', cursive, sans-serif;
            color: white;
        }
        .container {
            margin-top: 15%;
        }
        .btn {
            background-color: #ff1493;
            color: white;
            padding: 15px 30px;
            border: none;
            font-size: 20px;
            border-radius: 20px;
            cursor: pointer;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }
        .btn:hover {
            background-color: #ff007f;
            transform: scale(1.1);
        }
        .hidden {
            display: none;
            font-size: 22px;
            margin-top: 20px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            opacity: 0;
            transform: translateY(-20px);
            transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
        }
        .heart {
            font-size: 30px;
            animation: heartbeat 1s infinite;
        }
        @keyframes heartbeat {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        .show {
            display: block;
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🎂 Happy Birthday LINDA NABILA LESTARI, a special person who is bringing so much joy to my heart 🎂</h2>
        <button class="btn" onclick="showMessage()">Please click this ❤️</button>
        <p id="message" class="hidden">
            halooo sayanggggkuuu, on this day was your favourite day. happy birthday my princess. semogaa sehat selaluu panjang umurr, dan tetap menjadii lindaa yangg akuu kenall yaaa sayanggg. bertambahnyaa usia kamu semogaa menjadii seseorang yangg lebih baik darii sebelumnyaa, di lancarkan kuliahnyaa. I always lucky to have u, and always proud of u,i wish u all the best for uu!! Always remember, no matter what happens, I'll always be here for youuuu!<br><br>
            <b>JANLUPPP WALAUU SUDAA BERTAMBAHH UMURR BAWELL NYAA JANGANN ILANGG YAAA??</b> <br><br>
            I ALWAYSS LOVEE UU SAYANGGGG <span class="heart">❤️❤️❤️❤️❤️❤️❤️❤️❤️</span>
        </p>
    </div>
    <script>
        function showMessage() {
            let message = document.getElementById('message');
            message.classList.add('show');
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)