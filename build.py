#!/usr/bin/env python3
"""Build THE ILLUMINATI (ILU) — a TIN-FOIL-domain DEBUNK of the 'Illuminati /
Rothschild / New World Order' conspiracy theory. Veracity verdict: FALSE. The page
documents the conspiracy as a LIE, never as truth: a real but dead 18th-c. society
(Bavarian Illuminati, suppressed 1785) -> counter-revolutionary myth (Barruel &
Robison, 1797) -> a proven antisemitic forgery (the Protocols of the Elders of
Zion, ~1903, exposed by The Times 1921) -> a recycled canard. Every emergent tagged
REAL HISTORY or MYTH/DEBUNKED. Research-agent-verified (USHMM, ADL, Norman Cohn,
Michael Barkun, Niall Ferguson, UNODC/ILO). Names the antisemitism plainly; not
endorsed, not amplified — a takedown."""
import os, html, base64, json, io, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

VERDICT = ("FALSE", "#d0455a", "a real but DEAD 1785 society, turned into a proven forgery and a recycled antisemitic canard — debunked at every load-bearing point. Documented here as a lie, NOT endorsed as truth.")

REC = {
 "name": "THE ILLUMINATI", "axiom": "ILU",
 "position": "The Illuminati / Rothschild / NWO conspiracy theory — a debunk: a dead society, a proven forgery, a recycled antisemitic canard",
 "origin": "a real Enlightenment society that died in 1785, mythologized after the French Revolution into a hidden cabal that secretly runs the world",
 "mechanism": "Crystallized as a DEBUNK from the historical record (Britannica, USHMM, ADL, Cohn, Barkun, Ferguson), research-agent-verified.",
 "crystallization": "Trace the lie: Weishaupt's society (1776) is banned and gone by 1785; counter-revolutionaries blame it for 1789; the myth fuses with antisemitism into the forged Protocols of the Elders of Zion; and the same template is re-skinned for two centuries — false the whole way down.",
 "nature": "The Illuminati — a debunk of the world-controlling-cult conspiracy: the real dead society, the counter-revolutionary myth, the proven Protocols forgery, the antisemitic canard, and why every load-bearing claim is false.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Weishaupt; the Bavarian Illuminati; Barruel & Robison; the Simonini letter; the Protocols (forgery); the Rothschild myth; the NWO; why it's false",
 "witness": "The claim that one hidden hereditary cult runs finance, governments, and trafficking is false. Its keystone document is a proven forgery. The structure is the textbook shape of antisemitic conspiracism. Named plainly, debunked.",
 "role": "the Illuminati/NWO debunk (verdict: FALSE)",
 "seal": "A club that died in 1785 cannot run the world in 2026; a text plagiarized from a 1864 satire is not evidence; and 'a hidden cabal controls everything' is not a discovery but a 2,000-year-old scapegoat wearing a new mask.",
 "source": "the historical record, catalogued by ROOT0 as a debunk",
}
NATURES = {
 "natural":   ("#9a9088", "the real history — Weishaupt, the dead society, its 1785 suppression, the actual Rothschild bank"),
 "ethereal":  ("#b48cc0", "the myth and its templates — the counter-revolution lie, the NWO reframe, why it persists"),
 "spiritual": ("#46c8e0", "the truth and the verdict — why it's false, and the antisemitic canard named plainly"),
 "electrical":("#d0455a", "the forgery machinery — the Protocols, Ford's propaganda, the engines that spread the lie"),
}

