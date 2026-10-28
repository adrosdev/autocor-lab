# Phase 1 — Python + REST (AUTOCOR 1.4, 1.6)

| Step | File | What it teaches |
|---|---|---|
| 1 | step01_plain_get.py | A REST call is text on the wire; Basic Auth is Base64, not encryption |
| 2 | step02_repetition.py | Each plain request rebuilds auth and opens a new TLS connection |
| 3 | step03_session.py | `Session` persists auth, headers, and the connection — measured 33% faster on 2 calls |
| 4 | step04_error_handling.py | 4xx is not a Python error; `raise_for_status`, typed exceptions, `timeout` |