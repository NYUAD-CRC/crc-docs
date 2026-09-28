"""Generate research_plot.html (publication charts) from the CSV data files.

Run automatically by Sphinx (see conf.py), or by hand:

    python3 source/hpc/research/publication_stats.py

Counting rules
--------------
* Only CSV files that a research_*.rst page actually includes are counted.
* The year comes from the file name (``<dept>-<year>.csv``).
* A paper listed more than once -- under several departments, several
  years, or twice on the same page -- is counted ONCE in the yearly bars and the
  overall total (in the earliest year it is listed under).
* In the department pie chart a paper counts once for every department that
  lists it, so the slices can add up to slightly more than the total.
* CRC publications (data/crc.csv) are one list with a Year column instead of
  per-year files. ALL of them count toward the CRC total (shown separately in
  the chart title and as the CRC slice of the pie chart). A CRC paper that is
  ALSO listed under a department/center is not added again to the yearly bars
  or the overall total; a CRC paper that appears ONLY in the CRC list is added
  to its year and to the overall total.

Nothing needs editing here when publications are added: just add rows to the
CSV files and rebuild.
"""
import collections
import csv
import glob
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT = os.path.join(HERE, "research_plot.html")

# Display name and pie-chart order for each file prefix.
DEPARTMENTS = collections.OrderedDict([
    ("biology", "Biology"),
    ("cgsb", "CGSB"),
    ("chemistry", "Chemistry"),
    ("computer", "Computer Science"),
    ("access", "ACCESS"),
    ("engineering", "Engineering"),
    ("math", "Mathematics"),
    ("physics", "Physics"),
    ("nyu", "NYU NYU"),
    ("shanghai", "NYU Shanghai"),
    ("socialscience", "Social Science"),
    ("psychology", "Psychology"),
    ("crc", "CRC"),
    ("arts", "Arts & Humanities"),
])

# The *-pre2018.csv files do not record individual years. This is the
# historical 2013-2017 breakdown of those papers; any difference between this
# and the actual pre-2018 count is applied to 2017 (with a warning).
PRE2018_SPLIT = collections.OrderedDict([
    ("2013", 1), ("2014", 12), ("2015", 16), ("2016", 19), ("2017", 23),
])

LINK_RE = re.compile(r"^\s*`(.*)<([^<>]*)>`_\s*$", re.S)
DOI_RE = re.compile(r"(10\.\d{4,9}/[^\s?#&]+)", re.I)
FILE_RE = re.compile(r"^(?P<dept>[a-z]+)-(?P<year>\d{4}|pre2018)\.csv$")
CRC_FILE = "crc.csv"  # single list; year from its "Year" column (see above)


def _norm_title(title):
    title = unicodedata.normalize("NFKD", title).lower()
    return re.sub(r"[^a-z0-9]", "", title)


def _doi(url):
    m = DOI_RE.search(url or "")
    return m.group(1).lower().rstrip(".)") if m else None


def _included_files():
    """CSV file names referenced by the research_*.rst pages."""
    names = set()
    for rst in glob.glob(os.path.join(HERE, "research_*.rst")):
        with open(rst, encoding="utf-8") as fh:
            names.update(re.findall(r":file:\s*data/(\S+\.csv)", fh.read()))
    return names


def _read_csv(name):
    with open(os.path.join(DATA, name), encoding="utf-8-sig") as fh:
        return list(csv.reader(fh))


def _parse(cell):
    link = LINK_RE.match(cell)
    title, url = (link.group(1), link.group(2)) if link else (cell, "")
    return title.strip(), url


def _crc_entries():
    rows = _read_csv(CRC_FILE)
    header = [h.strip().lower() for h in rows[0]]
    ycol = header.index("year") if "year" in header else None
    entries = []
    for row in rows[1:]:
        if len(row) < 2 or not row[1].strip():
            continue
        title, url = _parse(row[1])
        year = row[ycol].strip() if ycol is not None and len(row) > ycol else ""
        if not re.match(r"^\d{4}$", year):
            print("publication_stats: CRC paper without a valid Year, not added"
                  " to the yearly bars: %s" % title[:80], file=sys.stderr)
            year = None
        entries.append({"dept": "crc", "year": year, "file": CRC_FILE,
                        "title": title, "key": _norm_title(title),
                        "doi": _doi(url)})
    return entries


def load_entries():
    entries = []
    for name in sorted(_included_files()):
        if name == CRC_FILE:
            entries.extend(_crc_entries())
            continue
        m = FILE_RE.match(name)
        if not m:
            print("publication_stats: skipping %s (not <dept>-<year>.csv)" % name,
                  file=sys.stderr)
            continue
        dept, year = m.group("dept"), m.group("year")
        if dept not in DEPARTMENTS:
            print("publication_stats: unknown department prefix %r in %s"
                  % (dept, name), file=sys.stderr)
        for row in _read_csv(name)[1:]:
            if len(row) < 2 or not row[1].strip():
                continue
            title, url = _parse(row[1])
            entries.append({"dept": dept, "year": year, "file": name,
                            "title": title, "key": _norm_title(title),
                            "doi": _doi(url)})
    return entries


