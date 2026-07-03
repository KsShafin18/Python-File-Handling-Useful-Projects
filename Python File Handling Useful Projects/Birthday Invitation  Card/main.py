# Variables

birthday_person = input("Birthday Person Name: ")
age = input("Turning Age: ")
date = input("Date (dd/mm/yyyy): ")
time = input("Time: ")
venue = input("Venue: ")
host = input("Host Name: ")
theme = input("Party Theme: ")
image = input("Birthday Image URL: ")

# File Handling

file = open("BirthdayInvitation.html", "w",)

file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Birthday Invitation</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<style>

body{{
    background:linear-gradient(135deg,#ff9a9e,#fad0c4,#fad390);
    font-family:Arial,sans-serif;
}}

.invitation{{
    width:850px;
    margin:40px auto;
    background:white;
    padding:40px;
    border-radius:20px;
    text-align:center;
    box-shadow:0 10px 30px rgba(0,0,0,.2);
}}

img{{
    width:180px;
    height:180px;
    object-fit:cover;
    border-radius:50%;
    border:6px solid #ff4081;
}}

h1{{
    color:#ff4081;
    font-size:55px;
    margin-top:20px;
}}

.name{{
    font-size:45px;
    font-weight:bold;
    color:#6a1b9a;
}}

.details{{
    font-size:22px;
    margin-top:20px;
    line-height:1.8;
}}

.footer{{
    margin-top:35px;
    font-size:22px;
    color:#444;
}}

.buttons{{
    text-align:center;
    margin-bottom:40px;
}}

</style>

</head>

<body>

<div class="invitation">

<img src="{image}">

<h1>Birthday Party</h1>

<p>You are invited to celebrate</p>

<div class="name">
{birthday_person}'s {age} Birthday
</div>

<div class="details">

<p><b>Date:</b> {date}</p>

<p><b>Time:</b> {time}</p>

<p><b>Venue:</b> {venue}</p>

<p><b>Theme:</b> {theme}</p>

</div>

<div class="footer">

Hosted by <b>{host}</b>

<br><br>

We hope you can join us for a day filled with fun, laughter and wonderful memories!

</div>

</div>

<div class="buttons">

<button class="btn btn-danger px-4" onclick="window.print()">
Print Invitation
</button>

</div>

</body>
</html>
""")

file.close()

print("Birthday Invitation Generated Successfully!")