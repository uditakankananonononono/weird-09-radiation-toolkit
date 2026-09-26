#!/usr/bin/env python3
"""Fetch W09 candidate-cluster ortholog sequences individually from NCBI protein
(accession-level provenance ledger, resumable). Supports the H4-redirect direction
(per-candidate ortholog sets across lineages) and the accession gate."""
import json, subprocess, time, hashlib, os, sys
os.makedirs('data/candidate_orthologs', exist_ok=True)
LEDGER = 'data/candidate_orthologs_ledger.json'
led = json.load(open(LEDGER)) if os.path.exists(LEDGER) else {}
members = json.load(open('/tmp/w09_cand_members.json'))
todo = []
for rep, ms in members.items():
    for m in ms:
        sp, acc = m.split('|', 1)
        if acc not in led:
            todo.append((rep, sp, acc))
print(f'{len(todo)} to fetch, {len(led)} already ledgered', flush=True)
n = 0
for rep, sp, acc in todo:
    for attempt in range(3):
        try:
            r = subprocess.run(['curl','-sf','--max-time','25',
                f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id={acc}&rettype=fasta&retmode=text'],
                capture_output=True, timeout=30)
            if r.returncode == 0 and r.stdout.startswith(b'>'):
                break
        except Exception:
            pass
        time.sleep(2 + attempt*2)
    else:
        led[acc] = {'rep': rep, 'species': sp, 'status': 'fetch_failed'}
        continue
    seq = r.stdout
    open(f'data/candidate_orthologs/{acc}.fa','wb').write(seq)
    led[acc] = {'rep': rep, 'species': sp, 'status': 'ok',
                'sha256': hashlib.sha256(seq).hexdigest(),
                'bytes': len(seq), 'source': 'ncbi_protein_efetch_fasta'}
    n += 1
    if n % 10 == 0:
        json.dump(led, open(LEDGER,'w'), indent=1)
        print(f'  {n} fetched', flush=True)
    time.sleep(1.3)
json.dump(led, open(LEDGER,'w'), indent=1)
ok = sum(1 for v in led.values() if v['status']=='ok')
fail = sum(1 for v in led.values() if v['status']!='ok')
print(f'DONE: {ok} ok, {fail} failed, ledger={LEDGER}')
