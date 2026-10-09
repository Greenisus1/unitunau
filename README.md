# Unitunau

Bounded offline Decimal length/mass/temperature converter. Python 3.9+, no dependencies. Published in a private GitHub repository. Download its ZIP while signed into the owner account, extract it and open a terminal inside the source folder. Not verified as store-installed.

```text
python3 unitunau.py
python3 -m unittest -v
bash app-store.sh install
bash app-store.sh run
```

Supported units (case-sensitive): length m/km/cm/mm, mass kg/g/mg, temperature C/F/K. Explicit from/to units, no inference. Decimal input up to 15 integer and 12 fractional digits, no exponent or nonfinite values. Negative length/mass rejected. Temperature below absolute zero rejected. No medical dosing, currency, volume, energy, rates, non-SI length/mass or compound units. q at value prompt exits; EOF/Ctrl-C exits.

Decimal local precision 40; repeating Fahrenheit fractions can round at 40 significant digits. Prints decimal form and rounding caveat, not measurement-precision/accuracy claims. Temperature formulas and SI prefixes are conventional fixed conversion arithmetic, not live prices. No network, saved data, exports, purchases or device control. Use only for ordinary educational/manual conversions, not safety-critical engineering or clinical calculations.

Temperature formulas source: https://www.nist.gov/pml/owm/si-units-temperature

16 tests cover factors, temperature points, negative/absolute-zero rules, dimensions, units, numeric bounds and unchanged Decimal context. Linux tested; Pi/non-Linux untested. Marker/version1.0.0 published.
SI prefixes source: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes

The current public-only Pi App Store cannot discover private repositories; authenticated store support is not verified.

Fullscreen update: Store interactive launch uses terminal-sized board cells or wrapped full-terminal utility input/results with PgUp/PgDn scrolling. Original core rules and direct CLI commands remain unchanged. Ctrl+C cancels utility entry, result Enter returns; no new dependency downloads. Linux PTY resize/restoration checked; physical Pi untested.
