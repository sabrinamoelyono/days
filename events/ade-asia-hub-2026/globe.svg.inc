<svg width="620" height="620" viewBox="-320 -320 640 640" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="dots" width="11" height="11" patternUnits="userSpaceOnUse"><circle cx="5.5" cy="5.5" r="1.7" fill="#FEFB16"/></pattern>
    <radialGradient id="shade" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset=".7" stop-color="#fff" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
    <mask id="m"><circle r="300" fill="url(#shade)"/></mask>
    <filter id="glow" x="-1" y="-1" width="3" height="3"><feGaussianBlur stdDeviation="6"/></filter>
  </defs>
  <!-- land: loose dot masses for East & Southeast Asia -->
  <g mask="url(#m)" opacity=".75">
    <path fill="url(#dots)" d="M-40,-260 C40,-280 120,-250 150,-200 C170,-160 120,-150 110,-110 C100,-70 60,-60 40,-20 C30,10 -10,0 -30,30 C-60,60 -110,40 -130,0 C-160,-50 -150,-120 -120,-180 C-100,-220 -80,-250 -40,-260Z"/>
    <path fill="url(#dots)" d="M150,-190 C175,-200 195,-170 185,-140 C175,-110 150,-115 145,-140 C140,-160 140,-182 150,-190Z"/>
    <path fill="url(#dots)" d="M-60,40 C-30,50 -20,90 -40,120 C-55,140 -75,120 -75,95 C-75,70 -80,45 -60,40Z"/>
    <path fill="url(#dots)" d="M-120,150 C-60,140 0,150 60,165 C90,172 95,190 60,192 C0,195 -60,185 -120,175 C-145,170 -140,152 -120,150Z"/>
    <path fill="url(#dots)" d="M10,90 C50,80 80,100 70,130 C60,150 20,145 5,125 C-5,110 -5,95 10,90Z"/>
    <path fill="url(#dots)" d="M120,60 C160,50 200,70 190,110 C180,140 140,135 125,110 C115,90 105,65 120,60Z"/>
  </g>
  <circle r="300" fill="none" stroke="#FEFB16" stroke-opacity=".45" stroke-width="1.5"/>
  <ellipse rx="300" ry="96" fill="none" stroke="#FEFB16" stroke-opacity=".14"/>
  <ellipse rx="150" ry="300" fill="none" stroke="#FEFB16" stroke-opacity=".14"/>
  <!-- route arcs -->
  <path d="M-62,-10 C-20,-170 80,-205 170,-180" fill="none" stroke="#FEFB16" stroke-width="2.2"/>
  <path d="M-62,-10 C0,40 70,120 135,178" fill="none" stroke="#FEFB16" stroke-width="2.2"/>
  <g fill="#FEFB16">
    <circle cx="170" cy="-180" r="16" filter="url(#glow)"/><circle cx="170" cy="-180" r="8"/>
    <circle cx="-62" cy="-10" r="16" filter="url(#glow)"/><circle cx="-62" cy="-10" r="8"/>
    <circle cx="135" cy="178" r="16" filter="url(#glow)"/><circle cx="135" cy="178" r="8"/>
  </g>
  <g font-family="Archivo" font-weight="800" font-size="30" letter-spacing="3.6" fill="#F2F0EA" style="font-stretch:112%">
    <text x="148" y="-208" text-anchor="end">SEOUL</text>
    <text x="-62" y="38" text-anchor="middle">BANGKOK</text>
    <text x="115" y="230" text-anchor="end">JAKARTA</text>
  </g>
</svg>