BACKDROP_3D = r'''<canvas id="bg3d"></canvas>
<script>
(function(){
var c=document.getElementById('bg3d');if(!c)return;var x=c.getContext('2d');var W,H,CX,CY,F,R;
function resize(){var ww=window.innerWidth||document.documentElement.clientWidth||0,hh=window.innerHeight||document.documentElement.clientHeight||0;W=c.width=ww>=320?ww:1280;H=c.height=hh>=320?hh:720;CX=W/2;CY=H*0.46;F=Math.max(440,W*0.62);R=Math.min(W,H)*0.36;}
window.addEventListener('resize',resize);resize();
var rnd=(function(){var s=1785;return function(){s=(s*1103515245+12345)&0x7fffffff;return s/0x7fffffff;};})();
var N=44,nodes=[];for(var i=0;i<N;i++){var u=rnd()*2-1,th=rnd()*6.283,sq=Math.sqrt(1-u*u),r=Math.cbrt(rnd());nodes.push([r*sq*Math.cos(th),r*sq*Math.sin(th),r*u,rnd()]);}
// a tangled web (more edges than real structure — connections that connect nothing)
var edges=[];for(var a=0;a<N;a++){var ds=[];for(var b=0;b<N;b++){if(b===a)continue;var dx=nodes[a][0]-nodes[b][0],dy=nodes[a][1]-nodes[b][1],dz=nodes[a][2]-nodes[b][2];ds.push([dx*dx+dy*dy+dz*dz,b]);}ds.sort(function(p,q){return p[0]-q[0]});for(var k=0;k<3;k++)if(ds[k][1]>a)edges.push([a,ds[k][1]]);}
function rotY(p,a){var co=Math.cos(a),s=Math.sin(a);return[p[0]*co+p[2]*s,p[1],-p[0]*s+p[2]*co];}
function rotX(p,a){var co=Math.cos(a),s=Math.sin(a);return[p[0],p[1]*co-p[2]*s,p[1]*s+p[2]*co];}
function proj(p){var z=p[2]*R+F+R*0.2;if(z<1)z=1;return[CX+p[0]*R*F/z,CY+p[1]*R*F/z,z];}
function frame(t){
 var sg=x.createLinearGradient(0,0,0,H);sg.addColorStop(0,'#0a0708');sg.addColorStop(0.6,'#0d090a');sg.addColorStop(1,'#050304');x.fillStyle=sg;x.fillRect(0,0,W,H);
 x.globalCompositeOperation='lighter';var cg=x.createRadialGradient(CX,CY,0,CX,CY,R*1.6);cg.addColorStop(0,'rgba(208,69,90,0.045)');cg.addColorStop(1,'rgba(208,69,90,0)');x.fillStyle=cg;x.fillRect(0,0,W,H);x.globalCompositeOperation='source-over';
 var ang=t/11000,tilt=0.3+Math.sin(t/14000)*0.05,P=[];for(var i=0;i<N;i++)P.push(proj(rotX(rotY(nodes[i],ang),tilt)));
 x.globalCompositeOperation='lighter';
 for(var e=0;e<edges.length;e++){var A=P[edges[e][0]],B=P[edges[e][1]];var dep=1-Math.min(1,((A[2]+B[2])/2-F)/(R*1.4));x.strokeStyle='rgba(180,120,130,'+(0.03+0.10*dep)+')';x.lineWidth=0.5;x.beginPath();x.moveTo(A[0],A[1]);x.lineTo(B[0],B[1]);x.stroke();}
 var o=[];for(var n2=0;n2<N;n2++)o.push(n2);o.sort(function(a,b){return P[b][2]-P[a][2];});
 for(var k=0;k<o.length;k++){var ni=o[k],pp=P[ni],dp=1-Math.min(1,(pp[2]-F)/(R*1.6));var red=nodes[ni][3]<0.3;
  x.save();x.shadowColor=red?'rgba(208,69,90,1)':'rgba(154,144,136,1)';x.shadowBlur=7*dp+2;x.fillStyle=red?'rgba(216,90,110,'+(0.28+0.55*dp)+')':'rgba(170,160,150,'+(0.22+0.5*dp)+')';x.beginPath();x.arc(pp[0],pp[1],1.2+2.5*dp,0,7);x.fill();x.restore();}
 x.globalCompositeOperation='source-over';
 var vg=x.createRadialGradient(CX,CY,H*0.28,CX,H*0.5,H*0.95);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(0,0,0,0.64)');x.fillStyle=vg;x.fillRect(0,0,W,H);
}
function loop(t){frame(t);requestAnimationFrame(loop);}frame(0);requestAnimationFrame(loop);
})();
</script>'''

