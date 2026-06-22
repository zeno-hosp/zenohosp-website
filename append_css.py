import os

css_path = '/Users/iniyananbu/Documents/Zeno Hosp Website/css/pages/why-us.css'

new_css = """
/* Founder Hero Styles */
.founder-hero {
    background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    position: relative;
    overflow: hidden;
}
.founder-hero::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%; width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(45,138,110,0.05) 0%, transparent 60%);
    z-index: 0;
}
.founder-hero .container {
    position: relative;
    z-index: 1;
}
.founder-badge {
    display: inline-block;
    background: rgba(45,138,110,0.1);
    color: #2D8A6E;
    padding: 6px 16px;
    border-radius: 100px;
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 24px;
    border: 1px solid rgba(45,138,110,0.2);
}
.glass-panel {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-radius: 24px;
    padding: 32px 48px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.04);
}

/* Dark Mode Pain Section */
.why-pain-section.dark-mode {
    background: #0a0a0a;
    color: #ffffff;
    border-bottom: 1px solid #222;
}
.why-pain-section.dark-mode h2 {
    color: #ffffff;
    margin-bottom: 12px;
}
.pain-subtitle {
    text-align: center;
    color: #a0a0a0;
    font-size: 1.1rem;
    max-width: 600px;
    margin: 0 auto 48px;
}
.why-pain-section.dark-mode .pain-card {
    background: #141414;
    border: 1px solid #2a2a2a;
    border-left: none;
    border-top: 3px solid #dc2626;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}
.why-pain-section.dark-mode .pain-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(220, 38, 38, 0.15);
    border-color: #3a3a3a;
    border-top-color: #ef4444;
}
.pain-icon {
    color: #dc2626;
    margin-bottom: 16px;
}
.why-pain-section.dark-mode .pain-card h4 {
    color: #f87171;
    font-size: 1.1rem;
    margin-bottom: 12px;
}
.why-pain-section.dark-mode .pain-card p {
    color: #a3a3a3;
    font-size: 0.95rem;
}

/* Bento Grid Differentiators */
.bento-section {
    background: #f8fafc;
}
.bento-grid {
    grid-template-columns: repeat(3, 1fr);
    grid-auto-rows: minmax(280px, auto);
}
.bento-wide {
    grid-column: span 2;
}
.bento-grid .diff-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.bento-grid .diff-card:hover {
    border-color: #cbd5e1;
    box-shadow: 0 20px 40px -10px rgba(0,0,0,0.08);
}
@media (max-width: 900px) {
    .bento-wide {
        grid-column: span 1;
    }
}
"""

with open(css_path, 'a') as f:
    f.write(new_css)
    
print("CSS appended successfully.")
