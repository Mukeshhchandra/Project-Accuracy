from pathlib import Path
import json,zipfile,hashlib
root=Path(__file__).resolve().parent.parent
out=root/'outputs'
names=['Accuracy.html','Open Accuracy.cmd','ACCURACY-READ-ME.md','ACCURACY-VALIDATION.md']
with zipfile.ZipFile(out/'Accuracy-local-review.zip','w',zipfile.ZIP_DEFLATED) as z:
    for name in names:
        path=out/name
        assert path.is_file()
        z.write(path,arcname='Accuracy/'+name)
audit=json.loads((root/'work/accuracy-audit.json').read_text())
manifest={name:{'bytes':(out/name).stat().st_size,
                'sha256':hashlib.sha256((out/name).read_bytes()).hexdigest()} for name in names}
(root/'work/review-package-manifest.json').write_text(json.dumps({'files':manifest,'bank':audit['bankSha256']},indent=2))
print(f"Packaged {len(names)} local files; no source PDFs, OCR corpus, credentials or saved student progress included.")
print(f"Archive: {out/'Accuracy-local-review.zip'} ({(out/'Accuracy-local-review.zip').stat().st_size:,} bytes)")
