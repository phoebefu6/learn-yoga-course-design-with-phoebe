// Node runner: loads assets/yc-live.js (and yc-data.js) exactly as the browser does and prints the
// canon as JSON with sorted keys. Compare with: python3 materials/yc_reference.py --json
const path = require("path");
const repo = process.argv[2] || path.join(__dirname, "..");
const api = require(path.join(path.resolve(repo), "assets/yc-live.js"));
function sortKeys(v) {
  if (Array.isArray(v)) return v.map(sortKeys);
  if (v && typeof v === "object") { const o = {}; Object.keys(v).sort().forEach(k => { o[k] = sortKeys(v[k]); }); return o; }
  return v;
}
process.stdout.write(JSON.stringify(sortKeys(api.canon())));
