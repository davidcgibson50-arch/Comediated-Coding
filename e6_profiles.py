"""Analysis E6, part 1: profiles and departure order on the five AIM-AI v2 dimensions.
Input: data release 1 (AIM-AI_v081_all162_intended.csv, AIM-AI_v081_ENA_ready_intended_EOML.csv,
AIM-AI_v08_C12_Sweep_Log.csv), all in one folder.
Usage: python e6_profiles.py <input_folder> [<output_folder>]
"""
import itertools, json, sys
import numpy as np, pandas as pd

import os
IN = os.path.join(sys.argv[1] if len(sys.argv) > 1 else '.', '')
OUT = os.path.join(sys.argv[2] if len(sys.argv) > 2 else '.', '')
DIMS = ['I-D1', 'I-D2', 'I-D3', 'I-D4', 'I-D5']
NAMES = {'I-D1': 'Engagement', 'I-D2': 'Steering', 'I-D3': 'Provenance',
         'I-D4': 'Interpretation', 'I-D5': 'Positioning'}
CONF = ['AD', 'AS', 'CM', 'HD']

a = pd.read_csv(IN + 'AIM-AI_v081_all162_intended.csv')
e = pd.read_csv(IN + 'AIM-AI_v081_ENA_ready_intended_EOML.csv')
a = a.merge(e[['EpisodeID', 'Institution', 'EntryID', 'OriginalPass', 'EpisodeOrder']],
            left_on='Episode ID', right_on='EpisodeID', how='left')
L = a[a.Learner == 1].copy()
I = a[a.Learner == 0].copy()
out = {}

# --- 1. Distributions (Table 2)
tab = {}
for d in DIMS:
    vc = L[d].value_counts()
    coded = sum(vc.get(c, 0) for c in CONF)
    dep = coded - vc.get('HD', 0)
    tab[NAMES[d]] = {**{c: int(vc.get(c, 0)) for c in CONF + ['NE']},
                     'departs_pct': round(100 * dep / coded), 'coded': int(coded)}
out['table2'] = tab

# --- 2. Profiles
def profile(r): return tuple(r[d] for d in DIMS)
def configs(r): return {r[d] for d in DIMS if r[d] in CONF}
L['profile'] = L.apply(profile, axis=1)
L['nconf'] = L.apply(lambda r: len(configs(r)), axis=1)
L['mixed'] = L.nconf >= 2
out['mixed'] = int(L.mixed.sum()); out['n_learner'] = len(L)
out['distinct_profiles'] = int(L.profile.nunique())
mixcomp = L[L.mixed].apply(lambda r: '+'.join(sorted(configs(r))), axis=1).value_counts()
out['mixture_composition'] = mixcomp.to_dict()
uni = L[~L.mixed].apply(lambda r: ''.join(sorted(configs(r))) or 'none', axis=1).value_counts()
out['uniform_composition'] = uni.to_dict()
top = L.profile.value_counts().head(10)
out['top_profiles'] = [{'profile': dict(zip([NAMES[d] for d in DIMS], p)), 'n': int(n)} for p, n in top.items()]
out['top8_cover'] = int(top.head(8).sum())
both = L[L['I-D2'].isin(CONF) & L['I-D3'].isin(CONF)]
div = both[both['I-D2'] != both['I-D3']]
out['steer_prov_both_coded'] = len(both); out['steer_prov_diverge'] = len(div)
out['steerHD_provAI'] = int(((div['I-D2'] == 'HD') & div['I-D3'].isin(['AD', 'AS', 'CM'])).sum())
out['divergence_pairs'] = div.groupby(['I-D2', 'I-D3']).size().to_dict()
out['divergence_pairs'] = {f'{k[0]}/{k[1]}': int(v) for k, v in out['divergence_pairs'].items()}

# --- 3. Departure order (Guttman / Loevinger H), NE as missing
def dep_matrix(df, dims):
    M = pd.DataFrame({d: df[d].map(lambda v: np.nan if v not in CONF else (0 if v == 'HD' else 1)) for d in dims})
    return M

def loevinger(M):
    """Scale H from pairwise-complete item pairs; Guttman errors relative to item popularity."""
    items = list(M.columns)
    p = M.mean()
    obs = exp = 0.0
    pair = {}
    for i, j in itertools.combinations(items, 2):
        sub = M[[i, j]].dropna(); n = len(sub)
        if n == 0: continue
        pi, pj = sub[i].mean(), sub[j].mean()
        easy, hard = (i, j) if pi >= pj else (j, i)   # easy = more frequent departure
        e_obs = ((sub[hard] == 1) & (sub[easy] == 0)).sum()
        e_exp = n * (1 - sub[easy].mean()) * sub[hard].mean()
        obs += e_obs; exp += e_exp
        pair[f'{NAMES.get(hard, hard)} given {NAMES.get(easy, easy)}'] = {
            'hard_departs': int((sub[hard] == 1).sum()),
            'also_easy': int(((sub[hard] == 1) & (sub[easy] == 1)).sum()),
            'errors': int(e_obs), 'Hij': round(1 - e_obs / e_exp, 3) if e_exp > 0 else None}
    return 1 - obs / exp, pair

def reproducibility(M):
    """Goodenough-Edwards reproducibility: errors against the ideal pattern implied by each row's departure count; NE skipped."""
    order = M.mean().sort_values(ascending=False).index.tolist()
    err = cells = 0
    for _, r in M[order].iterrows():
        v = r.dropna(); k = len(v)
        if k == 0: continue
        cells += k
        x = v.values.astype(int); s = x.sum()
        ideal = np.array([1] * s + [0] * (k - s))
        err += int((x != ideal).sum())
    return 1 - err / cells, order