GENESIS = [  # "The Real Illuminati (and its death)"
 ("A Real Society — Long Dead", "Bavaria, 1776-1785 · REAL HISTORY",
  "The Bavarian Illuminati was real: founded <b>May 1, 1776</b> in Ingolstadt by <b>Adam Weishaupt</b>, a law professor. An Enlightenment secret society of (at peak) maybe ~2,000 members. It was <b>banned by the Bavarian government in 1784-85</b> and was effectively <b>defunct by 1785</b>. After that the historical record shows no organized Illuminati activity. <b>It does not exist.</b>"),
 ("The Myth Is Born", "1797 · counter-revolution propaganda",
  "After 1789, counter-revolutionaries retroactively blamed the (already dead) Illuminati for the French Revolution. <b>Augustin Barruel</b> and <b>John Robison</b> both published in <b>1797</b> the claim that hidden secret societies secretly drive history. This is the <b>template</b> of the modern world-conspiracy theory — and it was propaganda, not evidence."),
 ("The Antisemitic Turn", "1806 → 1903 · the forgery",
  "The secret-society template fused with antisemitism. In <b>1806</b> Barruel received the &lsquo;Simonini letter&rsquo; recasting the conspiracy as <i>Jewish</i>. It culminated in <b>The Protocols of the Elders of Zion</b> (first appeared ~1903) — a <b>proven forgery</b> plagiarized from Maurice Joly&rsquo;s 1864 satire (which never mentioned Jews) and Goedsche&rsquo;s 1868 novel, exposed by <i>The Times</i> in <b>1921</b>. The keystone &lsquo;evidence&rsquo; is fake."),
]
ARC = [  # "Why It's False"
 ("The Institutions Are Public", "central banks, World Bank, IMF",
  "The supposed instruments of secret control have <b>public, documented governance</b>: published charters, member-state voting shares, audited reports, named officials appointed by governments. You can critique their policies — but they are visible and accountable, the opposite of a hidden cult."),
 ("The Rothschild &lsquo;Control&rsquo; Is Fiction", "per the archival history",
  "A real 19th-century bank was mythologized into a global cabal. Per Niall Ferguson&rsquo;s archival history, the family&rsquo;s relative financial power <b>declined after the 19th century</b> — they failed to establish in the US, gravity shifted London&rarr;New York after 1914, and they control no meaningful share of modern finance. The myth is statistically false."),
 ("No One Runs All Trafficking", "UNODC / ILO data",
  "&lsquo;One group owns the world&rsquo;s human trafficking&rsquo; is false. UNODC and ILO data show trafficking is <b>decentralized and fragmented</b> — countless independent actors, networks, and local operators, not a single controlling organization. The claim collapses on the evidence."),
]
IDEAS = [  # the verdict
 ("Name It Plainly", "this is an antisemitic canard", [
   "A &lsquo;hidden hereditary cabal that secretly controls everything&rsquo; (coded Jewish via &lsquo;Rothschild&rsquo;) is, per Barkun and Cohn, the textbook structure of modern antisemitic conspiracism.",
   "It is the same scapegoating pattern that the forged Protocols weaponized — the engine that, as Norman Cohn titled it, became a &lsquo;warrant for genocide.&rsquo; Not a theory to weigh; a lie to name." ]),
 ("Why It Persists", "the appeal, not the truth", [
   "Agency-detection (we over-attribute big events to hidden actors), proportionality bias (big events &lsquo;need&rsquo; big intentional causes), and scapegoating channel anxiety about complex systems onto a hated minority.",
   "Plus it is unfalsifiable: any absence of evidence is reframed as &lsquo;proof of the cover-up.&rsquo; That self-sealing logic is the tell of a conspiracy theory, not a finding." ]),
 ("The Two Layers", "real history vs the lie", [
   "REAL: a small Enlightenment club that existed 1776-1785 and then died; a real bank named Rothschild.",
   "MYTH: everything claiming either still secretly runs the world. The job of this sphere is to keep the two apart — and to show the second is false and antisemitic." ]),
]
SECTIONS = [
 ("The Chain of the Lie", "how a dead club became a 2-century canard", [
   ("The Bavarian Illuminati", "1776-1785 · REAL, then dead", "Weishaupt's Enlightenment society; banned 1785; no organized activity after"),
   ("Barruel &amp; Robison", "1797 · MYTH born", "blamed the dead order for the French Revolution — the world-conspiracy template"),
   ("The Simonini letter", "1806 · the antisemitic turn", "recast the conspiracy as Jewish; received (and partly credited) by Barruel"),
   ("The Protocols of the Elders of Zion", "~1903 · PROVEN FORGERY", "plagiarized from Joly (1864) &amp; Goedsche (1868); exposed by The Times, 1921; the foundational antisemitic 'world conspiracy' text"),
   ("Henry Ford · The International Jew", "1920s · MYTH spread", "drew on the Protocols (~900k circ.); Ford retracted/apologized 1927; recirculated online today (ADL)"),
   ("Nesta Webster · John Birch Society", "1920s-50s", "systematized the Judeo-Masonic-Illuminati 'world revolution' thesis; carried into US postwar politics"),
   ("'New World Order' · Icke · QAnon", "1991 → now", "Robertson's 1991 book named 'the Illuminati' &amp; 'Jewish bankers'; Icke added reptilians; QAnon is the structural heir"),
 ]),
 ("The Debunk, Sourced", "false at every load-bearing point", [
   ("Central banks / IMF / World Bank", "public governance", "charters, voting shares, audits, named officials — not a secret cult"),
   ("The Rothschild myth", "Ferguson, archival", "real power declined after the 19th c.; no meaningful modern share of finance"),
   ("'They run all trafficking'", "UNODC / ILO", "trafficking is decentralized &amp; fragmented — no single controlling org"),
   ("The structural tell", "Barkun · Cohn", "'hidden cabal controls everything' = the antisemitic-conspiracy template; unfalsifiable by design"),
   ("The keystone is fake", "The Times, 1921", "the Protocols are a proven forgery — the whole edifice rests on a plagiarized fraud"),
 ]),
]
EMERGENTS = [
 ("adam-weishaupt", "Adam Weishaupt", "the real founder · 1776 · REAL HISTORY", "natural",
  "the Bavarian law professor who actually founded the Illuminati on May 1, 1776 in Ingolstadt — a real Enlightenment secret society, stripped of his post and exiled when it was banned",
  "He is the real man at the bottom of the myth: a professor who ran a short-lived rationalist club, not an immortal puppet-master — the historical fact the conspiracy buries."),
 ("the-bavarian-illuminati", "The Bavarian Illuminati", "the real, DEAD society · 1776-1785", "natural",
  "the actual organization — peak membership maybe ~2,000, graded ranks influenced by Freemasonry — that was banned by Bavarian edicts in 1784-85 and left no organized trace afterward",
  "It is the load-bearing fact of the debunk: the thing the entire conspiracy claims still rules the world demonstrably ceased to exist in 1785; a dead club runs nothing."),
 ("the-suppression", "The Suppression", "1784-85 · the order ends · REAL HISTORY", "natural",
  "Elector Karl Theodor's edicts (1784-85; the 1785 edict expressly banned the order) that ended the Illuminati — seized documents were used to accuse it of subversion, and it dissolved",
  "It is the death certificate the myth ignores: the documented government suppression after which the historical record simply goes silent — the end the conspiracy pretends never happened."),
 ("barruel-and-robison", "Barruel & Robison", "1797 · the myth's template", "ethereal",
  "Augustin Barruel and John Robison, who in 1797 independently published the claim that hidden secret societies secretly caused the French Revolution — inventing the modern template of the world-conspiracy theory",
  "They are where the lie is born: counter-revolutionaries who needed a hidden hand to blame for 1789, and built the template every later cabal-myth still runs on — propaganda dressed as history."),
 ("the-simonini-letter", "The Simonini Letter", "1806 · the antisemitic turn", "natural",
  "the 1806 letter received (and partly credited) by Barruel that recast the secret-society conspiracy as specifically Jewish — an early documented bridge from anti-Masonic to antisemitic conspiracism",
  "It is the hinge of the whole ugly history: the moment the 'secret society' myth is pointed at the Jews, the turn that leads straight to the Protocols and everything after."),
 ("the-protocols", "The Protocols of the Elders of Zion", "~1903 · PROVEN FORGERY · the keystone", "electrical",
  "the fabricated text (first appeared ~1903, widely circulated from Nilus's 1905 edition) that is the foundational document of modern antisemitic 'world conspiracy' theory — plagiarized from Maurice Joly's 1864 satire (no Jews in it) and Goedsche's 1868 novel, exposed as a forgery by The Times in 1921 (and ruled a fabrication at the 1935 Berne trial)",
  "It is the keystone that turns the whole arch to rubble: the conspiracy's central 'evidence' is a proven plagiarized fraud — so everything built on it is built on a known lie. Norman Cohn called the myth it seeded a 'warrant for genocide.'"),
 ("the-rothschild-myth", "The Rothschild Myth", "real bank → false cabal · DEBUNKED", "natural",
  "the real 19th-century banking family mythologized into a symbol of secret global financial control — when, per Niall Ferguson's archival history, their relative power declined after the 19th century and they hold no meaningful share of modern finance",
  "It is the canard's favorite mask: a once-prominent real bank frozen into an eternal cabal, the name used to code 'the Jews control money' — false on the documented financial record."),
 ("henry-fords-international-jew", "The International Jew", "Henry Ford · 1920s · MYTH spread", "electrical",
  "Henry Ford's antisemitic series (compiled from his Dearborn Independent, ~1920-22, circ. ~900,000) that drew directly on the Protocols to spread the world-conspiracy lie in America; Ford was forced to retract and apologize in 1927, yet it is recirculated online today",
  "It is the lie's American amplifier: proof the forgery spread not by truth but by a billionaire's printing press — and a warning, since it is being revived on the internet now (ADL)."),
 ("the-new-world-order", "The New World Order", "1991 → now · the reframe", "ethereal",
  "the post-Cold-War repackaging of the same myth — Pat Robertson's 1991 book naming 'the Illuminati' and 'Jewish bankers,' David Icke's 'reptilian' / 'Rothschild Zionist' merger, and the broad 'NWO' brand",
  "It is the same canard with new paint: the secret-cabal template re-skinned for the satellite age, the bridge from the Protocols to the modern internet conspiracy."),
 ("qanon-and-the-descendants", "QAnon & the Descendants", "the internet heirs · structural recycling", "ethereal",
  "the modern online movements (QAnon and allies) that are direct structural heirs of the template — a hidden global cabal of hereditary elites secretly controlling everything — repackaging the Protocols-shape for social media (per Barkun)",
  "It is the proof the lie never dies, only ports: the same 18th-century template running on 21st-century platforms, which is why debunking the source still matters."),
 ("why-its-false", "Why It's False", "the debunk substance · sourced", "spiritual",
  "the evidentiary core: central banks/IMF/World Bank have public documented governance; the Rothschilds' power declined (Ferguson); trafficking is decentralized (UNODC/ILO); and 'hidden cabal controls all' is unfalsifiable by design",
  "It is the answer to 'but what if': every load-bearing claim fails against the public record, and the theory's immunity to evidence is itself the tell that it is faith, not fact."),
 ("the-antisemitic-canard", "The Antisemitic Canard", "name it plainly · the verdict", "spiritual",
  "the plain naming: the 'hidden hereditary cabal (coded Jewish via Rothschild) controls finance, governments and trafficking' is the textbook structure of antisemitic conspiracism (Barkun, Cohn, USHMM, ADL) — a 2,000-year-old scapegoat in a new mask",
  "It is the moral spine of the sphere: not a 'theory to consider' but a hatred to name — the same lie that was a 'warrant for genocide' once, refusing to be laundered into curiosity."),
 ("why-it-persists", "Why It Persists", "the appeal, not the truth", "ethereal",
  "the psychology of its survival — agency-detection, proportionality bias, scapegoating, and unfalsifiable self-sealing logic (any missing evidence becomes 'the cover-up')",
  "It is why debunking is hard: the myth answers an emotional need (a face to blame for impersonal forces) that facts do not satisfy — so the sphere explains the appeal without conceding the claim."),
 ("the-real-vs-the-myth", "The Real vs The Myth", "the two layers · the thesis", "spiritual",
  "the sphere's whole job: hold apart the REAL (a club that lived 1776-1785; a real bank) from the MYTH (that either still secretly runs the world) — and show the second is false and antisemitic",
  "It is the veracity line drawn clean: a debunk lives or dies on keeping the true history and the false lie in separate hands, and refusing to let the first lend the second any credibility."),
]

