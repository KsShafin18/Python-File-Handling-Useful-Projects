# vars
company = input("Company Name: ")
name = input("Your Name: ")
designation = input("Designation: ")
phone = input("Phone Number: ")
email = input("Email Address: ")
website = input("Website: ")
address = input("Office Address: ")
logo = input("Logo URL: ")

# File Handling operations
file = open("BusinessCard.html", "w+",)

file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Business Card</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>

body{{
    background:#ececec;
    font-family:'Poppins',sans-serif;
}}

.card-box{{
    width:850px;
    height:450px;
    margin:50px auto;
    border-radius:20px;
    overflow:hidden;
    display:flex;
    box-shadow:0 10px 30px rgba(0,0,0,.2);
}}

.left{{
    width:35%;
    background:#0d6efd;
    color:white;
    text-align:center;
    padding:40px 20px;
}}

.left img{{
    width:130px;
    height:130px;
    object-fit:cover;
    border-radius:50%;
    border:5px solid white;
    margin-bottom:20px;
}}

.company{{
    font-size:28px;
    font-weight:bold;
}}

.right{{
    width:65%;
    background:white;
    padding:50px;
}}

.name{{
    font-size:40px;
    font-weight:bold;
    color:#0d6efd;
}}

.designation{{
    font-size:22px;
    color:#555;
    margin-bottom:35px;
}}

.info{{
    font-size:20px;
    margin:15px 0;
}}

.footer{{
    margin-top:40px;
    font-size:18px;
    color:#666;
}}

.buttons{{
    text-align:center;
    margin-bottom:50px;
}}

</style>

</head>

<body>

<div class="card-box">

<div class="left">

<img src="{logo}">

<div class="company">
{company}
</div>

</div>

<div class="right">

<div class="name">
{name}
</div>

<div class="designation">
{designation}
</div>

<div class="info">
 {phone}
</div>

<div class="info">
 {email}
</div>

<div class="info">
 {website}
</div>

<div class="info">
 {address}
</div>

<div class="footer">
Thank you for your business.
</div>

</div>

</div>

<div class="buttons">

# Buttons
<button class="btn btn-primary" onclick="window.print()">
Print Card
</button>

</div>

</body>
</html>
""")

file.close()

print("Business Card Generated Successfully!")