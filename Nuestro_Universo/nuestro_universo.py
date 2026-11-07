<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nuestro Universo</title>
<style>
:root{
  --noche:#0b0a22; --violeta:#2a1a55; --ciruela:#4a1d5c;
  --rosa:#ffb9e9; --lila:#e6d6ff; --oro:#ffe3a8; --mar:#7fd6e6; --fuego:#ff9c7a;
  --texto:#f3eaff;
  --serif:"Palatino Linotype","Book Antiqua",Palatino,Georgia,serif;
}
*{box-sizing:border-box;margin:0}
html,body{height:100%}
body{
  background:radial-gradient(ellipse at 20% 0%,#2f2063 0%,transparent 55%),
             radial-gradient(ellipse at 90% 100%,#561f5e 0%,transparent 50%),
             linear-gradient(160deg,#080a1f,#120f2e 60%,#09091b);
  color:var(--texto);font-family:var(--serif);line-height:1.8;
  overflow-x:hidden;min-height:100%;
}
#estrellas{position:fixed;inset:0;width:100%;height:100%;z-index:0}
.signos{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none;opacity:.55}
main{position:relative;z-index:1;max-width:680px;margin:0 auto;padding:28px 20px 60px;
  padding-top:max(28px,env(safe-area-inset-top));min-height:100vh;display:flex;flex-direction:column;justify-content:center}
.vista{display:none;animation:entra .7s ease}
.vista.activa{display:block}
@keyframes entra{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.vista{animation:none}}

/* PORTADA: libro cerrado */
.libro{
  margin:0 auto;width:min(86vw,340px);aspect-ratio:3/4.2;cursor:pointer;border:none;color:inherit;
  background:linear-gradient(145deg,#3a1f6e,#6b2670 60%,#3a1a5e);
  border-radius:6px 18px 18px 6px;position:relative;text-align:center;
  box-shadow:-10px 10px 40px rgba(0,0,0,.55),0 0 50px rgba(190,100,255,.25),inset 6px 0 0 rgba(0,0,0,.35);
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:30px;
  font-family:var(--serif);transition:transform .5s,box-shadow .5s;
}
.libro::before{content:"";position:absolute;inset:12px 12px 12px 22px;border:1px solid rgba(255,227,168,.5);border-radius:3px 12px 12px 3px}
.libro:hover,.libro:focus-visible{transform:perspective(900px) rotateY(-14deg) scale(1.03);outline:none}
.libro .sig{font-size:2rem;letter-spacing:.4em;color:var(--oro)}
.libro h1{font-size:clamp(1.9rem,8vw,2.6rem);font-weight:400;color:var(--oro);line-height:1.2;text-shadow:0 0 18px rgba(255,200,120,.5)}
.libro small{color:var(--lila);font-size:.95rem;font-style:italic}
.pista{text-align:center;margin-top:28px;color:var(--lila);font-style:italic;animation:late 2.6s infinite}
@keyframes late{50%{opacity:.4}}
.dedic{text-align:center;margin-top:12px;color:#cdb9ee;font-size:.9rem}

/* ÍNDICE */
h2.t{font-weight:400;font-size:clamp(1.8rem,6vw,2.4rem);text-align:center;color:var(--rosa);text-shadow:0 0 18px rgba(215,91,255,.5);line-height:1.25}
.sub{text-align:center;color:var(--lila);font-style:italic;margin:6px 0 26px}
.lista{display:grid;gap:12px}
.cap-btn{
  display:flex;align-items:center;gap:16px;text-align:left;width:100%;cursor:pointer;
  background:linear-gradient(135deg,rgba(100,65,150,.3),rgba(225,100,180,.12));
  border:1px solid rgba(231,174,255,.35);border-radius:14px;padding:14px 18px;color:var(--texto);font-family:var(--serif);font-size:1.02rem;
  transition:border-color .25s,background .25s;
}
.cap-btn:hover,.cap-btn:focus-visible{border-color:var(--rosa);background:rgba(255,185,233,.14);outline:none}
.cap-btn .ico{font-size:1.7rem;width:2.2rem;text-align:center}
.cap-btn b{display:block;font-weight:400;color:var(--rosa);font-size:1.12rem}
.cap-btn span{color:#cdb9ee;font-size:.88rem;font-style:italic}

/* CAPÍTULO: página de libro */
.pagina{
  background:linear-gradient(160deg,rgba(60,40,110,.45),rgba(110,40,110,.25));
  border:1px solid rgba(231,174,255,.3);border-radius:20px;padding:30px 24px;margin:18px 0;
  box-shadow:0 0 30px rgba(180,90,255,.12);
}
.pagina p{margin-bottom:1em;text-align:center}
.pagina p.izq{text-align:left}
.frase{text-align:center;color:var(--oro);font-size:1.3rem;line-height:1.6;margin:22px 0;font-style:italic}
.emoji{text-align:center;font-size:3rem}
.num{display:grid;gap:12px;margin:18px 0}
.dato{text-align:center;border:1px solid rgba(255,190,245,.3);border-radius:16px;padding:16px;background:rgba(130,85,180,.18)}
.dato b{display:block;font-size:2.4rem;font-weight:400;color:var(--rosa);text-shadow:0 0 14px #d45bff;line-height:1.2}
.dato span{color:var(--lila);font-size:.9rem}
.dos{display:grid;grid-template-columns:1fr 1fr;gap:12px}

.nav{display:flex;gap:10px;justify-content:space-between;margin-top:22px}
.btn{
  cursor:pointer;border:1px solid #e8a9ff;background:linear-gradient(90deg,#6738a5,#bd4c9e);color:#fff;
  border-radius:30px;padding:.7rem 1.3rem;font-family:var(--serif);font-size:1rem;transition:box-shadow .3s,background .3s;
}
.btn:hover,.btn:focus-visible{box-shadow:0 0 20px rgba(228,120,255,.5);background:linear-gradient(90deg,#9855d5,#ed72bc);outline:none}
.btn.suave{background:transparent}
.btn.centro{display:block;margin:20px auto 0}
.migas{text-align:center;color:#cdb9ee;font-size:.85rem;margin-bottom:6px}

/* FOTOS */
.fotos{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:10px;margin:16px 0}
.foto{margin:0;cursor:pointer;border-radius:12px;overflow:hidden;border:1px solid rgba(231,174,255,.35);background:#1a1240;position:relative}
.foto img{display:block;width:100%;aspect-ratio:1;object-fit:cover;transition:transform .4s}
.foto:hover img{transform:scale(1.06)}
.foto figcaption{position:absolute;left:0;right:0;bottom:0;padding:18px 8px 6px;font-size:.78rem;line-height:1.3;text-align:center;background:linear-gradient(transparent,rgba(8,6,30,.9))}
.chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:12px 0}
.chip{cursor:pointer;border:1px solid rgba(231,174,255,.5);background:transparent;color:var(--lila);border-radius:20px;padding:.35rem 1rem;font-family:var(--serif);font-size:.92rem}
.chip.on{background:rgba(255,185,233,.2);color:var(--rosa);border-color:var(--rosa)}
.visor{position:fixed;inset:0;z-index:20;background:rgba(5,4,20,.94);display:none;flex-direction:column;align-items:center;justify-content:center;padding:20px}
.visor.on{display:flex}
.visor img{max-width:100%;max-height:70vh;border-radius:12px;box-shadow:0 0 40px rgba(200,100,255,.3)}
.visor p{margin:14px 0 8px;color:var(--rosa);font-style:italic;text-align:center}
.visor .nav{width:min(420px,100%)}
audio{width:100%;margin-top:10px}
.pie{text-align:center;color:#a995cc;font-size:.78rem;margin-top:34px}
:focus-visible{outline:2px solid var(--rosa);outline-offset:3px}
</style>
</head>
<body>

<canvas id="estrellas" aria-hidden="true"></canvas>

<!-- Constelaciones de Aries (arriba derecha) y Piscis (abajo izquierda) -->
<svg class="signos" viewBox="0 0 400 800" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <g fill="none" stroke="#ff9c7a" stroke-width="1" stroke-dasharray="3 5" opacity=".8">
    <polyline points="250,70 292,52 322,66 336,96"/>
  </g>
  <g fill="#ffd2bf">
    <circle cx="250" cy="70" r="3.2"/><circle cx="292" cy="52" r="3.6"/><circle cx="322" cy="66" r="2.6"/><circle cx="336" cy="96" r="2.2"/>
  </g>
  <text x="300" y="130" fill="#ffb59c" font-size="22" font-family="serif" text-anchor="middle">♈</text>
  <g fill="none" stroke="#7fd6e6" stroke-width="1" stroke-dasharray="3 5" opacity=".8">
    <polyline points="30,690 70,720 110,712 140,740 190,760 230,742 262,716 290,724"/>
    <polyline points="140,740 120,770 90,780"/>
  </g>
  <g fill="#cdf3fa">
    <circle cx="30" cy="690" r="2.4"/><circle cx="70" cy="720" r="3"/><circle cx="110" cy="712" r="2.2"/><circle cx="140" cy="740" r="3.4"/>
    <circle cx="190" cy="760" r="2.4"/><circle cx="230" cy="742" r="3"/><circle cx="262" cy="716" r="2.4"/><circle cx="290" cy="724" r="2.6"/>
    <circle cx="120" cy="770" r="2"/><circle cx="90" cy="780" r="2.4"/>
  </g>
  <text x="60" y="672" fill="#a8e6f2" font-size="22" font-family="serif" text-anchor="middle">♓</text>
</svg>

<main>

<!-- PORTADA -->
<section id="v-portada" class="vista activa">
  <button class="libro" id="abrir" aria-label="Abrir el libro: Nuestro Universo">
    <div class="sig">♈ ♓</div>
    <h1>Nuestro<br>Universo</h1>
    <small>una historia escrita por dos corazones</small>
    <div class="sig" style="font-size:1.1rem">✦</div>
  </button>
  <p class="pista">toca el libro para abrirlo</p>
  <p class="dedic">Para ti, mi amor · 09 · 11 · 2026</p>
</section>

<!-- ÍNDICE -->
<section id="v-indice" class="vista">
  <div class="emoji">🌌</div>
  <h2 class="t">Nuestro Universo</h2>
  <p class="sub">Elige el capítulo que quieras vivir</p>
  <div class="lista" id="lista"></div>
</section>

<!-- CAPÍTULO -->
<section id="v-cap" class="vista">
  <div class="migas" id="migas"></div>
  <h2 class="t" id="cap-titulo"></h2>
  <p class="sub" id="cap-sub"></p>
  <div id="cap-cuerpo"></div>
  <div class="nav">
    <button class="btn suave" id="prev">← Anterior</button>
    <button class="btn suave" id="idx">Índice</button>
    <button class="btn" id="next">Siguiente ✨</button>
  </div>
</section>

<div class="pie">Hecho con amor · para siempre en nuestro universo 🌌</div>
</main>

<!-- VISOR DE FOTOS -->
<div class="visor" id="visor" role="dialog" aria-label="Visor de fotos">
  <img id="visor-img" alt="">
  <p id="visor-nombre"></p>
  <div class="nav"><button class="btn suave" id="v-ant">←</button><button class="btn suave" id="v-cerrar">Cerrar</button><button class="btn suave" id="v-sig">→</button></div>
</div>

<script>
/* ==========================================================
   1. TUS DATOS  (edita solo esta sección)
   ========================================================== */
const ANIVERSARIO = new Date(2024, 10, 9);   // 09/11/2024 (el mes va de 0 a 11)
const CANCION = { titulo: "Quédate", artista: "Kany García", archivo: "cancion.mp3" }; // pon el mp3 en esta carpeta

/* FOTOS: pon tus imágenes en la carpeta "fotos" (junto a este HTML).
   nombre  = el título que ella verá
   cap     = en qué capítulos aparece (1, 2, 4 o 7)
   cat     = categoría para filtrar en el álbum del capítulo IV                    */
const FOTOS = [
  { src: "fotos/primer_dia.jpg",     nombre: "Nuestro primer día",    cap: [1],    cat: "Inicios" },
  { src: "fotos/primera_salida.jpg", nombre: "Nuestra primera salida", cap: [1, 4], cat: "Inicios" },
  { src: "fotos/nosotros_1.jpg",     nombre: "Tú y yo",               cap: [2],    cat: "Nosotros" },
  { src: "fotos/nosotros_2.jpg",     nombre: "Mi coincidencia favorita", cap: [2, 4], cat: "Nosotros" },
  { src: "fotos/viaje_1.jpg",        nombre: "Aquel viaje",           cap: [4],    cat: "Viajes" },
  { src: "fotos/viaje_2.jpg",        nombre: "Un lugar contigo",      cap: [4],    cat: "Viajes" },
  { src: "fotos/cumple_1.jpg",       nombre: "Celebrándote",          cap: [4],    cat: "Celebraciones" },
  { src: "fotos/favorita.jpg",       nombre: "Mi foto favorita",      cap: [7],    cat: "Nosotros" }
];
const FOTOS_VISIBLES_ALBUM = 6; // en el capítulo IV se muestran estas y el resto con "Ver todas"

/* ==========================================================
   2. CAPÍTULOS
   ========================================================== */
const hoy = new Date();
const dias = Math.floor((new Date(hoy.getFullYear(), hoy.getMonth(), hoy.getDate()) - ANIVERSARIO) / 864e5);
let anios = hoy.getFullYear() - ANIVERSARIO.getFullYear();
if (hoy.getMonth() < 10 || (hoy.getMonth() === 10 && hoy.getDate() < 9)) anios--;
let prox = new Date(hoy.getFullYear(), 10, 9);
const h0 = new Date(hoy.getFullYear(), hoy.getMonth(), hoy.getDate());
if (h0 > prox) prox = new Date(hoy.getFullYear() + 1, 10, 9);
const faltan = Math.round((prox - h0) / 864e5);
const esAntes = new Date(2026, 10, 9) > h0;

const CAPS = [
 { ico:"🌙", t:"Capítulo I", s:"El comienzo de todo", r:"Cuando llegaste a mi vida",
   html:()=>`
   <div class="emoji">🌙💫</div>
   <div class="pagina">
     <p>Antes de ti, mi mundo tenía millones de momentos,<br>pero ninguno se parecía a lo que comenzaría<br>cuando llegaste a mi vida.</p>
     <p>Sin darme cuenta, empezaste a convertirte<br>en una de mis personas favoritas.</p>
     <p>Y así comenzó nuestra historia…<br>una historia que hoy sigue siendo mi lugar favorito.</p>
   </div>
   ${galeria(1)}
   <div class="frase">09 de noviembre de 2024<br>El día en que comenzó nuestro para siempre.</div>`},

 { ico:"♈♓", t:"Capítulo II", s:"Tú y yo", r:"Un Aries y una Piscis",
   html:()=>`
   ${galeria(2)}
   <div class="pagina">
     <p>Mi amor, si pudiera elegir nuevamente<br>entre todos los caminos posibles,<br>volvería a elegir el que me lleva hasta ti.</p>
     <p>Tú, mi Piscis, eres el mar: profunda, tierna, llena de sueños.<br>Yo, tu Aries, soy la chispa que no sabe quedarse quieta.<br>Y aun así, junto a ti, el fuego aprende a descansar.</p>
     <p>No somos una historia perfecta,<br>pero sí una historia que quiero seguir construyendo contigo.</p>
   </div>
   <div class="frase">Mi coincidencia favorita eres tú. ❤️</div>`},

 { ico:"⏳", t:"Capítulo III", s:"El tiempo a tu lado", r:"Los días que llevamos juntos",
   html:()=>`
   <div class="pagina">
     <p>El tiempo pasa, los días cambian<br>y el universo sigue moviéndose…</p>
     <p>Pero hay algo que permanece:<br>las ganas de seguir compartiendo la vida contigo.</p>
   </div>
   <div class="num">
     <div class="dato"><b>${dias.toLocaleString("es-CO")}</b><span>días de nuestra historia</span></div>
     <div class="dos">
       <div class="dato"><b>${anios}</b><span>años juntos</span></div>
       <div class="dato"><b>${faltan===0?"¡Hoy!":faltan}</b><span>${faltan===0?"es nuestro aniversario":"días para el aniversario"}</span></div>
     </div>
   </div>
   <div class="frase">Y todavía nos quedan tantos momentos por vivir…</div>`},

 { ico:"📸", t:"Capítulo IV", s:"Pequeños instantes, grandes recuerdos", r:"Nuestro álbum",
   html:()=>`
   <div class="pagina"><p>Cada fotografía guarda un pedacito de lo que somos.<br>Quizás sean momentos sencillos,<br>pero contigo hasta lo más pequeño<br>se convierte en un recuerdo especial.</p></div>
   <div id="album"></div>`},

 { ico:"🎶", t:"Capítulo V", s:"Una canción, dos corazones", r:"Nuestra canción",
   html:()=>`
   <div class="emoji">🎶💜</div>
   <div class="pagina">
     <p>Hay canciones que se escuchan…<br>y hay canciones que se sienten.</p>
     <p>Para mí, ${CANCION.titulo} de ${CANCION.artista}<br>tiene un significado especial,<br>porque me recuerda a nosotros.</p>
     <p>Quiero que cada vez que la escuches<br>recuerdes que hay alguien que te quiere<br>y que elige seguir caminando a tu lado.</p>
   </div>
   <div class="frase">Nuestra canción: ${CANCION.titulo} ❤️</div>
   <audio controls src="${CANCION.archivo}"></audio>`},

 { ico:"💌", t:"Capítulo VI", s:"De Titi para mi amor", r:"Una carta para ti",
   html:()=>`
   <div class="emoji">💌</div>
   <div class="pagina">
     <p class="izq">Mi amor:</p>
     <p class="izq">No sé si existen palabras suficientes para explicarte lo importante que eres para mí.</p>
     <p class="izq">Gracias por cada sonrisa, por cada abrazo, por cada conversación, por cada momento y por permitirme compartir una parte de tu vida.</p>
     <p class="izq">Quiero seguir descubriendo el mundo contigo, celebrar tus alegrías, acompañarte en los días difíciles y crear recuerdos que algún día podamos mirar con una sonrisa.</p>
     <p class="izq">No te prometo que todos los días serán perfectos, pero sí quiero prometerte que mis ganas de construir algo bonito contigo son reales.</p>
     <p class="izq">Gracias por ser tú, por existir en mi universo y por hacer que mi vida tenga una estrella tan especial.</p>
     <p class="izq">Feliz aniversario${esAntes?" adelantado":""}, mi amor.</p>
     <p class="izq">Te quiero muchísimo.</p>
     <p class="izq">Con todo mi amor,<br><b>Tu Titi ❤️</b></p>
   </div>`},

 { ico:"✨", t:"Capítulo VII", s:"Lo mejor todavía nos espera", r:"Nuestro futuro",
   html:()=>`
   <div class="emoji">🌌💖✨</div>
   <div class="pagina">
     <p>Mi amor…</p>
     <p>Esta historia no termina aquí.</p>
     <p>Nos quedan lugares por conocer,<br>fotografías por tomar,<br>canciones por dedicar,<br>abrazos por compartir<br>y muchísimas razones para sonreír.</p>
     <p>Si el universo es infinito,<br>quiero que nuestra historia<br>tenga infinitas páginas.</p>
     <p>Gracias por ser parte de mi vida.<br>Gracias por ser mi persona especial.</p>
     <p>Y si tuviera que volver a comenzar,<br>volvería a elegirte a ti.</p>
   </div>
   ${galeria(7)}
   <div class="frase">Feliz segundo aniversario<br>09 · 11 · 2026<br>Te quiero, mi amor ❤️</div>
   <p class="sub">Con amor, tu Titi</p>
   <button class="btn centro" onclick="irIndice()">Volver a vivir nuestra historia ❤️</button>`}
];

/* ==========================================================
   3. FOTOS Y VISOR
   ========================================================== */
function figura(f, lista, i){
  return `<figure class="foto" tabindex="0" data-i="${i}" data-l="${lista}">
    <img src="${f.src}" alt="${f.nombre}" loading="lazy" onerror="this.closest('figure').remove()">
    <figcaption>${f.nombre}</figcaption></figure>`;
}
let visorLista = [], visorPos = 0;
function galeria(cap){
  const l = FOTOS.filter(f => f.cap.includes(cap));
  if(!l.length) return "";
  return `<div class="fotos" data-lista="cap${cap}">${l.map((f,i)=>figura(f,"cap"+cap,i)).join("")}</div>`;
}
function listaDe(id){
  if(id.startsWith("cap")) return FOTOS.filter(f=>f.cap.includes(+id.slice(3)));
  if(id==="album") return albumActual;
  return [];
}
let albumActual = [], albumTodas = false, albumCat = "Todas";
function pintarAlbum(){
  const cats = ["Todas", ...new Set(FOTOS.filter(f=>f.cap.includes(4)).map(f=>f.cat))];
  const base = FOTOS.filter(f=>f.cap.includes(4) && (albumCat==="Todas" || f.cat===albumCat));
  albumActual = albumTodas ? base : base.slice(0, FOTOS_VISIBLES_ALBUM);
  const el = document.getElementById("album");
  if(!base.length){ el.innerHTML = `<p class="sub">Aquí aparecerán nuestros recuerdos. Agrega tus fotos en la carpeta «fotos».</p>`; return; }
  el.innerHTML = `
    <div class="chips">${cats.map(c=>`<button class="chip ${c===albumCat?"on":""}" data-cat="${c}">${c}</button>`).join("")}</div>
    <div class="fotos">${albumActual.map((f,i)=>figura(f,"album",i)).join("")}</div>
    ${base.length>FOTOS_VISIBLES_ALBUM ? `<button class="btn suave centro" id="vermas">${albumTodas?"Ver menos":"Ver todas ("+base.length+")"}</button>`:""}`;
  el.querySelectorAll(".chip").forEach(b=>b.onclick=()=>{albumCat=b.dataset.cat;albumTodas=false;pintarAlbum();});
  const vm = document.getElementById("vermas"); if(vm) vm.onclick=()=>{albumTodas=!albumTodas;pintarAlbum();};
}
function abrirVisor(id,i){
  visorLista = listaDe(id); visorPos = i; mostrarVisor();
  document.getElementById("visor").classList.add("on");
}
function mostrarVisor(){
  const f = visorLista[visorPos]; if(!f) return;
  document.getElementById("visor-img").src = f.src;
  document.getElementById("visor-img").alt = f.nombre;
  document.getElementById("visor-nombre").textContent = f.nombre + "  (" + (visorPos+1) + "/" + visorLista.length + ")";
}
document.getElementById("v-ant").onclick=()=>{visorPos=(visorPos-1+visorLista.length)%visorLista.length;mostrarVisor();};
document.getElementById("v-sig").onclick=()=>{visorPos=(visorPos+1)%visorLista.length;mostrarVisor();};
document.getElementById("v-cerrar").onclick=()=>document.getElementById("visor").classList.remove("on");
document.addEventListener("click",e=>{
  const f = e.target.closest(".foto"); if(!f) return;
  const id = f.dataset.l; const vis = [...f.parentElement.querySelectorAll(".foto")];
  abrirVisor(id, vis.indexOf(f));
});
document.addEventListener("keydown",e=>{
  if(e.key==="Escape") document.getElementById("visor").classList.remove("on");
  if(document.getElementById("visor").classList.contains("on")){
    if(e.key==="ArrowRight") document.getElementById("v-sig").click();
    if(e.key==="ArrowLeft") document.getElementById("v-ant").click();
  } else if(e.key==="Enter" && document.activeElement.classList.contains("foto")) document.activeElement.click();
});

/* ==========================================================
   4. NAVEGACIÓN
   ========================================================== */
const vistas = {portada:"v-portada", indice:"v-indice", cap:"v-cap"};
let actual = 0;
function ver(v){
  Object.values(vistas).forEach(id=>document.getElementById(id).classList.remove("activa"));
  document.getElementById(vistas[v]).classList.add("activa");
  window.scrollTo({top:0});
}
function irIndice(){ ver("indice"); }
function irCap(n){
  actual = n; const c = CAPS[n];
  document.getElementById("migas").textContent = c.r;
  document.getElementById("cap-titulo").textContent = c.t;
  document.getElementById("cap-sub").textContent = c.s;
  document.getElementById("cap-cuerpo").innerHTML = c.html();
  if(n===3){ albumTodas=false; albumCat="Todas"; pintarAlbum(); }
  document.getElementById("prev").style.visibility = n>0 ? "visible":"hidden";
  document.getElementById("next").style.visibility = n<CAPS.length-1 ? "visible":"hidden";
  ver("cap");
}
document.getElementById("abrir").onclick = irIndice;
document.getElementById("idx").onclick = irIndice;
document.getElementById("prev").onclick = ()=>irCap(actual-1);
document.getElementById("next").onclick = ()=>irCap(actual+1);
document.getElementById("lista").innerHTML = CAPS.map((c,i)=>
  `<button class="cap-btn" onclick="irCap(${i})"><span class="ico">${c.ico}</span><div><b>${c.t} · ${c.s}</b><span>${c.r}</span></div></button>`).join("");

/* ==========================================================
   5. FONDO DE ESTRELLAS
   ========================================================== */
(function(){
  const cv = document.getElementById("estrellas"), cx = cv.getContext("2d");
  let W,H,S=[];
  function init(){
    W = cv.width = innerWidth; H = cv.height = innerHeight;
    S = Array.from({length:Math.min(140,Math.floor(W*H/9000))},()=>({x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.4+.3,p:Math.random()*6.3,v:Math.random()*.02+.005}));
  }
  const quieto = matchMedia("(prefers-reduced-motion:reduce)").matches;
  function dibujar(t){
    cx.clearRect(0,0,W,H);
    for(const s of S){
      const a = quieto ? .7 : .35 + .55*Math.abs(Math.sin(s.p + t*s.v*.1));
      cx.beginPath(); cx.arc(s.x,s.y,s.r,0,6.283); cx.fillStyle=`rgba(255,240,255,${a})`; cx.fill();
    }
    if(!quieto) requestAnimationFrame(dibujar);
  }
  addEventListener("resize",()=>{init();if(quieto)dibujar(0);});
  init(); requestAnimationFrame(dibujar);
})();
</script>
</body>
</html>