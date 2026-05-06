
Localització andorrana de Odoo
==============================

Localització andorrana de Odoo.

Per Batista10.

El manifest és a l'arrel del clon. Odoo usa el **nom de la carpeta** del mòdul com a nom tècnic: ha de ser vàlid (sense guions), p. ex. **`l10n_ad`**.

Clona amb nom explícit: `git clone <url> l10n_ad`

Al servidor, si la carpeta del repo és `l10n-andorra`, pots fer un enllaç simbòlic `l10n_ad` → aquesta carpeta dins del teu `addons_path`; Odoo el carregarà com a mòdul `l10n_ad`.
