SELECT *

FROM
user as u
LEFT JOIN
profile as p
ON u.profile_id = p.profile_id
LEFT JOIN
onboarding as o
ON u.onboarding_id = o.onboarding_id
LEFT JOIN
mobile as m
ON u.mobile_id = m.mobile_id
LEFT JOIN
account as a
ON u.account_id = a.account_id
LEFT JOIN
status as s
ON u.status_id = s.status_id
LEFT JOIN
debito as d
ON s.status_debito_id = d.status_debito_id
LEFT JOIN
carteiras_digitais as cd
ON s.status_cart_digital_id = cd.status_cart_digital_id
LEFT JOIN
cartao_de_credito as cc
ON s.status_cartao_de_credito_id.= cc.status_cartao_de_credito_id
LEFT JOIN
cash as cs
ON s.status_cash_id = cs.status_cash_id
LEFT JOIN
pix as pix
ON s.status_pix_id = pix.status_pix_id
