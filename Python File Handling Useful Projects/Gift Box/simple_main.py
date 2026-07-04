sender_name = input('Type Sender Name:')
receiver_name = input('Type Reciver Name:')
message = input('Type Your Massage:')

file = open("gift.html","w+",encoding="utf-8")

file.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Gift Card</title>

<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;500&display=swap" rel="stylesheet">

<style>

*{{
margin:0;
padding:0;
box-sizing:border-box;
}}

body{{

height:100vh;
overflow:hidden;
display:flex;
justify-content:center;
align-items:center;
font-family:Poppins,sans-serif;
background:
linear-gradient(135deg,#180018,#330033,#4d004d,#2b001d);
position:relative;

}}

body::before{{
content:'';
position:absolute;
width:200%;
height:200%;
background:
radial-gradient(circle,#ff4fa311 2px,transparent 2px);
background-size:80px 80px;
animation:bgmove 30s linear infinite;
}}

@keyframes bgmove{{

from{{transform:translateY(0);}}
to{{transform:translateY(-200px);}}

}}

.container{{
z-index:5;
text-align:center;
}}

.title{{
color:white;
font-size:35px;
}}

.sub{{
color:pink;
font-size:28px;
margin-bottom:20px;
}}

.click{{
margin-top:20px;
display:inline-block;
padding:12px 30px;
background:#ff4fa3;
border-radius:40px;
cursor:pointer;
color:white;
transition:.4s;
}}

.click:hover{{
transform:scale(1.1);
box-shadow:0 0 20px hotpink;
}}

.gift{{
position:relative;
width:250px;
height:180px;
margin:auto;
transition:1.5s;
}}

.box{{
position:absolute;
bottom:0;
width:250px;
height:130px;
background:#111;
border-radius:12px;
box-shadow:0 20px 40px #000;
}}

.lid{{
position:absolute;
top:0;
width:250px;
height:50px;
background:#222;
border-radius:12px;
transition:1.5s;
transform-origin:left;
}}

.ribbon-v{{
position:absolute;
left:110px;
width:30px;
height:180px;
background:#ff3ea5;
}}

.ribbon-h{{
position:absolute;
top:20px;
width:250px;
height:25px;
background:#ff3ea5;
}}

.bow{{
position:absolute;
top:5px;
left:95px;
font-size:45px;
color:#ff69b4;
}}

.message{{
opacity:0;
transition:2s;
margin-top:40px;
font-family:'Great Vibes',cursive;
font-size:52px;
color:#ffd2ea;
text-shadow:0 0 15px hotpink;
}}

.open .lid{{
transform:rotate(-130deg) translateY(-20px);
}}

.open .message{{
opacity:1;
}}

.flower{{
position:absolute;
font-size:35px;
opacity:0;
animation:float 7s linear infinite;
}}

@keyframes float{{

0%{{
transform:translateY(120vh) rotate(0deg);
opacity:0;
}}

10%{{opacity:1;}}

100%{{
transform:translateY(-120vh) rotate(360deg);
opacity:0;
}}

}}

</style>

</head>

<body>

<div class="container">

<div class="title">
Gift by "{sender_name}"
</div>

<div class="sub">
For {receiver_name}
</div>

<div id="gift" class="gift">

<div class="lid"></div>

<div class="box"></div>

<div class="ribbon-v"></div>

<div class="ribbon-h"></div>

<div class="bow">🎀</div>

</div>

<div class="click" onclick="openGift()">
Click Here
</div>

<div class="message" id="msg">
{message}
</div>

</div>

<script>

function flower(){{

let f=document.createElement("div");

f.className="flower";

f.innerHTML=["🌸","🌺","💮","🌷","🌹"][Math.floor(Math.random()*5)];

f.style.left=Math.random()*100+"vw";

f.style.animationDuration=(4+Math.random()*4)+"s";

f.style.fontSize=(25+Math.random()*30)+"px";

document.body.appendChild(f);

setTimeout(()=>{{

f.remove();

}},8000);

}}

function openGift(){{

document.getElementById("gift").classList.add("open");

document.getElementById("msg").style.opacity=1;

setInterval(flower,180);

}}

</script>

</body>
</html>
''')

file.close()

print("gift successfully created")