M5 = dep_matrix(L, DIMS)
H5, pairs5 = loevinger(M5); R5, order5 = reproducibility(M5)
out['scale5'] = {'H': round(H5, 3), 'Rep': round(R5, 3), 'order': [NAMES[d] for d in order5],
                 'departure_rates': {NAMES[d]: round(M5[d].mean(), 3) for d in DIMS}, 'pairs': pairs5}

# Four-dimension check (E5 counted once: IS departs if either component departs)
L4 = L.copy()
def is_dep(r):
    s, p = r['I-D2'], r['I-D3']
    vals = [v for v in (s, p) if v in CONF]
    if not vals: return 'NE'
    return 'AS' if any(v != 'HD' for v in vals) else 'HD'
L4['IS'] = L4.apply(is_dep, axis=1)
M4 = dep_matrix(L4, ['I-D1', 'IS', 'I-D4', 'I-D5'])
H4, _ = loevinger(M4); R4, _ = reproducibility(M4)
out['scale4_check'] = {'H': round(H4, 3), 'Rep': round(R4, 3)}

# Within collection
out['scale5_by_collection'] = {}
for inst, g in L.groupby('Institution'):
    h, _ = loevinger(dep_matrix(g, DIMS)); r, o = reproducibility(dep_matrix(g, DIMS))
    out['scale5_by_collection'][inst] = {'H': round(h, 3), 'Rep': round(r, 3), 'n': len(g)}

# Bootstrap: H and the order of the top items (steering vs interpretation), resampling entries
rng = np.random.default_rng(20261110)
entries = L.EntryID.unique()
Hs, steer_lowest, order_counts = [], 0, {}
B = 2000
for _ in range(B):
    samp = rng.choice(entries, len(entries), replace=True)
    g = pd.concat([L[L.EntryID == s] for s in samp])
    Mb = dep_matrix(g, DIMS)
    h, _ = loevinger(Mb); Hs.append(h)
    rates = Mb.mean()
    o = tuple(NAMES[d] for d in rates.sort_values(ascending=False).index)
    order_counts[o] = order_counts.get(o, 0) + 1
    if rates['I-D2'] < rates['I-D4']: steer_lowest += 1
out['bootstrap'] = {'B': B, 'H_ci': [round(np.percentile(Hs, 2.5), 3), round(np.percentile(Hs, 97.5), 3)],
                    'p_steering_departs_less_than_interpretation': round(steer_lowest / B, 3),
                    'top_orders': {' > '.join(k): v for k, v in sorted(order_counts.items(), key=lambda x: -x[1])[:4]}}

# Pre-sweep check: revert C12 sweep changes
sw = pd.read_csv(IN + 'AIM-AI_v08_C12_Sweep_Log.csv')
fmap = {'D1': 'I-D1', 'D2': 'I-D2', 'D3': 'I-D3', 'D4': 'I-D4', 'D5': 'I-D5'}
Lpre = L.set_index('Episode ID').copy()
nrev = 0
for _, r in sw.iterrows():
    f = fmap.get(str(r.Field))
    if f and r.EpisodeID in Lpre.index and Lpre.at[r.EpisodeID, f] == r.After:
        Lpre.at[r.EpisodeID, f] = r.Before; nrev += 1
Mp = dep_matrix(Lpre, DIMS); hp, _ = loevinger(Mp); rp, op = reproducibility(Mp)
Lpre['nconf'] = Lpre.apply(lambda r: len(configs(r)), axis=1)
out['pre_sweep'] = {'cells_reverted': nrev, 'H': round(hp, 3), 'Rep': round(rp, 3),
                    'order': [NAMES[d] for d in op], 'mixed': int((Lpre.nconf >= 2).sum())}

# Scale exceptions: episodes departing on a rarer dimension without departing on a commoner one
exc = []
ordr = order5
for _, r in L.iterrows():
    v = {d: (None if r[d] not in CONF else int(r[d] != 'HD')) for d in DIMS}
    for i, j in itertools.combinations(ordr, 2):   # i commoner, j rarer
        if v[i] == 0 and v[j] == 1:
            exc.append({'episode': r['Episode ID'], 'departs_on': NAMES[j], 'not_on': NAMES[i],
                        'profile': '/'.join(r[d] for d in DIMS)})
out['exceptions'] = pd.DataFrame(exc).groupby(['departs_on', 'not_on']).size().to_dict() if exc else {}
out['exceptions'] = {f'{k[0]} without {k[1]}': int(v) for k, v in out['exceptions'].items()}
pd.DataFrame(exc).to_csv(OUT + 'e6_scale_exceptions.csv', index=False)

# --- 4. Instructor episodes
I['nconf'] = I.apply(lambda r: len(configs(r)), axis=1)
out['instructor'] = {'n': len(I), 'mixed': int((I.nconf >= 2).sum()),
                     'pos_AS': int((I['I-D5'] == 'AS').sum()), 'steer_HD': int((I['I-D2'] == 'HD').sum()),
                     'any_CM': int(I[DIMS].isin(['CM']).any(axis=1).sum()),
                     'interp_NE': int((I['I-D4'] == 'NE').sum())}

json.dump(out, open(OUT + 'e6_profiles.json', 'w'), indent=1, default=str)
print(json.dumps({k: v for k, v in out.items() if k not in ('top_profiles',)}, indent=1, default=str))
