# Variables

college = input("College/University Name: ")
event = input("Event Name: ")
student = input("Student Name: ")
date = input("Date (dd/mm/yyyy): ")
time = input("Time: ")
venue = input("Venue: ")
chief_guest = input("Chief Guest: ")
organizer = input("Organizer: ")
logo = input("Logo URL: ")

#ashol jinis
file = open('Invitation card.html', 'w+')
file.write(f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{event}</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<style>

body{{
    background:#eaf4ff;
    font-family:Arial,sans-serif;
}}

.invitation{{
    width:900px;
    margin:40px auto;
    background:#ffffff;
    border:8px solid #0d6efd;
    border-radius:20px;
    padding:50px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
}}

.logo{{
    width:100px;
    height:100px;
    object-fit:cover;
    border-radius:50%;
}}

.college{{
    font-size:32px;
    color:#0d6efd;
    font-weight:bold;
}}

.heading{{
    font-size:52px;
    color:#003366;
    font-weight:bold;
    margin-top:20px;
}}

.event{{
    font-size:36px;
    color:#0d6efd;
    font-weight:bold;
    margin:20px 0;
}}

.message{{
    font-size:21px;
    color:#444;
    line-height:1.8;
    margin:30px 0;
}}

table{{
    width:80%;
    margin:auto;
}}

table th{{
    background:#0d6efd;
    color:white;
    width:35%;
}}

table td{{
    background:#f8fbff;
}}

.footer{{
    margin-top:40px;
    text-align:center;
    font-size:20px;
    color:#555;
}}

.buttons{{
    text-align:center;
    margin:30px;
}}

</style>

</head>

<body>

<div class="invitation">

<div class="text-center">

<img src="{logo}" class="logo mb-3">

<div class="college">
{college}
</div>

<div class="heading">
STUDENT EVENT INVITATION
</div>

<div class="event">
{event}
</div>

<p class="message">

Dear <b>{student}</b>,

<br><br>

You are cordially invited to attend the <b>{event}</b> organized by <b>{college}</b>. The program will be held on <b>{date}</b> at <b>{time}</b> in <b>{venue}</b>. Your presence and participation will make this occasion more meaningful and memorable. We warmly welcome you to join us and be a part of this special event.

</p>

<table class="table table-bordered">

<tr>
<th>Date</th>
<td>{date}</td>
</tr>

<tr>
<th>Time</th>
<td>{time}</td>
</tr>

<tr>
<th>Venue</th>
<td>{venue}</td>
</tr>

<tr>
<th>Chief Guest</th>
<td>{chief_guest}</td>
</tr>

<tr>
<th>Organizer</th>
<td>{organizer}</td>
</tr>

</table>

<div class="footer">

We are looking forward to your gracious presence.

<br><br>

<b>{college}</b>

</div>

</div>

</div>

<div class="buttons">

<button onclick="window.print()" class="btn btn-primary px-4">
Print Invitation
</button>

</div>

</body>

</html>
""")
file.close()
print('Invitation card created Successfully')
