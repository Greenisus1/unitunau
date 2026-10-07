#!/usr/bin/env python3
"""Unitunau: bounded Decimal SI length/mass/temperature conversion."""
import decimal as d,re,sys
FACTORS={'m':('length','1'),'km':('length','1000'),'cm':('length','0.01'),'mm':('length','0.001'),'kg':('mass','1'),'g':('mass','0.001'),'mg':('mass','0.000001')}
TEMP=('C','F','K')
def number(text):
    text=text.strip()
    if not re.fullmatch(r'[+-]?\d{1,15}(?:\.\d{1,12})?',text,flags=re.ASCII):raise ValueError('Decimal only: up to 15 integer and 12 fractional digits, no exponents.')
    return d.Decimal(text)
def convert(text,source,target):
    value=number(text)
    with d.localcontext() as ctx:
        ctx.prec=40
        if source in FACTORS and target in FACTORS:
            if FACTORS[source][0]!=FACTORS[target][0]:raise ValueError('Units must share a dimension.')
            if value<0:raise ValueError('Length/mass cannot be negative.')
            result=value*d.Decimal(FACTORS[source][1])/d.Decimal(FACTORS[target][1])
        elif source in TEMP and target in TEMP:
            # Kelvin >=0; exact Decimal input and intermediate arithmetic.
            k=value if source=='K' else value+d.Decimal('273.15') if source=='C' else (value-d.Decimal(32))*d.Decimal(5)/d.Decimal(9)+d.Decimal('273.15')
            if k<0:raise ValueError('Below absolute zero.')
            result=k if target=='K' else k-d.Decimal('273.15') if target=='C' else (k-d.Decimal('273.15'))*d.Decimal(9)/d.Decimal(5)+d.Decimal(32)
        else:raise ValueError('Unknown units or mixed dimensions.')
        return format(result,'f')
def main():
    try:
        print('UNITUNAU | SI length/mass and C/F/K, Decimal precision 40, no medical/currency use');print('Units: m km cm mm / kg g mg / C F K');value=input('Value (q exits): ')
        if value.strip().lower()=='q':return 0
        source=input('From unit: ').strip();target=input('To unit: ').strip();print(convert(value,source,target),target)
        print('Repeating temperature fractions rounded to 40 significant digits; no measurement-accuracy claim.')
    except ValueError:print('Invalid number/units/dimension or below allowed physical range.',file=sys.stderr);return 2
    except (EOFError,KeyboardInterrupt):print('\nCancelled.')
    return 0
if __name__=='__main__':raise SystemExit(main())