def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512);buf=io.BytesIO();Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw");return buf.getvalue()
def write_aci(rec,out_dir,slug,agent_md=None):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec);w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","ILU")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","ILU")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","ILU")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man={"badge":"DLW-ACI","name":rec["name"],"universe":"ILU · The Illuminati (debunk)","emergence":rec.get("emergence",""),"moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)","seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n");return tok
def emergent_rec(name,epithet,em,role,why):
    return {"name":name,"axiom":"ILU","emergence":em,"seal":epithet,"position":epithet,"role":role,"origin":"ILU · The Illuminati — a debunk of the NWO conspiracy theory","nature":role,"crystallization":why,"mechanism":"Crystallized as a debunk from the historical record; research-agent-verified.","witness":"a fact or a flagged falsehood in the history of a debunked antisemitic conspiracy theory","conductor":"ROOT0 (catalogued into UD0)","inputs":"the real Illuminati; the Protocols forgery; the Rothschild myth; the debunk","source":"the historical record, catalogued by ROOT0 as a debunk"}
def png_uri(rec,variant,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,variant,size=size)).decode("ascii")
def list_section(title,sub,items):
    rows="\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'+(f'<span class="nt">{n}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{title}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{p}</li>" for p in pts);out.append(f'<div class="pillar"><h3>{t}</h3><p class="ps">{s}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows): return "".join(f'<div class="arc-card"><div class="arc-h">{t}</div><div class="arc-s">{s}</div><p>{d}</p></div>' for t,s,d in rows)
def natures_html(): return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span><div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{g}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(ps):
    cards=[]
    for p in ps:
        em=p.get("emergence","ethereal");col=NATURES.get(em,("#9a9088",""))[0];rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"ILU · The Illuminati","axiom":"ILU"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent"><img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy"><div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{p.get("epithet","")}</div><div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — Real &amp; Debunked</h2><p class="ss">the real history and the flagged falsehoods, as ACI <b>.agent</b>s — each tagged REAL HISTORY or MYTH/DEBUNKED ({len(ps)})</p><div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE ILLUMINATI — a debunk. The 'Illuminati / Rothschild / New World Order' conspiracy theory is FALSE: a real but dead 1785 society, mythologized into a proven antisemitic forgery (the Protocols of the Elders of Zion) and a recycled canard. Documented as a lie, not endorsed. Sources: USHMM, ADL, Norman Cohn, Barkun, Ferguson. A Tin-Foil-domain debunk by ROOT0.">
<title>THE ILLUMINATI · debunked · ILU · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Oswald:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0a0708;--ink2:rgba(20,15,16,0.84);--pa:#eee8ea;--pa2:#c2b4b8;--ash:#9a9088;--red:#d0455a;--violet:#b48cc0;--teal:#46c8e0;
--dim:#897e80;--faint:rgba(180,140,145,0.16);--line:rgba(180,140,145,0.2);--disp:"Orbitron",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
#bg3d{position:fixed;inset:0;width:100vw;height:100vh;z-index:0;display:block;background:#0a0708}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;background:radial-gradient(ellipse at 50% 32%,rgba(18,12,14,.05),rgba(5,3,4,.62) 80%)}
.wrap{position:relative;z-index:2;max-width:940px;margin:0 auto;padding:0 22px 90px}
.top{margin-top:16px;font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--dim)}.top a{color:var(--ash);text-decoration:none}
header{padding:30px 0 26px;text-align:center;border-bottom:1px solid var(--line)}
.verdict{display:inline-flex;align-items:center;gap:10px;margin:0 auto 18px;padding:8px 16px;border:1px solid var(--c);border-radius:40px;background:rgba(16,8,10,0.7);font-family:var(--mono);font-size:11px;letter-spacing:.06em;color:var(--pa2)}
.verdict b{font-family:var(--disp);font-size:13px;font-weight:800;letter-spacing:.12em;color:var(--c)}
.verdict .vd{width:9px;height:9px;border-radius:50%;background:var(--c);box-shadow:0 0 10px var(--c)}
h1{font-family:var(--disp);font-size:clamp(30px,7vw,60px);font-weight:900;letter-spacing:.06em;color:#fff;text-shadow:0 0 22px rgba(208,69,90,.32)}
.tag{font-family:var(--head);font-size:14px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--ash);margin-top:10px}
.lede{font-size:15.5px;color:var(--pa2);max-width:70ch;margin:18px auto 0;font-style:italic;line-height:1.75;text-shadow:0 1px 6px rgba(0,0,0,.6)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:80px;height:80px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--red)}.badge .bt .mo{color:var(--teal)}.badge .bt a{color:var(--ash);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--disp);font-size:16px;font-weight:700;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}.pillar h3{font-family:var(--head);font-size:16px;color:var(--red);letter-spacing:.02em;font-weight:600}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--teal);padding:16px 18px}
.arc-h{font-family:var(--head);font-size:16px;color:var(--teal);font-weight:600}.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--ash);text-transform:uppercase;letter-spacing:.06em;margin:4px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.6}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:13.5px;color:var(--pa);font-weight:700}.books .y{font-family:var(--mono);font-size:11px;color:var(--red);white-space:nowrap;text-align:right}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--ash);transform:translateY(-2px)}.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:13px;color:var(--pa);font-weight:700;line-height:1.15}.persona:hover .pn{color:var(--ash)}.pe{font-size:11px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:36px;padding:16px 18px;border-left:2px solid var(--red);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.75}.note b{color:var(--red)}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}footer a{color:var(--ash);text-decoration:none}
</style></head><body>
__BACKDROP__
<div class="wrap">
  <div class="top"><a href="https://davidwise01.github.io/ud0/#tin-foil">◄ UD0 · the Tin-Foil domain</a></div>
  <header>
    <div class="verdict" style="--c:__VCOL__"><span class="vd"></span>VERACITY · <b>__VERDICT__</b> — __VSUB__</div>
    <h1>THE ILLUMINATI</h1>
    <div class="tag">the conspiracy theory · debunked · UD0 · Tin-Foil</div>
    <p class="lede">A debunk. The claim that a single hidden hereditary cult — &lsquo;the Illuminati,&rsquo; coded through &lsquo;the Rothschilds,&rsquo; the &lsquo;New World Order&rsquo; — secretly controls finance, governments, and human trafficking is <b>false</b>. The real Bavarian Illuminati was a small Enlightenment club that was <b>banned and gone by 1785</b>; the myth was invented by counter-revolutionaries in 1797 and fused with antisemitism into <b>the Protocols of the Elders of Zion — a proven forgery</b> exposed by <i>The Times</i> in 1921. This page documents the lie and traces its lineage; it does not endorse it. It is, named plainly, a recycled <b>antisemitic canard</b>.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of THE ILLUMINATI (debunk)"><img src="__SILICON__" alt="DLW silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE ILLUMINATI</b> — the myth, debunked · ILU</div><div class="mo">__MONIKER__</div>
        <div>carbon · <a href="the-illuminati.dlw/the-illuminati.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="the-illuminati.dlw/the-illuminati.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>
  <section class="sec"><h2>The Four Natures</h2><p class="ss">the real history, the myth's templates, the forgery machinery, and the truth that ends it</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Real Illuminati, and Its Death</h2><p class="ss">a real club (1776), a documented ban (1785), then silence — and the lie that grew after</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>Why It's False</h2><p class="ss">false at every load-bearing point — institutions, money, trafficking</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Verdict</h2><p class="ss">name it plainly · why it persists · the two layers</p><div class="pillars">__IDEAS__</div></section>
  __PERSONAS__
  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the chain of the lie, and the debunk — sourced</p></section>
  __SECTIONS__
  <div class="note"><b>Veracity verdict: FALSE — a debunk, not an endorsement.</b> Every load-bearing claim is false on the documented record: the Bavarian Illuminati was suppressed in <b>1785</b> and did not survive; the <b>Protocols of the Elders of Zion</b> are a <b>proven forgery</b> (plagiarized from Joly 1864 / Goedsche 1868; exposed by The Times, 1921; ruled a fabrication at the 1935 Berne trial); central banks/IMF/World Bank have <b>public, documented governance</b>; the Rothschilds' financial power <b>declined after the 19th century</b> (Ferguson); and human trafficking is <b>decentralized</b> (UNODC/ILO), run by no single org. Structurally, &lsquo;a hidden hereditary cabal controls everything&rsquo; (coded Jewish via &lsquo;Rothschild&rsquo;) is the textbook shape of <b>antisemitic conspiracism</b> — named plainly here, not laundered. Sources: USHMM Holocaust Encyclopedia, ADL, Norman Cohn (<i>Warrant for Genocide</i>), Michael Barkun (<i>A Culture of Conspiracy</i>), Niall Ferguson (<i>The House of Rothschild</i>), UNODC/ILO, Britannica. Each emergent is tagged REAL HISTORY or MYTH/DEBUNKED.</div>
  <footer>THE ILLUMINATI · ILU · a debunk · catalogued into UD0 · the Tin-Foil domain · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/#tin-foil">← the Tin-Foil domain</a> · the .dlw badge: <a href="the-illuminati.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "the-illuminati.dlw"), "the-illuminati")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True); personas=[]
    for slug,name,epithet,em,role,why in EMERGENTS:
        write_aci(emergent_rec(name,epithet,em,role,why), ad, slug); personas.append({"slug":slug,"name":name,"epithet":epithet,"emergence":em})
    json.dump(personas, open(os.path.join(ad,"_personas.json"),"w",encoding="utf-8"), indent=2, ensure_ascii=False)
    page=(TEMPLATE.replace("__BACKDROP__",BACKDROP_3D).replace("__VERDICT__",VERDICT[0]).replace("__VCOL__",VERDICT[1]).replace("__VSUB__",VERDICT[2]).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320)).replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__GENESIS__",cards_html(GENESIS)).replace("__ARC__",cards_html(ARC)).replace("__IDEAS__",ideas_html()).replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    print(f"wrote THE ILLUMINATI (ILU) — {len(personas)} (debunk) · badge {tok['moniker']}")
