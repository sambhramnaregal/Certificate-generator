from flask import Flask, request, send_file, render_template_string
from pathlib import Path
from generate_certificate import generate_certificate_pdf

app = Flask(__name__)

HTML_FORM = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Internship Certificate Generator</title>

<style>
    body {
        font-family: 'Georgia', serif;
        background: #f4f4f4;
        text-align: center;
    }

    .container {
        margin-top: 20px;
    }

    input {
        padding: 10px;
        margin: 10px;
        font-size: 16px;
    }

    button {
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        background: #1f3c5c;
        color: white;
        border: none;
        border-radius: 5px;
        margin: 10px 5px;
    }

    button:hover {
        background: #0f2c4c;
    }

    /* Certificate Design */
    .certificate {
        width: 900px;
        height: 600px;
        margin: 30px auto;
        background: white;
        border: 15px solid #1f3c5c;
        position: relative;
        padding: 40px;
        box-shadow: 0 0 20px rgba(0,0,0,0.2);
    }

    .certificate::before {
        content: "";
        position: absolute;
        top: 10px;
        left: 10px;
        right: 10px;
        bottom: 10px;
        border: 5px solid #d4af37;
    }

    h1 {
        color: #1f3c5c;
        margin-top: 20px;
    }

    .title {
        font-size: 30px;
        font-weight: bold;
        margin: 20px 0;
    }

    .name {
        font-size: 28px;
        font-weight: bold;
        color: #000;
        margin: 20px 0;
    }

    .text {
        font-size: 18px;
        margin: 10px 0;
    }

    .date {
        margin-top: 40px;
        font-size: 18px;
    }

    .signature {
        position: absolute;
        bottom: 40px;
        right: 80px;
        text-align: center;
    }

    .signature-line {
        border-top: 2px solid black;
        width: 150px;
        margin: auto;
    }

    .input-group {
        margin: 20px 0;
    }

    .button-group {
        margin: 20px 0;
    }

    .hidden {
        display: none;
    }
</style>
</head>

<body>

<div class="container">
    <h2>Internship Certificate Generator</h2>

    <div class="input-group">
        <input type="text" id="nameInput" placeholder="Enter Name">
        <input type="date" id="dateInput">
    </div>

    <div class="button-group">
        <button onclick="generateCertificate()">Generate Certificate</button>
        <button onclick="downloadPDF()" class="hidden" id="downloadBtn">Download as PDF</button>
    </div>
</div>

<div class="certificate" id="certificate">
    <h1>SwipeGen</h1>

    <div class="title">CERTIFICATE OF COMPLETION</div>

    <div class="text">This is to certify that</div>

    <div class="name" id="name">[Name]</div>

    <div class="text">
        has successfully completed the internship program in<br>
        <b>CSE (Data Science) / AI & ML</b> at our organization.<br><br>
        During this period, the intern demonstrated dedication,
        technical skills, and professionalism in all assigned tasks.
    </div>

    <div class="date">
        Date: <span id="date">[Date]</span>
    </div>

    <div class="signature">
        <div class="signature-line"></div>
        <div>Authorized Signatory</div>
    </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script>
function generateCertificate() {
    const name = document.getElementById("nameInput").value;
    const date = document.getElementById("dateInput").value;

    if (!name || !date) {
        alert("Please enter both name and date");
        return;
    }

    document.getElementById("name").innerText = name;
    document.getElementById("date").innerText = date;
    document.getElementById("downloadBtn").classList.remove("hidden");
}

function downloadPDF() {
    const element = document.getElementById("certificate");
    const name = document.getElementById("nameInput").value;
    const opt = {
        margin: 10,
        filename: name + "_Certificate.pdf",
        image: { type: "png", quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { orientation: "landscape", unit: "mm", format: "a4" }
    };
    html2pdf().set(opt).save().from(element).save();
}
</script>

</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    app.run(debug=True)
