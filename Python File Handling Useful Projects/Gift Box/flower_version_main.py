import json
import html

sender_name = input("Type Sender Name: ")
receiver_name = input("Type Receiver Name: ")
message = input("Type Your Message: ")

# Safe versions for embedding
sender_html = html.escape(sender_name)
receiver_html = html.escape(receiver_name)
message_js = json.dumps(message)  # safe JS string literal (already quoted)

file = open("gift.html", "w", encoding="utf-8")
file.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>A Gift For {receiver_html}</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;600&display=swap');

  * {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }}

  html, body {{
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #060109;
    font-family: 'Poppins', sans-serif;
  }}

  .scene {{
    position: fixed;
    inset: 0;
    overflow: hidden;
  }}

  .bg-gradient {{
    position: absolute;
    inset: -10%;
    background:
      radial-gradient(circle at 30% 20%, #3a0a3a, transparent 60%),
      radial-gradient(circle at 70% 80%, #1a0033, transparent 60%),
      linear-gradient(135deg, #0d0014, #2b0022 40%, #1a0510 70%, #05000a);
    background-size: 200% 200%;
    animation: bgShift 18s ease-in-out infinite;
    transition: filter 1.6s ease, transform 1.6s ease;
    filter: saturate(1.1);
  }}

  .bg-gradient.blurred {{
    filter: blur(14px) brightness(0.55) saturate(1.3);
    transform: scale(1.08);
  }}

  @keyframes bgShift {{
    0% {{ background-position: 0% 0%; }}
    50% {{ background-position: 100% 100%; }}
    100% {{ background-position: 0% 0%; }}
  }}

  .particles {{
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 2;
  }}

  .particle {{
    position: absolute;
    top: -5%;
    will-change: transform, opacity;
    animation-name: floatDown;
    animation-timing-function: linear;
    animation-fill-mode: forwards;
  }}

  @keyframes floatDown {{
    0%   {{ transform: translate(0, -10vh) rotate(0deg); opacity: 0; }}
    10%  {{ opacity: 1; }}
    90%  {{ opacity: 1; }}
    100% {{ transform: translate(var(--drift, 40px), 110vh) rotate(360deg); opacity: 0; }}
  }}

  .stage {{
    position: relative;
    z-index: 5;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 28px;
    perspective: 1400px;
  }}

  .labels {{
    text-align: center;
    color: #ffd7ec;
    opacity: 0;
    animation: labelFade 1.6s ease forwards 0.3s;
  }}

  @keyframes labelFade {{
    from {{ opacity: 0; transform: translateY(-14px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
  }}

  .gift-by {{
    font-size: 26px;
    font-weight: 600;
    letter-spacing: 2px;
    text-shadow: 0 0 18px rgba(255,120,190,0.75), 0 0 40px rgba(255,90,180,0.4);
  }}

  .for-you {{
    margin-top: 6px;
    font-size: 17px;
    font-weight: 300;
    letter-spacing: 4px;
    color: #ffc2e2;
    opacity: 0.85;
  }}

  .gift-wrap {{
    position: relative;
    width: 260px;
    height: 210px;
  }}

  .box-container {{
    position: absolute;
    inset: 0;
    width: 260px;
    height: 210px;
    transform-style: preserve-3d;
    transition: transform 1s ease, opacity 1s ease;
  }}

  .box-container.shrink {{
    transform: scale(0.4) translateY(40px);
    opacity: 0;
  }}

  .box-body {{
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 130px;
    background: linear-gradient(155deg, #1c1c1f, #050505 55%, #000);
    border-radius: 14px;
    box-shadow:
      0 25px 60px rgba(0,0,0,0.7),
      0 0 40px rgba(255,70,160,0.15),
      inset 0 0 25px rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.06);
  }}

  .box-lid {{
    position: absolute;
    top: 40px;
    left: -4px;
    width: calc(100% + 8px);
    height: 60px;
    background: linear-gradient(155deg, #222226, #08080a 60%, #000);
    border-radius: 16px 16px 6px 6px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.6), inset 0 0 20px rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.07);
    transform-origin: top center;
    transform-style: preserve-3d;
    transition: transform 1.3s cubic-bezier(0.6,-0.2,0.3,1.3), box-shadow 1.3s ease;
    z-index: 6;
  }}

  .box-lid.open {{
    transform: rotateX(-125deg) translateY(-6px);
    box-shadow: 0 40px 60px rgba(255,80,170,0.25);
  }}

  .ribbon-vertical {{
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 26px;
    height: 100%;
    background: linear-gradient(180deg, #ff9ecf, #ff2f92 45%, #d1006a);
    box-shadow: 0 0 18px rgba(255,80,170,0.85), 0 0 40px rgba(255,60,160,0.5);
    z-index: 7;
    transition: transform 1.1s ease, opacity 1.1s ease;
  }}

  .ribbon-horizontal {{
    position: absolute;
    top: 46px;
    left: -6px;
    width: calc(100% + 12px);
    height: 24px;
    background: linear-gradient(90deg, #ff9ecf, #ff2f92 45%, #d1006a);
    box-shadow: 0 0 18px rgba(255,80,170,0.85), 0 0 40px rgba(255,60,160,0.5);
    z-index: 7;
    transition: transform 1.1s ease, opacity 1.1s ease;
  }}

  .untie .ribbon-vertical {{
    transform: translateX(-50%) translateY(-140px) rotate(15deg);
    opacity: 0;
  }}

  .untie .ribbon-horizontal {{
    transform: translateY(-40px) scaleX(1.3);
    opacity: 0;
  }}

  .bow {{
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 90px;
    height: 50px;
    z-index: 8;
    transition: transform 1s ease, opacity 1s ease;
  }}

  .bow-half {{
    position: absolute;
    top: 0;
    width: 40px;
    height: 40px;
    background: linear-gradient(135deg, #ffb3d9, #ff2f92);
    box-shadow: 0 0 20px rgba(255,90,180,0.9);
    border-radius: 50% 50% 50% 0;
  }}

  .bow-half.left {{
    left: 0;
    transform: rotate(45deg);
  }}

  .bow-half.right {{
    right: 0;
    transform: rotate(-135deg);
  }}

  .bow-knot {{
    position: absolute;
    top: 12px;
    left: 50%;
    transform: translateX(-50%);
    width: 20px;
    height: 20px;
    background: #ff5aa8;
    border-radius: 6px;
    box-shadow: 0 0 18px rgba(255,110,190,0.95);
  }}

  .untie .bow {{
    transform: translateX(-50%) translateY(-30px) scale(0.8) rotate(20deg);
    opacity: 0;
  }}

  .bouquet {{
    position: absolute;
    bottom: 90px;
    left: 50%;
    transform: translate(-50%, 40px) scale(0.55);
    opacity: 0;
    z-index: 4;
    transition: transform 1.6s cubic-bezier(0.34,1.4,0.4,1), opacity 1.2s ease;
  }}

  .bouquet.rise {{
    transform: translate(-50%, -60px) scale(0.85);
    opacity: 1;
  }}

  .bouquet.center {{
    transform: translate(-50%, -35px) scale(1.35) rotate(180deg);
  }}

  .bouquet.floating {{
    animation: bouquetFloat 4s ease-in-out infinite;
  }}

  @keyframes bouquetFloat {{
    0%, 100% {{ transform: translate(-50%, -35px) scale(1.35) rotate(178deg); }}
    50%      {{ transform: translate(-50%, -50px) scale(1.35) rotate(182deg); }}
  }}

  .stem {{
    position: absolute;
    bottom: -10px;
    width: 5px;
    height: 90px;
    background: linear-gradient(180deg, #3fae5a, #1c5c30);
    border-radius: 3px;
    transform-origin: bottom center;
  }}

  .leaf {{
    position: absolute;
    width: 22px;
    height: 12px;
    background: linear-gradient(135deg, #58c777, #226b38);
    border-radius: 50% 50% 50% 0;
  }}

  .flower {{
    position: absolute;
    width: 46px;
    height: 46px;
  }}

  .petal {{
    position: absolute;
    width: 24px;
    height: 30px;
    left: 11px;
    top: -7px;
    background: radial-gradient(circle at 50% 75%, #ffe2f2, #ff8fc7 55%, #ff3f97);
    border-radius: 50% 50% 50% 50% / 65% 65% 35% 35%;
    transform-origin: 50% 100%;
    box-shadow: 0 0 10px rgba(255,140,200,0.6);
  }}

  .flower-center {{
    position: absolute;
    width: 14px;
    height: 14px;
    left: 16px;
    top: 16px;
    background: radial-gradient(circle, #fff3b0, #ffce4a);
    border-radius: 50%;
    box-shadow: 0 0 12px rgba(255,220,120,0.9);
    z-index: 2;
  }}

  .click-btn {{
    padding: 14px 38px;
    font-size: 17px;
    font-weight: 600;
    letter-spacing: 1px;
    color: #fff;
    background: linear-gradient(135deg, #ff2f92, #b8006b);
    border: none;
    border-radius: 40px;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(255,60,150,0.7), 0 8px 20px rgba(0,0,0,0.4);
    transition: transform 0.35s ease, opacity 0.6s ease, box-shadow 0.35s ease;
    animation: pulseBtn 2.2s ease-in-out infinite;
  }}

  .click-btn:hover {{
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0 0 40px rgba(255,80,170,0.9);
  }}

  .click-btn.hidden {{
    opacity: 0;
    pointer-events: none;
    transform: translateY(20px);
  }}

  @keyframes pulseBtn {{
    0%, 100% {{ box-shadow: 0 0 25px rgba(255,60,150,0.7), 0 8px 20px rgba(0,0,0,0.4); }}
    50%      {{ box-shadow: 0 0 45px rgba(255,100,190,0.95), 0 8px 25px rgba(0,0,0,0.5); }}
  }}

  .message-card {{
    position: absolute;
    bottom: 8%;
    left: 50%;
    transform: translate(-50%, 20px);
    width: min(88vw, 560px);
    padding: 28px 34px;
    background: rgba(20,4,18,0.45);
    border: 1px solid rgba(255,180,220,0.3);
    border-radius: 18px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 40px rgba(255,90,180,0.25);
    opacity: 0;
    transition: opacity 1.4s ease, transform 1.4s ease;
    z-index: 10;
    text-align: center;
  }}

  .message-card.show {{
    opacity: 1;
    transform: translate(-50%, 0);
  }}

  .typed-message {{
    font-family: 'Great Vibes', cursive;
    font-size: 30px;
    line-height: 1.5;
    color: #ffe3f2;
    text-shadow: 0 0 16px rgba(255,140,200,0.8), 0 0 30px rgba(255,100,180,0.5);
    white-space: pre-wrap;
  }}

  .cursor {{
    display: inline-block;
    width: 2px;
    background: #ffd7ec;
    margin-left: 2px;
    animation: blink 0.8s step-start infinite;
  }}

  @keyframes blink {{
    50% {{ opacity: 0; }}
  }}
</style>
</head>
<body>

<div class="scene">
  <div class="bg-gradient" id="bgGradient"></div>
  <div class="particles" id="particles"></div>

  <div class="stage">
    <div class="labels">
      <h1 class="gift-by">Gift By {sender_html}</h1>
      <h2 class="for-you">For {receiver_html}</h2>
    </div>

    <div class="gift-wrap">
      <div class="box-container" id="boxContainer">
        <div class="box-body"></div>
        <div class="ribbon-vertical"></div>
        <div class="ribbon-horizontal"></div>

        <div class="bow">
          <div class="bow-half left"></div>
          <div class="bow-half right"></div>
          <div class="bow-knot"></div>
        </div>

        <div class="box-lid" id="boxLid"></div>
      </div>

      <div class="bouquet" id="bouquet">
        <div class="stem" style="left:50%; transform: translateX(-50%) rotate(0deg);"></div>
        <div class="stem" style="left:38%; transform: translateX(-50%) rotate(-18deg); height:75px;"></div>
        <div class="stem" style="left:62%; transform: translateX(-50%) rotate(18deg); height:75px;"></div>
        <div class="leaf" style="left:34%; top:40px; transform: rotate(-30deg);"></div>
        <div class="leaf" style="left:60%; top:50px; transform: rotate(30deg);"></div>

        <div class="flower" style="left:calc(50% - 23px); top:-10px;">
          <div class="petal" style="transform: rotate(0deg);"></div>
          <div class="petal" style="transform: rotate(60deg);"></div>
          <div class="petal" style="transform: rotate(120deg);"></div>
          <div class="petal" style="transform: rotate(180deg);"></div>
          <div class="petal" style="transform: rotate(240deg);"></div>
          <div class="petal" style="transform: rotate(300deg);"></div>
          <div class="flower-center"></div>
        </div>

        <div class="flower" style="left:calc(38% - 23px); top:15px; transform: scale(0.85) rotate(-10deg);">
          <div class="petal" style="transform: rotate(0deg);"></div>
          <div class="petal" style="transform: rotate(60deg);"></div>
          <div class="petal" style="transform: rotate(120deg);"></div>
          <div class="petal" style="transform: rotate(180deg);"></div>
          <div class="petal" style="transform: rotate(240deg);"></div>
          <div class="petal" style="transform: rotate(300deg);"></div>
          <div class="flower-center"></div>
        </div>

        <div class="flower" style="left:calc(62% - 23px); top:20px; transform: scale(0.8) rotate(12deg);">
          <div class="petal" style="transform: rotate(0deg);"></div>
          <div class="petal" style="transform: rotate(60deg);"></div>
          <div class="petal" style="transform: rotate(120deg);"></div>
          <div class="petal" style="transform: rotate(180deg);"></div>
          <div class="petal" style="transform: rotate(240deg);"></div>
          <div class="petal" style="transform: rotate(300deg);"></div>
          <div class="flower-center"></div>
        </div>
      </div>
    </div>

    <button class="click-btn" id="clickBtn">Click Here ❤️</button>

    <div class="message-card" id="messageCard">
      <p id="typedMessage" class="typed-message"></p>
    </div>
  </div>
</div>

<script>
  const clickBtn = document.getElementById('clickBtn');
  const boxContainer = document.getElementById('boxContainer');
  const boxLid = document.getElementById('boxLid');
  const bouquet = document.getElementById('bouquet');
  const bgGradient = document.getElementById('bgGradient');
  const messageCard = document.getElementById('messageCard');
  const typedMessage = document.getElementById('typedMessage');
  const particlesEl = document.getElementById('particles');

  const fullMessage = {message_js};

  function spawnParticle(type) {{
    const el = document.createElement('div');
    el.className = 'particle';
    el.style.left = Math.random() * 100 + 'vw';
    el.style.setProperty('--drift', (Math.random() * 160 - 80) + 'px');
    const duration = 6 + Math.random() * 6;
    el.style.animationDuration = duration + 's';
    el.style.fontSize = (14 + Math.random() * 16) + 'px';
    el.style.opacity = '0.9';
    if (type === 'petal') {{
      el.textContent = '🌸';
    }} else if (type === 'heart') {{
      el.textContent = '❤️';
    }} else {{
      el.textContent = '✨';
    }}
    particlesEl.appendChild(el);
    setTimeout(() => el.remove(), duration * 1000 + 200);
  }}

  setInterval(() => spawnParticle('petal'), 550);
  setInterval(() => spawnParticle('heart'), 900);
  setInterval(() => spawnParticle('sparkle'), 400);

  function typeMessage(text, el, speed) {{
    el.innerHTML = '';
    const cursor = document.createElement('span');
    cursor.className = 'cursor';
    cursor.textContent = ' ';
    let i = 0;
    function step() {{
      if (i <= text.length) {{
        el.textContent = text.slice(0, i);
        el.appendChild(cursor);
        i++;
        setTimeout(step, speed);
      }} else {{
        cursor.remove();
      }}
    }}
    step();
  }}

  clickBtn.addEventListener('click', () => {{
    clickBtn.classList.add('hidden');
    boxContainer.classList.add('untie');

    setTimeout(() => {{
      boxLid.classList.add('open');
    }}, 700);

    setTimeout(() => {{
      bouquet.classList.add('rise');
    }}, 1500);

    setTimeout(() => {{
      bouquet.classList.add('center');
      bgGradient.classList.add('blurred');
      boxContainer.classList.add('shrink');
    }}, 2600);

    setTimeout(() => {{
      messageCard.classList.add('show');
      typeMessage(fullMessage, typedMessage, 45);
    }}, 3800);

    setTimeout(() => {{
      bouquet.classList.add('floating');
    }}, 4300);
  }});
</script>

</body>
</html>
''')
file.close()

print("gift.html has been created successfully! Open it in your browser to view the gift.")