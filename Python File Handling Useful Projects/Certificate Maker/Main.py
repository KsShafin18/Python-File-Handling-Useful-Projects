#Variables 
title = input('Name for your certificate:')
organization = input('Organization Name:')
participant = input('Participant Name:')
description = f'This {title} certificate is proudly presented in recognition of your dedication, hard work, and valuable contribution. Your commitment and excellence have made a meaningful impact, and we sincerely appreciate your achievements.'
coordinator = input('Sir/Trainer Name:')
director = input('Director Name:')
date =input('dd/mm/yyyy:')
certificate_id =input('Type ID No:')
logo = input('Logo url:')
qr = 'qr.png'
seal = 'seal.png'


#File_Handling_operation
file = open('Certificate.html', 'w+', encoding='utf-8')

file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{title}</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>

<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@700&family=Poppins:wght@300;400;600&family=Great+Vibes&display=swap" rel="stylesheet">

<style>

/* ===== BODY ===== */
body{{
    background:#f3efe6;
    font-family:'Poppins',sans-serif;
    margin:0;
    padding:0;
}}

/* ===== CERTIFICATE BOX ===== */
.certificate{{
    width:1100px;
    margin:40px auto;
    background:#fbf7ef;
    border:8px solid #6b3d23;
    padding:50px;
    box-shadow:0 10px 30px rgba(0,0,0,0.15);
}}

/* INNER BORDER */
.inner-border{{
    border:2px solid #6b3d23;
    padding:40px;
}}

/* LOGO */
.logo{{
    width:90px;
    height:90px;
    object-fit:cover;
}}

/* COMPANY NAME */
.company{{
    font-size:28px;
    font-weight:600;
    color:#3b2a1a;
}}

/* MAIN HEADING */
.heading{{
    font-family:'Cormorant Garamond',serif;
    font-size:62px;
    font-weight:bold;
    letter-spacing:2px;
    color:#2b1b10;
}}

/* SUBTITLE */
.subtitle{{
    font-size:24px;
    letter-spacing:3px;
    color:#555;
}}

/* NAME */
.name{{
    font-family:'Great Vibes',cursive;
    font-size:72px;
    margin:25px 0;
    color:#1f1f1f;
}}

/* DESCRIPTION */
.description{{
    font-size:20px;
    color:#444;
    max-width:850px;
    margin:auto;
    line-height:1.6;
}}

/* SIGNATURE LINE */
.signature-line{{
    border-top:2px solid #000;
    width:260px;
    margin:auto;
    margin-bottom:10px;
}}

/* QR */
.qr{{
    width:120px;
}}

/* SEAL */
.seal{{
    width:110px;
}}

/* SMALL TEXT */
.footer-small{{
    font-size:14px;
    color:#666;
}}

/* BUTTON AREA */
.buttons{{
    text-align:center;
    margin:30px 0 50px;
}}

</style>

</head>

<body>

<div class="certificate">

<div class="inner-border">

<div class="text-center">

<img src="{logo}" class="logo rounded-circle mb-3">

<h3 class="company">{organization}</h3>

<h1 class="heading text-uppercase mt-3">
CERTIFICATE OF APPRECIATION
</h1>

<h4 class="subtitle mt-3">
THIS CERTIFICATE IS GIVEN TO
</h4>

<div class="name">
{participant}
</div>

<p class="description">
{description}
</p>

</div>

<div class="row mt-5 align-items-end">

<div class="col text-center">
<div class="signature-line"></div>
<h5>{coordinator}</h5>
<p>Program Coordinator</p>
</div>

<div class="col text-center">
<img src="{qr}" class="qr">
<p class="footer-small">{certificate_id}</p>
</div>

<div class="col text-center">
<img src="{seal}" class="seal">
</div>

<div class="col text-center">
<div class="signature-line"></div>
<h5>{director}</h5>
<p>Executive Director</p>
</div>

</div>

<div class="text-center mt-4">
<p class="footer-small">
Issued on <b>{date}</b>
</p>
</div>

</div>

</div>

<!-- BUTTONS -->
<div class="buttons">

    <button onclick="window.print()" class="btn btn-danger px-4">
        Print
    </button>

    <button onclick="downloadPDF()" class="btn btn-success px-4">
        Download
    </button>

</div>

<script>
function downloadPDF(){{
    const el = document.querySelector(".certificate");

    html2pdf()
    .from(el)
    .set({{
        filename: "{participant}_certificate.pdf",
        html2canvas: {{
            scale: 2
        }},
        jsPDF: {{
            format: "a4",
            orientation: "landscape"
        }}
    }})
    .save();
}}
</script>

</body>
</html>
""")

file.close()
print("Certificate Generated Successfully!")