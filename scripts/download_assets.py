"""Copy the public SPYA assets locally before publishing. Uses macOS curl."""
import json
import subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
assets=json.loads((R/'data/assets.json').read_text())
failed=[]
for key,a in assets.items():
    dest=R/a['local'];dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists() and dest.stat().st_size>100:continue
    tmp=dest.with_suffix(dest.suffix+'.part')
    print('Downloading SPYA asset:',key,flush=True)
    result=subprocess.run(['curl','--fail','--location','--silent','--show-error','--connect-timeout','10','--max-time','35','--output',str(tmp),a['url']])
    valid=False
    if result.returncode==0 and tmp.exists():
        header=tmp.read_bytes()[:12]
        valid=header.startswith((b'\x89PNG\r\n\x1a\n',b'\xff\xd8\xff',b'GIF87a',b'GIF89a'))
    if valid:tmp.replace(dest)
    else:
        tmp.unlink(missing_ok=True);failed.append(key)
if failed:
    print('These assets will use their original SPYA image URLs:',', '.join(failed))
else:print('All SPYA images are stored locally.')