def group_papers(entries):
    """Group entries that are the same paper (same title or same DOI)."""
    parent = list(range(len(entries)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    first = {}
    for i, e in enumerate(entries):
        for k in (("t", e["key"]), ("d", e["doi"])):
            if not k[1]:
                continue
            if k in first:
                parent[find(i)] = find(first[k])
            else:
                first[k] = i
    groups = collections.defaultdict(list)
    for i, e in enumerate(entries):
        groups[find(i)].append(e)
    return list(groups.values())


def _year_sort(y):
    return "0000" if y == "pre2018" else y


def compute():
    entries = load_entries()
    papers = group_papers(entries)

    per_year = collections.Counter()
    crc = {"total": 0, "unique": 0, "shared": 0}
    counted = 0
    for p in papers:
        depts = set(e["dept"] for e in p)
        if "crc" in depts:
            crc["total"] += 1
            if depts == {"crc"}:
                crc["unique"] += 1
            else:
                crc["shared"] += 1
        # Year: from the department listing; CRC's own year only for CRC-only papers.
        years = [e["year"] for e in p if e["dept"] != "crc"] or \
                [e["year"] for e in p if e["year"]]
        if not years:
            continue  # CRC-only paper with no year: cannot be placed
        per_year[min(years, key=_year_sort)] += 1
        counted += 1

    per_dept = collections.Counter()
    for p in papers:
        for d in set(e["dept"] for e in p):
            per_dept[d] += 1

    bars = collections.OrderedDict()
    pre = per_year.pop("pre2018", 0)
    split = collections.OrderedDict(PRE2018_SPLIT)
    diff = pre - sum(split.values())
    if diff:
        print("publication_stats: pre-2018 has %d papers but PRE2018_SPLIT sums"
              " to %d; adjusting 2017" % (pre, sum(split.values())),
              file=sys.stderr)
        split["2017"] += diff
    bars.update(split)
    for y in sorted(per_year):
        bars[y] = per_year[y]

    dups = [p for p in papers if len(p) > 1]
    return bars, per_dept, counted, len(entries), dups, crc


HTML = """<!-- GENERATED by publication_stats.py from data/*.csv on every build.
     Do not edit the numbers here by hand; edit the CSV files instead. -->
<html>
   <head>
      <title>Total HPC Publications</title>
      <script type = "text/javascript" src = "https://www.gstatic.com/charts/loader.js">
      </script>
      <script type = "text/javascript">
         google.charts.load('current', {{packages: ['corechart']}});
      </script>
   </head>

   <body>
      <div id = "container" style = "width: 700px; height: 400px; margin: 0 auto">
      </div>
      <script language = "JavaScript">
         function drawChart() {{
            // Define the chart to be drawn.
            var data = google.visualization.arrayToDataTable([
               ['Year', 'No. of Publications'],
{year_rows}
            ]);

            var options = {{title: 'Publications Per Year\\n\\nTotal Publications: {total}'}};

            // Instantiate and draw the chart.
            var chart = new google.visualization.ColumnChart(document.getElementById('container'));
            chart.draw(data, options);
         }}
         google.charts.setOnLoadCallback(drawChart);
      </script>
   </body>
</html>

<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {{'packages':['corechart']}});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {{

        var data = google.visualization.arrayToDataTable([
          ['Department', 'Publications'],
{dept_rows}
        ]);

        var options = {{
          title: 'Publications Per Department'
        }};

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }}
    </script>
  </head>
  <body>
    <div id="piechart" style="width: 700px; height: 400px;"></div>
  </body>
</html>
"""


def render():
    bars, per_dept, total, _, _, crc = compute()
    year_rows = ",\n".join("               ['%s', %d]" % (y, n)
                           for y, n in bars.items())
    dept_rows = ",\n".join("          ['%s', %d]" % (label.replace("'", "\\'"),
                                                     per_dept[key])
                           for key, label in DEPARTMENTS.items()
                           if per_dept.get(key))
    return HTML.format(year_rows=year_rows, dept_rows=dept_rows, total=total,
                       crc_total=crc["total"], crc_unique=crc["unique"],
                       crc_shared=crc["shared"])


def write():
    html = render()
    old = None
    if os.path.exists(OUT):
        with open(OUT, encoding="utf-8") as fh:
            old = fh.read()
    if html != old:  # avoid touching the file (and forcing rebuilds) needlessly
        with open(OUT, "w", encoding="utf-8") as fh:
            fh.write(html)


if __name__ == "__main__":
    bars, per_dept, total, n_entries, dups, crc = compute()
    write()
    print("Listed entries: %d   Unique papers: %d" % (n_entries, total))
    print("CRC: %(total)d total, %(unique)d CRC-only, %(shared)d also listed"
          " elsewhere" % crc)
    print("Per year: " + ", ".join("%s=%d" % kv for kv in bars.items()))
    print("Per department: " + ", ".join(
        "%s=%d" % (DEPARTMENTS.get(k, k), v) for k, v in sorted(per_dept.items())))
    if "-v" in sys.argv:
        print("\nPapers listed more than once:")
        for p in dups:
            print("  %s\n      %s" % (p[0]["title"][:90],
                                    ", ".join(e["file"] for e in p)))
