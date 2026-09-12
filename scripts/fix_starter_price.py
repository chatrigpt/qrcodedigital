from pathlib import Path

index_path = Path(__file__).resolve().parents[1] / "index.html"
text = index_path.read_text(encoding="utf-8")

text = text.replace(
    '<div class="value-step"><b><span class="old-price">15 000 F</span><strong>15 000 F promo + 4 900 F/mois</strong></b><span>Starter · Panier WhatsApp + 3 cartes QR</span></div>',
    '<div class="value-step"><b><strong>15 000 F + 4 900 F/mois</strong></b><span>Starter · Panier WhatsApp + 3 cartes QR</span></div>'
)
text = text.replace(
    '<div class="offer-price"><span class="old-price">15 000 F</span><span class="promo-price">15 000 F</span><span class="promo-label">Promo</span><small>installation promo + 4 900 F/mois</small></div>',
    '<div class="offer-price">15 000 F<small>installation + 4 900 F/mois</small></div>'
)
text = text.replace('Pack Starter — 15 000 F promo + 4 900 F/mois', 'Pack Starter — 15 000 F + 4 900 F/mois')
text = text.replace('Installation promo 15 000 F CFA puis abonnement 4 900 F CFA/mois.', 'Installation 15 000 F CFA puis abonnement 4 900 F CFA/mois.')

index_path.write_text(text, encoding="utf-8")
