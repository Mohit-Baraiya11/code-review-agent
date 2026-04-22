<img width="113" height="150" alt="code_review_agent_architecture" src="https://github.com/user-attachments/assets/d0f2b928-1be9-4ef9-a536-2a07d115b4f7" /># CodeScan — AI Code Review Agent

A multi-agent AI system that analyzes any GitHub repository and produces a structured code review report covering bugs, security vulnerabilities, and code quality — all analyzed in parallel.

<svg width="100%" viewBox="0 0 680 900" role="img" style="" xmlns="http://www.w3.org/2000/svg">
  <title style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">Code Review Agent Architecture</title>
  <desc style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">LangGraph-based multi-agent architecture for automated code review</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  <mask id="imagine-text-gaps-rkp0sz" maskUnits="userSpaceOnUse"><rect x="0" y="0" width="680" height="900" fill="white"/><rect x="301.78125" y="31.60000228881836" width="76.4375" height="20.80000114440918" fill="black" rx="2"/><rect x="259.9750061035156" y="50.79999923706055" width="160.0500030517578" height="18.40000057220459" fill="black" rx="2"/><rect x="268.1000061035156" y="119.5999984741211" width="143.8000030517578" height="20.80000114440918" fill="black" rx="2"/><rect x="235.3874969482422" y="138.8000030517578" width="209.22500610351562" height="18.40000057220459" fill="black" rx="2"/><rect x="246.99375915527344" y="207.60000610351562" width="186.0124969482422" height="20.80000114440918" fill="black" rx="2"/><rect x="237.47500610351562" y="226.8000030517578" width="205.0500030517578" height="18.40000057220459" fill="black" rx="2"/><rect x="289.0062561035156" y="260.8000183105469" width="101.98750305175781" height="18.40000057220459" fill="black" rx="2"/><rect x="314.0187683105469" y="291.6000061035156" width="51.962501525878906" height="20.80000114440918" fill="black" rx="2"/><rect x="256.4437561035156" y="308.8000183105469" width="167.1125030517578" height="18.40000057220459" fill="black" rx="2"/><rect x="296.4624938964844" y="364.8000183105469" width="87.07500457763672" height="18.40000057220459" fill="black" rx="2"/><rect x="61.712501525878906" y="395.6000061035156" width="76.57500457763672" height="20.80000114440918" fill="black" rx="2"/><rect x="25.200000762939453" y="414.8000183105469" width="149.60000610351562" height="18.40000057220459" fill="black" rx="2"/><rect x="63.73750305175781" y="428.8000183105469" width="72.5250015258789" height="18.40000057220459" fill="black" rx="2"/><rect x="278.88751220703125" y="395.6000061035156" width="122.2249984741211" height="20.80000114440918" fill="black" rx="2"/><rect x="282.65625" y="414.8000183105469" width="114.6875" height="18.40000057220459" fill="black" rx="2"/><rect x="296.8062438964844" y="428.8000183105469" width="86.38750457763672" height="18.40000057220459" fill="black" rx="2"/><rect x="534.4874877929688" y="395.6000061035156" width="91.0250015258789" height="20.80000114440918" fill="black" rx="2"/><rect x="518.9000244140625" y="414.8000183105469" width="122.20000457763672" height="18.40000057220459" fill="black" rx="2"/><rect x="511.4937744140625" y="428.8000183105469" width="137.0124969482422" height="18.40000057220459" fill="black" rx="2"/><rect x="272.2124938964844" y="529.6000366210938" width="135.57500457763672" height="20.80000114440918" fill="black" rx="2"/><rect x="245.4375" y="548.7999877929688" width="189.125" height="18.40000057220459" fill="black" rx="2"/><rect x="419.0062561035156" y="574.7999877929688" width="101.98750305175781" height="18.40000057220459" fill="black" rx="2"/><rect x="265.40625" y="609.6000366210938" width="149.1875" height="20.80000114440918" fill="black" rx="2"/><rect x="244.5625" y="626.7999877929688" width="190.875" height="18.40000057220459" fill="black" rx="2"/><rect x="171.28750610351562" y="658" width="27.42500114440918" height="18.40000057220459" fill="black" rx="2"/><rect x="488.95001220703125" y="658" width="22.100000381469727" height="18.40000057220459" fill="black" rx="2"/><rect x="94.73125457763672" y="703.6000366210938" width="110.5374984741211" height="20.80000114440918" fill="black" rx="2"/><rect x="66.0250015258789" y="722.7999877929688" width="167.9499969482422" height="18.40000057220459" fill="black" rx="2"/><rect x="470.95001220703125" y="703.6000366210938" width="98.0999984741211" height="20.80000114440918" fill="black" rx="2"/><rect x="458.13751220703125" y="722.7999877929688" width="123.7249984741211" height="18.40000057220459" fill="black" rx="2"/><rect x="252.88751220703125" y="807.6000366210938" width="174.22500610351562" height="20.80000114440918" fill="black" rx="2"/><rect x="246.0500030517578" y="826.7999877929688" width="187.90000915527344" height="18.40000057220459" fill="black" rx="2"/><rect x="283.6437683105469" y="868.7999877929688" width="112.7125015258789" height="18.40000057220459" fill="black" rx="2"/><rect x="34" y="808.7999877929688" width="99.3499984741211" height="18.40000057220459" fill="black" rx="2"/><rect x="34" y="830.7999877929688" width="84.6875" height="18.40000057220459" fill="black" rx="2"/><rect x="34" y="852.7999877929688" width="109.6500015258789" height="18.40000057220459" fill="black" rx="2"/></mask></defs>

  <!-- INPUT -->
  <g onclick="sendPrompt('What inputs does the Code Review Agent accept?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="240" y="20" width="200" height="52" rx="8" stroke-width="0.5" style="fill:rgb(68, 68, 65);stroke:rgb(180, 178, 169);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="42" text-anchor="middle" dominant-baseline="central" style="fill:rgb(211, 209, 199);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">User input</text>
    <text x="340" y="60" text-anchor="middle" dominant-baseline="central" style="fill:rgb(180, 178, 169);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">GitHub URL + review focus</text>
  </g>

  <!-- Arrow -->
  <line x1="340" y1="72" x2="340" y2="106" marker-end="url(#arrow)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- NODE 1: Repo Fetcher -->
  <g onclick="sendPrompt('What does the Repo Fetcher node do in the Code Review Agent?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="200" y="108" width="280" height="52" rx="8" stroke-width="0.5" style="fill:rgb(60, 52, 137);stroke:rgb(175, 169, 236);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="130" text-anchor="middle" dominant-baseline="central" style="fill:rgb(206, 203, 246);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">1. Repo fetcher node</text>
    <text x="340" y="148" text-anchor="middle" dominant-baseline="central" style="fill:rgb(175, 169, 236);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">GitHub API → fetch files + structure</text>
  </g>

  <!-- Arrow -->
  <line x1="340" y1="160" x2="340" y2="194" marker-end="url(#arrow)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- NODE 2: Language Detector -->
  <g onclick="sendPrompt('How does the language detector node work?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="200" y="196" width="280" height="52" rx="8" stroke-width="0.5" style="fill:rgb(60, 52, 137);stroke:rgb(175, 169, 236);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="218" text-anchor="middle" dominant-baseline="central" style="fill:rgb(206, 203, 246);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">2. Language detector node</text>
    <text x="340" y="236" text-anchor="middle" dominant-baseline="central" style="fill:rgb(175, 169, 236);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Detect stack → set review strategy</text>
  </g>

  <!-- Conditional label -->
  <text x="340" y="270" text-anchor="middle" dominant-baseline="central" style="fill:var(--color-text-secondary);fill:rgb(194, 192, 182);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">conditional edge</text>
  <line x1="340" y1="248" x2="340" y2="282" marker-end="url(#arrow)" stroke-dasharray="5 4" mask="url(#imagine-text-gaps-rkp0sz)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-dasharray:5px, 4px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- CONDITIONAL ROUTER BOX -->
  <g onclick="sendPrompt('What is the conditional router doing in the Code Review Agent?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="215" y="284" width="250" height="44" rx="8" stroke-width="0.5" style="fill:rgb(99, 56, 6);stroke:rgb(239, 159, 39);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="302" text-anchor="middle" dominant-baseline="central" style="fill:rgb(250, 199, 117);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Router</text>
    <text x="340" y="318" text-anchor="middle" dominant-baseline="central" style="fill:rgb(239, 159, 39);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Route by language detected</text>
  </g>

  <!-- Fan out arrows to 3 parallel nodes -->
  <line x1="260" y1="328" x2="90" y2="378" marker-end="url(#arrow)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <line x1="340" y1="328" x2="340" y2="378" marker-end="url(#arrow)" mask="url(#imagine-text-gaps-rkp0sz)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <line x1="420" y1="328" x2="590" y2="378" marker-end="url(#arrow)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- Parallel label -->
  <text x="340" y="374" text-anchor="middle" dominant-baseline="central" style="fill:var(--color-text-secondary);fill:rgb(194, 192, 182);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">parallel nodes</text>

  <!-- PARALLEL NODES ROW -->
  <!-- Node A: Bug Finder -->
  <g onclick="sendPrompt('What does the Bug Finder agent analyze?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="20" y="382" width="160" height="64" rx="8" stroke-width="0.5" style="fill:rgb(8, 80, 65);stroke:rgb(93, 202, 165);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="100" y="406" text-anchor="middle" dominant-baseline="central" style="fill:rgb(159, 225, 203);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Bug finder</text>
    <text x="100" y="424" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Logic errors, null checks,</text>
    <text x="100" y="438" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">edge cases</text>
  </g>

  <!-- Node B: Security Analyzer -->
  <g onclick="sendPrompt('What does the Security Analyzer agent look for?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="260" y="382" width="160" height="64" rx="8" stroke-width="0.5" style="fill:rgb(8, 80, 65);stroke:rgb(93, 202, 165);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="406" text-anchor="middle" dominant-baseline="central" style="fill:rgb(159, 225, 203);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Security analyzer</text>
    <text x="340" y="424" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Injections, secrets,</text>
    <text x="340" y="438" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">vulnerabilities</text>
  </g>

  <!-- Node C: Code Quality -->
  <g onclick="sendPrompt('What does the Code Quality agent check?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="500" y="382" width="160" height="64" rx="8" stroke-width="0.5" style="fill:rgb(8, 80, 65);stroke:rgb(93, 202, 165);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="580" y="406" text-anchor="middle" dominant-baseline="central" style="fill:rgb(159, 225, 203);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Code quality</text>
    <text x="580" y="424" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Complexity, naming,</text>
    <text x="580" y="438" text-anchor="middle" dominant-baseline="central" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">dead code, duplication</text>
  </g>

  <!-- Merge arrows back -->
  <line x1="100" y1="446" x2="280" y2="516" marker-end="url(#arrow)" mask="url(#imagine-text-gaps-rkp0sz)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <line x1="340" y1="446" x2="340" y2="516" marker-end="url(#arrow)" mask="url(#imagine-text-gaps-rkp0sz)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <line x1="580" y1="446" x2="400" y2="516" marker-end="url(#arrow)" mask="url(#imagine-text-gaps-rkp0sz)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- NODE 4: Aggregator -->
  <g onclick="sendPrompt('How does the Aggregator node combine results from parallel agents?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="200" y="518" width="280" height="52" rx="8" stroke-width="0.5" style="fill:rgb(60, 52, 137);stroke:rgb(175, 169, 236);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="540" text-anchor="middle" dominant-baseline="central" style="fill:rgb(206, 203, 246);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">3. Aggregator node</text>
    <text x="340" y="558" text-anchor="middle" dominant-baseline="central" style="fill:rgb(175, 169, 236);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Merge findings, rank by severity</text>
  </g>

  <!-- Conditional edge again -->
  <text x="470" y="584" text-anchor="middle" dominant-baseline="central" style="fill:var(--color-text-secondary);fill:rgb(194, 192, 182);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">conditional edge</text>
  <line x1="340" y1="570" x2="340" y2="600" marker-end="url(#arrow)" stroke-dasharray="5 4" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-dasharray:5px, 4px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- CONDITIONAL: any critical issues? -->
  <g onclick="sendPrompt('What happens when critical issues are found in code review?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="215" y="602" width="250" height="44" rx="8" stroke-width="0.5" style="fill:rgb(99, 56, 6);stroke:rgb(239, 159, 39);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="620" text-anchor="middle" dominant-baseline="central" style="fill:rgb(250, 199, 117);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Critical issues found?</text>
    <text x="340" y="636" text-anchor="middle" dominant-baseline="central" style="fill:rgb(239, 159, 39);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Branch: deep dive vs summarize</text>
  </g>

  <!-- YES branch: Deep Dive -->
  <line x1="248" y1="646" x2="150" y2="690" marker-end="url(#arrow)" mask="url(#imagine-text-gaps-rkp0sz)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="185" y="672" text-anchor="middle" style="fill:var(--color-text-secondary);fill:rgb(194, 192, 182);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">yes</text>

  <!-- NO branch: skip to report -->
  <line x1="432" y1="646" x2="530" y2="690" marker-end="url(#arrow)" mask="url(#imagine-text-gaps-rkp0sz)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="500" y="672" text-anchor="middle" style="fill:var(--color-text-secondary);fill:rgb(194, 192, 182);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:auto">no</text>

  <!-- Deep Dive node -->
  <g onclick="sendPrompt('What does the deep dive node do for critical issues?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="60" y="692" width="180" height="52" rx="8" stroke-width="0.5" style="fill:rgb(113, 43, 19);stroke:rgb(240, 153, 123);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="150" y="714" text-anchor="middle" dominant-baseline="central" style="fill:rgb(245, 196, 179);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Deep dive node</text>
    <text x="150" y="732" text-anchor="middle" dominant-baseline="central" style="fill:rgb(240, 153, 123);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Tavily search for fix patterns</text>
  </g>

  <!-- Skip node (ghost) -->
  <g onclick="sendPrompt('What happens when no critical issues are found?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="440" y="692" width="160" height="52" rx="8" stroke-width="0.5" style="fill:rgb(68, 68, 65);stroke:rgb(180, 178, 169);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="520" y="714" text-anchor="middle" dominant-baseline="central" style="fill:rgb(211, 209, 199);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">Skip research</text>
    <text x="520" y="732" text-anchor="middle" dominant-baseline="central" style="fill:rgb(180, 178, 169);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Go straight to report</text>
  </g>

  <!-- Both merge into report -->
  <line x1="150" y1="744" x2="280" y2="794" marker-end="url(#arrow)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <line x1="520" y1="744" x2="400" y2="794" marker-end="url(#arrow)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- NODE 5: Report Generator -->
  <g onclick="sendPrompt('What does the final Report Generator node output?')" style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="200" y="796" width="280" height="52" rx="8" stroke-width="0.5" style="fill:rgb(60, 52, 137);stroke:rgb(175, 169, 236);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="818" text-anchor="middle" dominant-baseline="central" style="fill:rgb(206, 203, 246);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:14px;font-weight:500;text-anchor:middle;dominant-baseline:central">4. Report generator node</text>
    <text x="340" y="836" text-anchor="middle" dominant-baseline="central" style="fill:rgb(175, 169, 236);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Structured MD report + fix hints</text>
  </g>

  <!-- Arrow to output -->
  <line x1="340" y1="848" x2="340" y2="866" marker-end="url(#arrow)" style="fill:none;stroke:rgb(156, 154, 146);color:rgb(255, 255, 255);stroke-width:1.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>

  <!-- OUTPUT -->
  <g style="fill:rgb(0, 0, 0);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto">
    <rect x="240" y="868" width="200" height="20" rx="6" stroke-width="0.5" style="fill:rgb(68, 68, 65);stroke:rgb(180, 178, 169);color:rgb(255, 255, 255);stroke-width:0.5px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
    <text x="340" y="878" text-anchor="middle" dominant-baseline="central" style="fill:rgb(180, 178, 169);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:middle;dominant-baseline:central">Final review report</text>
  </g>

  <!-- Legend -->
  <rect x="20" y="808" width="12" height="12" rx="2" fill="#AFA9EC" style="fill:rgb(175, 169, 236);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="38" y="818" dominant-baseline="central" style="fill:rgb(194, 192, 182);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:start;dominant-baseline:central">Sequential node</text>
  <rect x="20" y="830" width="12" height="12" rx="2" fill="#5DCAA5" style="fill:rgb(93, 202, 165);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="38" y="840" dominant-baseline="central" style="fill:rgb(194, 192, 182);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:start;dominant-baseline:central">Parallel agent</text>
  <rect x="20" y="852" width="12" height="12" rx="2" fill="#EF9F27" style="fill:rgb(239, 159, 39);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:16px;font-weight:400;text-anchor:start;dominant-baseline:auto"/>
  <text x="38" y="862" dominant-baseline="central" style="fill:rgb(194, 192, 182);stroke:none;color:rgb(255, 255, 255);stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;opacity:1;font-family:&quot;Anthropic Sans&quot;, -apple-system, &quot;system-ui&quot;, &quot;Segoe UI&quot;, sans-serif;font-size:12px;font-weight:400;text-anchor:start;dominant-baseline:central">Conditional router</text>
</svg>oading code_review_agent_architecture.svg…]()


## Stack

| Tool | Purpose |
|------|---------|
| LangGraph | Multi-agent graph orchestration |
| Groq (LLaMA 3.3) | AI inference for code analysis |
| GitHub API | Fetch repository files |
| Tavily | Web research for critical issue fixes |
| FastAPI | REST API backend |
| Python 3.11+ | Runtime |

---

## Architecture

The system uses all 3 LangGraph patterns:

- **Sequential** — Repo fetcher → Language detector → Aggregator → Report generator
- **Parallel** — Bug finder, Security analyzer, Code quality run simultaneously using `Send()` API
- **Conditional** — Router 1 routes by language, Router 2 routes by severity (critical issues → deep dive)

### Graph Flow

```
Repo Fetcher → Language Detector → [Router 1]
                                        ↓
                    ┌───────────────────┼───────────────────┐
                    ↓                   ↓                   ↓
              Bug Finder       Security Analyzer      Code Quality
                    └───────────────────┼───────────────────┘
                                        ↓
                                   Aggregator → [Router 2]
                                                    ↓
                                        critical? → Deep Dive (Tavily)
                                             ↓              ↓
                                        Report Generator ←──┘
                                                ↓
                                              END
```

---

## Project Structure

```
code-review-agent/
├── .env
├── main.py                  # FastAPI entry point
├── index.html               # Frontend UI
├── graph/
│   ├── state.py             # GraphState TypedDict
│   ├── builder.py           # LangGraph graph definition
│   └── nodes/
│       ├── repo_fetcher.py
│       ├── language_detector.py
│       ├── bug_finder.py
│       ├── security_analyzer.py
│       ├── code_quality.py
│       ├── aggregator.py
│       ├── deep_dive.py
│       └── report_generator.py
├── utils/
│   └── github_client.py
└── prompts/
    ├── bug_finder.txt
    ├── security.txt
    └── quality.txt
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/code-review-agent
cd code-review-agent
```

### 2. Create virtual environment

```bash
uv venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
uv add langgraph langchain-groq langchain-core tavily-python PyGithub python-dotenv fastapi uvicorn
```

### 4. Configure environment variables

Create a `.env` file in the root:

```env
GROQ_API_KEY=your_groq_key_here
GITHUB_TOKEN=your_github_token_here
TAVILY_API_KEY=your_tavily_key_here
```

### 5. Get API Keys

| Service | URL | Cost |
|---------|-----|------|
| Groq | console.groq.com | Free |
| GitHub Token | github.com/settings/tokens | Free |
| Tavily | tavily.com | Free (1000/month) |

---

## Running Locally

```bash
PYTHONPATH=. uv run uvicorn main:app --reload
```

Then open `index.html` in your browser and paste any GitHub repo URL.

---

## API

### `POST /review`

```json
{
  "repo_url": "https://github.com/username/repository",
  "focus": "all"
}
```

**Focus options:** `all` | `bugs` | `security` | `quality`

**Response:**

```json
{
  "repo_url": "...",
  "detected_language": "Python",
  "critical_found": false,
  "total_files": 12,
  "final_report": "# Code Review Report..."
}
```

### `GET /health`

```json
{ "status": "ok" }
```

---

## Deployment (Render)

1. Push to GitHub
2. Create a new **Web Service** on [render.com](https://render.com)
3. Set the following:

| Field | Value |
|-------|-------|
| Build Command | `pip install uv && uv sync` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

4. Add environment variables in Render dashboard:
   - `GROQ_API_KEY`
   - `GITHUB_TOKEN`
   - `TAVILY_API_KEY`
   - `PYTHONPATH` = `.`

---

## Key Concepts

| Term | Description |
|------|-------------|
| `GraphState` | Shared TypedDict all nodes read from and write to |
| `Node` | Plain Python function: takes state, returns updated fields |
| `Edge` | Connection between nodes — fixed or conditional |
| `Send()` | LangGraph's fan-out API for parallel execution |
| `Annotated[list, operator.add]` | Merges parallel agent results instead of overwriting |

---

