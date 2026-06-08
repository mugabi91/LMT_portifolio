css_sheet ="""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, stApp, [class*="css"]{
    font-family: 'Inter', sans-serif;
    scroll-behavior: smooth;
    height: 100%;
}



/* =====================================================
   BACKGROUND (LIGHT + PREMIUM GRADIENT)
===================================================== */

.stApp{
    background:
    radial-gradient(circle at top left, rgba(219,234,254,.9), transparent 40%),
    radial-gradient(circle at top right, rgba(237,233,254,.9), transparent 35%),
    linear-gradient(180deg, #fafafa, #f8fafc);
    
    background-color: #f8fafc;

    background-image: url("https://www.transparenttextures.com/patterns/cubes.png"),
        radial-gradient(circle at top left, rgba(219,234,254,.7), transparent 45%),
        radial-gradient(circle at top right, rgba(237,233,254,.7), transparent 40%);

    background-repeat: repeat, no-repeat, no-repeat;
    background-size: auto, cover, cover;
}

/* Hide Streamlit chrome */

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container{
    max-width: 1300px;
    padding-top: 1rem;
}

/* =====================================================
   DESKTOP NAVBAR (DEFAULT)
===================================================== */

.nav{
    display: flex !important;
    position: fixed;
    top: 16px;
    left: 50%;
    transform: translateX(-50%);

    width: min(92%, 900px);

    justify-content: space-between;
    align-items: center;
    gap: 12px;

    padding: 14px 20px;

    background: rgba(255,255,255,.35);
    backdrop-filter: blur(24px);

    border: 1px solid rgba(255,255,255,.8);
    border-radius: 999px;

    box-shadow: 0 10px 40px rgba(0,0,0,.05);

    z-index: 1000;

    box-sizing: border-box;
}

/* links */
.nav-links a {
    text-decoration: none;
    color: #334155;
    font-weight: 600;

    padding: 6px 12px;
    border-radius: 999px;

    transition: 0.2s ease;
}

/* hover */
.nav-links a:hover {
    background: rgba(37,99,235,0.10);
    color: #2563eb;
}

/* click feedback */
.nav-links a:active {
    transform: scale(0.96);
}

/* =====================================================
   HAMBURGER NAV (HIDDEN ON DESKTOP)
===================================================== */

/* container */
.hamburger-nav{
    display: none;
}

@media (max-width: 768px){

    .nav{
        display: none !important;
    }

    .hamburger-nav{
        display: block;
        position: fixed;
        top: 16px;
        left: 50%;
        transform: translateX(-50%);
        width: 92%;
        z-index: 1000;
    }

    .nav-bar{
        display: flex;
        justify-content: space-between;
        align-items: center;

        padding: 12px 16px;

        background: rgba(255,255,255,.45);
        backdrop-filter: blur(20px);

        border: 1px solid rgba(255,255,255,.8);
        border-radius: 999px;

        box-shadow: 0 10px 30px rgba(0,0,0,.08);

        position: relative;
        outline: none;
    }

    .hamburger{
        font-size: 24px;
        cursor: pointer;
        user-select: none;
    }

    /* hidden by default */
    .mobile-menu{
        display: none;

        position: absolute;
        top: 60px;
        left: 0;
        right: 0;

        flex-direction: column;
        gap: 8px;

        padding: 12px 16px;

        background: rgba(255,255,255,.65);
        backdrop-filter: blur(20px);

        border: 1px solid rgba(255,255,255,.8);
        border-radius: 16px;
    }

    /* MAGIC: open when navbar is clicked/focused */
    .nav-bar:focus-within .mobile-menu{
        display: flex;
    }

    .mobile-menu a{
        text-decoration: none;
        color: #0f172a;
        font-weight: 600;

        padding: 10px 12px;
        border-radius: 10px;
    }

    .mobile-menu a:hover{
        background: rgba(37,99,235,.10);
        color: #2563eb;
    }
}
/* =====================================================
   HERO (FULL SCREEN IMPACT)
===================================================== */

.hero{
    min-height: 90vh;  
    padding-top: 40px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    text-align: center;
}


.hero h1{
    font-size: clamp(2.5rem, 6vw, 4rem);
    line-height: .95;
    font-weight: 900;
    letter-spacing: -4px;
    color: #0f172a;

    margin-bottom: 20px;
    margin-top: 10px;  
}

.hero p{
    max-width: 750px;
    font-size: 1.25rem;
    line-height: 1.8;
    color: #64748b;
}

.cta{
    margin-top: 28px;
    padding: 16px 28px;
    background: #2563eb;
    color: white;
    border-radius: 999px;
    font-weight: 600;
}

.cta-btn{
    display: inline-block;

    padding: 10px 18px; 

    background: #2563eb;
    color: white;

    border-radius: 999px;

    font-weight: 600;
    font-size: 0.95rem;

    text-decoration: none;

    transition: 0.2s ease;
}

.cta-btn:hover{
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(37,99,235,0.25);
}
/* =====================================================
   GLASS
===================================================== */

.glass{
    background: rgba(255,255,255,.35);
    backdrop-filter: blur(24px);

    border: 1px solid rgba(255,255,255,.8);
    border-radius: 32px;

    box-shadow: 0 20px 60px rgba(0,0,0,.05);

    padding: 40px;
}

/* =====================================================
   SECTION TITLES
===================================================== */

.section-title{
    font-size: 3rem;
    font-weight: 800;
    color: #0f172a;
    margin-top: 40px;
    margin-bottom: 20px;
}

/* =====================================================
   FEATURED PROJECT
===================================================== */

.featured-title{
    font-size: 3.5rem;
    font-weight: 900;
    line-height: 1.05;
}

.featured-meta{
    margin-top: 20px;
    color: #64748b;
}

/* =====================================================
   PROJECT CARDS (ASYMMETRIC FEEL)
===================================================== */

.project-card{
    background: rgba(255,255,255,.45);
    backdrop-filter: blur(18px);

    border: 1px solid rgba(255,255,255,.8);
    border-radius: 24px;

    padding: 24px;

    transition: .3s;
    
    height: 220px;
    display: flex;
    flex-direction: column;

    box-sizing: border-box;
}

.project-card:hover{
    transform: translateY(-6px);
    box-shadow: 0 20px 50px rgba(37,99,235,.10);
}

.project-title{
    font-weight: 700;
    color: #0f172a;
    font-size: 1.2rem;
}

.project-desc{
    color: #64748b;
    margin-top: 10px;
    
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
/* =====================================================
    ABOUT
===================================================== */

.about{
    padding-top:10x;
    justify-content: center;
}

.about p{
    max-width: 850px;
    margin: 20px auto 0 auto;

    text-align: center;

    font-size: 1.1rem;
    line-height: 1.9;

    color: #64748b;
}


/* =====================================================
    METRICS
===================================================== */


.metrics-grid{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 20px;
}

/* tablet */
@media (max-width: 900px){
    .metrics-grid{
        grid-template-columns: repeat(2, 1fr);
    }
}

/* mobile */
@media (max-width: 600px){
    .metrics-grid{
        grid-template-columns: 1fr;
    }
}

/* keep your metric card safe */

.metric{
    background: rgba(255,255,255,.45);
    backdrop-filter: blur(18px);

    width: 100%;
    box-sizing: border-box;

    border: 1px solid rgba(255,255,255,.8);
    border-radius: 20px;

    padding: 18px 16px;   /* ↓ reduced */

    text-align: center;

    transition: .3s;

    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 4px;             /* ↓ tighter spacing */

    min-height: 120px;   /* prevents over-expansion */
}

/* number */
.metric-number{
    font-size: 2.4rem;   /* ↓ smaller but still dominant */
    font-weight: 900;
    color: #0f172a;
    line-height: 1;
    letter-spacing: -0.5px;
}

/* label */
.metric-label{
    font-size: 0.75rem;  /* dashboard style */
    font-weight: 600;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.12em;
}
/* =====================================================
   CONTACT
===================================================== */

.contact{
    text-align: center;
    margin-top: 140px;
    
}

.contact h2{
    font-size: 4rem;
    font-weight: 900;
    color: #0f172a;
    
    line-height: 1.05; 
    letter-spacing: -1px; 
    margin: 0;   
}

.contact p{
    color: #64748b;
    font-size: 1.2rem;
}

.contact-links{
    margin-top: 25px;
    display: flex;
    justify-content: center;
    gap: 20px;
}

.contact-links a{
    padding: 10px 18px;
    border-radius: 999px;

    background: rgba(255,255,255,.45);
    backdrop-filter: blur(18px);

    border: 1px solid rgba(255,255,255,.8);

    text-decoration: none;
    color: #0f172a;
    font-weight: 600;

    transition: 0.2s ease;
}

.contact-links a:hover{
    transform: translateY(-2px);
    background: rgba(37,99,235,.10);
    color: #2563eb;
}


/* =====================================================
   GEMINI-STYLE SAFE GLOW (STREAMLIT COMPATIBLE)
===================================================== */

.gemini-bg {
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    overflow: hidden;
}

/* shared glow base */
.gemini-glow {
    position: absolute;
    width: 650px;
    height: 650px;
    border-radius: 50%;

    filter: blur(140px);
    opacity: 0.55;

    animation: floatGlow 20s ease-in-out infinite,
               colorShift 12s ease-in-out infinite;
}

/* blue glow */
.g1 {
    top: -220px;
    left: -220px;
    background: rgba(37, 99, 235, 0.25);
}

/* purple glow */
.g2 {
    top: -250px;
    right: -220px;
    background: rgba(124, 58, 237, 0.22);
    animation-delay: -6s, -3s;
}

/* soft accent glow */
.g3 {
    bottom: -280px;
    left: 30%;
    background: rgba(236, 72, 153, 0.12);
    animation-delay: -12s, -6s;
}

/* movement animation */
@keyframes floatGlow {
    0% { transform: translate(0px, 0px) scale(1); }
    50% { transform: translate(90px, 60px) scale(1.15); }
    100% { transform: translate(0px, 0px) scale(1); }
}

/* =====================================================
   NEW: COLOR SHIFT (THIS IS THE GEMINI EFFECT)
===================================================== */

@keyframes colorShift {
    0% {
        filter: hue-rotate(0deg) blur(140px);
    }
    25% {
        filter: hue-rotate(20deg) blur(145px);
    }
    50% {
        filter: hue-rotate(-20deg) blur(135px);
    }
    75% {
        filter: hue-rotate(35deg) blur(150px);
    }
    100% {
        filter: hue-rotate(0deg) blur(140px);
    }
}

/* CRITICAL: keep Streamlit content above */
.block-container {
    position: relative;
    z-index: 2;
}


.page-content{
    animation: fadeIn 0.35s ease;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(10px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}


</style>
"""
    
    
    
    
#best colors  #042027