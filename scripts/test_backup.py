"""Offline test: a fake Supabase on localhost; back up, then restore. Run: python3 scripts/test_backup.py"""
import http.server, json, os, subprocess, sys, tempfile, threading

DATA = {"invoices": [{"id": i, "n": "x"} for i in range(2350)], "leads": [{"id": 1}], "etf_prices": [{"id": 1}], "job_ranked": [{"id": 1}]}
POSTED = {}

class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, obj, code=200):
        b = json.dumps(obj).encode(); self.send_response(code); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.headers.get("apikey") != "k": return self._send({}, 401)
        if self.path == "/rest/v1/": return self._send({"definitions": {t: {} for t in DATA}})
        t = self.path.split("/rest/v1/")[1].split("?")[0]
        a, b = self.headers["Range"].split("-"); return self._send(DATA[t][int(a):int(b) + 1])
    def do_POST(self):
        t = self.path.split("/rest/v1/")[1]; POSTED.setdefault(t, []).extend(json.loads(self.rfile.read(int(self.headers["Content-Length"]))))
        self.send_response(201); self.send_header("Content-Length", "0"); self.end_headers()

srv = http.server.HTTPServer(("127.0.0.1", 0), H); threading.Thread(target=srv.serve_forever, daemon=True).start()
env = dict(os.environ, SUPABASE_URL=f"http://127.0.0.1:{srv.server_port}", SUPABASE_SERVICE_KEY="k")
d = tempfile.mkdtemp(); here = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, os.path.join(here, "backup_supabase.py"), d], env=env, check=True, capture_output=True)
files = sorted(os.listdir(d)); assert files == ["invoices.json", "leads.json", "manifest.json"], files   # etf_prices and views skipped
m = json.load(open(os.path.join(d, "manifest.json"))); assert m["rows"] == {"invoices": 2350, "leads": 1} and not m["failed"], m  # paging works
subprocess.run([sys.executable, os.path.join(here, "restore_supabase.py"), d, "invoices"], env=env, check=True, capture_output=True)
assert len(POSTED["invoices"]) == 2350 and "leads" not in POSTED
bad = subprocess.run([sys.executable, os.path.join(here, "backup_supabase.py"), d], env=dict(env, SUPABASE_SERVICE_KEY="wrong"), capture_output=True)
assert bad.returncode != 0                                       # a wrong key fails loudly
print("OK")
