import os,sys
import webbrowser
import config

mod = config.modelname


def write_html():
    """Creat the main html page hosting all sets of diagnostics"""
    pathname = os.path.dirname(sys.argv[0])
    basedir=os.path.abspath(pathname)+'/ARMDiag/'
    
    f = open(basedir+'html/ARM_diag.html','w')
    
    message = """<html>
    <head>
    <TITLE>ARM Diagnostics Plots</TITLE>
    </head>
    </table>
    </b></font>
    <p>
    <b>ARM Metrics and Diagnostics Package</b>
    <p>
    <b>Model: """+mod+"""</b>
    <hr noshade size=2 size="100%">
    <TABLE width='1550' >
    <TR>
    <TD>
      <TH ALIGN=left VALIGN=top>
      <font color=blue>Set</font>
      <font color=blue>Description</font><br>
    <p>
      <font color=red>1</font> <A HREF="AC_mean_amip_table.html">Tables</A> of DJF, MAM, JJA, SON and Annual Mean.<br>
    <p>
      <font color=red>2</font> <A HREF="AC_amip_line_taylorD.html">Line plots and Taylor diagrams</A> of Annual Cycle.<br>
    <p>
      <font color=red>3</font> <A HREF="AC_amip_contour.html">Contour and Vertical profiles</A> of Annual Cycle.<br>
    <p>
      <font color=red>4</font> <A HREF="DC_amip_line_harmonicD.html">Line and Harmonic Dail plots</A> of Diurnal Cycle.<br>
    <p>
      <font color=red>5</font> <A HREF="DC_amip_contour.html">Contour plots</A> of Diurnal Cycle.<br>
    <p>
      <font color=red>6</font> <A HREF="Daily_amip_PDF.html">Line plots</A> of Probability Density Function.<br>
    
    </Table>
     
    <p>
    <p>
    <Table>
    <em>Click on Plot Type</em></b><p>
      <A HREF="AC_amip_line_taylorD.html"><img src="../figures/AC_amip_pr.png"  border=1 hspace=3 alt="Set 1" width="150" height="150"></a>
      <A HREF="AC_amip_line_taylorD.html"><img src="../figures/AC_amip_taylorD_pr.png"  border=1 hspace=3 alt="Set 1" width="150" height="150"></a>
      <A HREF="AC_amip_contour.html"><img src="../figures/mod_cl_p_annual_cycle_clim.png"   border=1 hspace=3 alt="Set 3" width="150" height="150"></a>
      <A HREF="DC_amip_line.html"><img src="../figures/ANN_cl_p_diff.png "   border=1 hspace=3 alt="Set 3" width="150" height="150"></a>
      <A HREF="DC_amip_contour.html"><img src="../figures/obs_cl_p_diurnal_clim.png"   border=1 hspace=3 alt="Set 3" width="150" height="150"></a>
      <A HREF="Daily_amip_PDF.html"><img src="../figures/Daily_amip_pr_JJA_pdf1.png"   border=1 hspace=3 alt="Set 6" width="150" height="150"></a>
    
    </TH>
    </TD>
    
    </TR>
    </TABLE>
    
    </TD>
    <Table>
    <img src="../figures/ARM_logo.png" >
    </TABLE>
    
    
    </html>"""
    
    f.write(message)
    f.close()


