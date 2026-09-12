from pathlib import Path

root = Path(__file__).resolve().parents[1]
index_path = root / "index.html"
article_path = root / "blog" / "prix-catalogue-digital-menu-qr-cote-divoire" / "index.html"


def replace(path, old, new):
    text = path.read_text(encoding="utf-8")
    updated = text.replace(old, new)
    if updated != text:
        path.write_text(updated, encoding="utf-8")


replace(
    index_path,
    '<div class="value-step"><b><span class="old-price">15 000 F</span><strong>15 000 F promo + 4 900 F/mois</strong></b><span>Starter · Panier WhatsApp + 3 cartes QR</span></div>',
    '<div class="value-step"><b><strong>15 000 F + 4 900 F/mois</strong></b><span>Starter · Panier WhatsApp + 3 cartes QR</span></div>',
)
replace(
    index_path,
    '<div class="offer-price"><span class="old-price">15 000 F</span><span class="promo-price">15 000 F</span><span class="promo-label">Promo</span><small>installation promo + 4 900 F/mois</small></div>',
    '<div class="offer-price">15 000 F<small>installation + 4 900 F/mois</small></div>',
)
replace(index_path, 'Pack Starter — 15 000 F promo + 4 900 F/mois', 'Pack Starter — 15 000 F + 4 900 F/mois')
replace(index_path, 'Installation promo 15 000 F CFA puis abonnement 4 900 F CFA/mois.', 'Installation 15 000 F CFA puis abonnement 4 900 F CFA/mois.')
replace(
    index_path,
    'Promotion sur les frais d’installation : 15 000 F quel que soit le pack, puis l’abonnement mensuel correspondant pour maintenir le service et les fonctions associées.',
    'Le Pack Starter reste à 15 000 F d’installation. En promotion, les frais d’installation des Packs Pro et Business passent à 15 000 F, puis l’abonnement mensuel correspondant s’applique.',
)
replace(
    index_path,
    '<div class="lifetime-note"><span>Installation promo : 15 000 F sur les trois packs.</span> L’abonnement mensuel reste celui correspondant au pack choisi.</div>',
    '<div class="lifetime-note"><span>Starter : 15 000 F d’installation. Promo Pro & Business : 15 000 F d’installation.</span> L’abonnement mensuel reste celui correspondant au pack choisi.</div>',
)
replace(
    index_path,
    'Promotion actuelle sur l’installation : 15 000 F quel que soit le pack. Les abonnements mensuels restent à 4 900 F/mois pour Starter, 14 900 F/mois pour Pro et 29 900 F/mois pour Business.',
    'Le Starter reste à 15 000 F d’installation + 4 900 F/mois. En promotion, l’installation du Pro passe de 30 000 F à 15 000 F et celle du Business de 60 000 F à 15 000 F. Leurs abonnements restent respectivement à 14 900 F/mois et 29 900 F/mois.',
)

replace(
    article_path,
    'Promotion actuelle chez Digital ADN : 15 000 F CFA d’installation quel que soit le pack. Le Pack Starter est ensuite à 4 900 F CFA par mois.',
    'Chez Digital ADN, le Pack Starter reste à 15 000 F CFA d’installation puis 4 900 F CFA par mois. La promotion à 15 000 F d’installation concerne les Packs Pro et Business.',
)
replace(
    article_path,
    'Promotion actuelle : <strong>15 000 F CFA d’installation sur les trois packs</strong>. Le Starter est ensuite à <strong>4 900 F CFA/mois</strong>, le Pro à <strong>14 900 F/mois</strong> et le Business à <strong>29 900 F/mois</strong>.',
    'Le Starter reste à <strong>15 000 F CFA d’installation + 4 900 F CFA/mois</strong>. En promotion, l’installation du Pro passe de <strong>30 000 F à 15 000 F</strong> et celle du Business de <strong>60 000 F à 15 000 F</strong>. Leurs abonnements restent à <strong>14 900 F/mois</strong> et <strong>29 900 F/mois</strong>.',
)
replace(
    article_path,
    '<tr><td><strong>Starter</strong></td><td><del>15 000 F</del> <strong>15 000 F promo</strong></td><td>4 900 F/mois</td>',
    '<tr><td><strong>Starter</strong></td><td><strong>15 000 F</strong></td><td>4 900 F/mois</td>',
)
replace(
    article_path,
    'Son installation est actuellement en promotion à <strong>15 000 F CFA</strong> puis l’abonnement est de <strong>4 900 F CFA par mois</strong>.',
    'Son installation est de <strong>15 000 F CFA</strong> puis l’abonnement est de <strong>4 900 F CFA par mois</strong>.',
)
replace(
    article_path,
    'Promotion actuelle : 15 000 F CFA d’installation sur chacun des trois packs catalogue. Le Starter est ensuite à 4 900 F CFA par mois.',
    'Le Pack Starter reste à 15 000 F CFA d’installation puis 4 900 F CFA par mois. La promotion à 15 000 F d’installation concerne les Packs Pro et Business.',
)
