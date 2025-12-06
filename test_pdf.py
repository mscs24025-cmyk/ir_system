import sys
print("Script started", file=sys.stderr)
sys.stderr.flush()

try:
    from fpdf import FPDF
    print("fpdf imported", file=sys.stderr)
    sys.stderr.flush()
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Hello World!')
    pdf.output('test_output.pdf')
    
    import os
    if os.path.exists('test_output.pdf'):
        print(f"SUCCESS: PDF created: test_output.pdf ({os.path.getsize('test_output.pdf')} bytes)")
    else:
        print("ERROR: PDF not created")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()

