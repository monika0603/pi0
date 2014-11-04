import re
import datetime

def main():
    result=[]
    error=[]
    binContent=[]
    statError=[]
    
    result3040=[]
    error3040=[]
    binContent3040=[]
    statError3040=[]
    
    result05=[]
    error05=[]
    binContent05=[]
    statError05=[]
    
    filenameFigI = "ViscosityPLBPaperFig1.C"
    filenameFigII = "ViscosityPLBPaperFig2.C"
    
    with open(filenameFigI) as inputdata:
        lines = inputdata.read().splitlines()
        subset = lines[28:1144]
        subset1 = lines[1144:2260]
        subset2 = lines[2325:3441]
        subset3 = lines[3441:4557]
        subset4 = lines[4622:5738]
        subset5 = lines[5738:6854]
        
    for line in subset:
        result.append(re.findall("[-+]?[0-9]*\.?[0-9]+", line))

    for line1 in subset1:
        error.append(re.findall("[-+]?[0-9]*\.?[0-9]+", line1))

    for i in range(len(result)):
        binContent.append(','.join(map(str, result[i])))

    for j in range(len(error)):
        statError.append(','.join(map(str, error[j])))

    for line8 in subset2:
        result3040.append(re.findall("[-+]?[0-9]*\.?[0-9]+", line8))
        
    for line9 in subset3:
        error3040.append(re.findall("[-+]?[0-9]*\.?[0-9]+(?:[Ee]-\d+)?", line9))
        
    for x in range(len(result3040)):
        binContent3040.append(','.join(map(str, result3040[x])))
        
    for y in range(len(error3040)):
        statError3040.append(','.join(map(str, error3040[y])))

    print len(binContent3040)
    print binContent3040[0]
    print len(statError3040)
    print statError3040[0]

    for line10 in subset4:
        result05.append(re.findall("[-+]?[0-9]*\.?[0-9]+", line10))
        
    for line11 in subset5:
        error05.append(re.findall("[-+]?[0-9]*\.?[0-9]+(?:[Ee]-\d+)?", line11))
        
    for xx in range(len(result05)):
        binContent05.append(','.join(map(str, result05[xx])))
        
    for yy in range(len(error05)):
        statError05.append(','.join(map(str, error05[yy])))

    figureIIvalues=[]
    figureIIerror=[]
    cProjections=[]
    cProjError=[]
    with open(filenameFigII) as dataFigII:
        linesFigII = dataFigII.read().splitlines()
        subsetFigII = linesFigII[32:63]
        subset1FigII = linesFigII[63:94]
        subset3040FigII = linesFigII[284:315]
        subset30401FigII = linesFigII[315:346]
        subset05FigII = linesFigII[746:777]
        subset051FigII = linesFigII[777:808]

    for line2 in subsetFigII:
        figureIIvalues.append(re.findall("[-+]?[0-9]*\.?[0-9]+", line2))
        
    for line3 in subset1FigII:
        figureIIerror.append(re.findall("[-+]?[0-9]*\.?[0-9]+(?:[Ee]-\d+)?", line3))
        
    for id in range(len(figureIIvalues)):
        cProjections.append(','.join(map(str, figureIIvalues[id])))
        
    for jd in range(len(figureIIerror)):
        cProjError.append(','.join(map(str, figureIIerror[jd])))

    figureII3040values=[]
    figureII3040error=[]
    cProjections3040=[]
    cProjError3040=[]
    
    for line4 in subset3040FigII:
        figureII3040values.append(re.findall("[-+]?[0-9]*\.?[0-9]+", line4))
    
    for line5 in subset30401FigII:
        figureII3040error.append(re.findall("[-+]?[0-9]*\.?[0-9]+(?:[Ee]-\d+)?", line5))
    
    for c in range(len(figureII3040values)):
        cProjections3040.append(','.join(map(str, figureII3040values[c])))
    
    for cc in range(len(figureIIerror)):
        cProjError3040.append(','.join(map(str, figureII3040error[cc])))

    figureII05values=[]
    figureII05error=[]
    cProjections05=[]
    cProjError05=[]
    
    for line6 in subset05FigII:
        figureII05values.append(re.findall("[-+]?[0-9]*\.?[0-9]+", line6))
    
    for line7 in subset051FigII:
        figureII05error.append(re.findall("[-+]?[0-9]*\.?[0-9]+(?:[Ee]-\d+)?", line7))
    
    for f in range(len(figureII05values)):
        cProjections05.append(','.join(map(str, figureII05values[f])))
    
    for ff in range(len(figureIIerror)):
        cProjError05.append(','.join(map(str, figureII05error[ff])))


    constructDataPage(binContent,statError,binContent3040,statError3040,binContent05,statError05,cProjections,cProjError,cProjections3040,cProjError3040,cProjections05,cProjError05,'/Users/monikas/Sites/STARplbDataPoints/DataPoints1.html')

class Object(object):
    pass

def constructDataPage(result,error,binContent3040,statError3040,binContent05,statError05,cProjections,cProjError,cProjections3040,cProjError3040,cProjections05,cProjError05,outfile):

    html = open(outfile,'w')
    
    html.write('<html>\n')
    html.write('<head>\n')
    html.write('<title>Data Points</title>\n')
    html.write('<meta http-equiv="refresh" content="900">\n')
    html.write('</head>\n')
    
    html.write('<body>\n')
    html.write('Data point for STAR paper: Phys. Letts. B 704 (2011) 467-473 '+'<br /><br />\n')
    html.write('Page generated at: '+str(datetime.datetime.now())+'<br /><br />\n')

    html.write('Figure I:' + '<br /><br />\n')
    html.write('<table width="200" border="1">\n')
    html.write('<tbody><tr>\n')
    
    html.write('<table width="376" border="1">')
    html.write('<tbody>')
    html.write('<tr>')
    html.write('<td colspan="2">Centrality 70-80%</td>')
    html.write('</tr>')
    html.write('<td width="36">Bin number, value of C</td>')
    html.write('<td width="61">Bin number, Statistical error</td>')
    html.write('</tr>')
    
    for i in range(len(result)):
        html.write('<tr>')
        html.write('<td>')
        html.write(str(result[i]))
        html.write('</td>')
        html.write('<td>')
        html.write(str(error[i]))
        html.write('</td>')
        html.write('</tr>')

    html.write('</tr>')
    html.write('</tbody></table>\n')

    html.write('Figure I:' + '<br /><br />\n')
    html.write('<table width="200" border="1">\n')
    html.write('<tbody><tr>\n')
    
    html.write('<table width="376" border="1">')
    html.write('<tbody>')
    html.write('<tr>')
    html.write('<td colspan="2">Centrality 30-40%</td>')
    html.write('</tr>')
    html.write('<td width="36">Bin number, value of C</td>')
    html.write('<td width="61">Bin number, Statistical error</td>')
    html.write('</tr>')
    
    for t in range(len(binContent3040)):
        html.write('<tr>')
        html.write('<td>')
        html.write(str(binContent3040[t]))
        html.write('</td>')
        html.write('<td>')
        html.write(str(statError3040[t]))
        html.write('</td>')
        html.write('</tr>')
    
    html.write('</tr>')
    html.write('</tbody></table>\n')

    html.write('Figure I:' + '<br /><br />\n')
    html.write('<table width="200" border="1">\n')
    html.write('<tbody><tr>\n')
    
    html.write('<table width="376" border="1">')
    html.write('<tbody>')
    html.write('<tr>')
    html.write('<td colspan="2">Centrality 0-5%</td>')
    html.write('</tr>')
    html.write('<td width="36">Bin number, value of C</td>')
    html.write('<td width="61">Bin number, Statistical error</td>')
    html.write('</tr>')
    
    for t in range(len(binContent05)):
        html.write('<tr>')
        html.write('<td>')
        html.write(str(binContent05[t]))
        html.write('</td>')
        html.write('<td>')
        html.write(str(statError05[t]))
        html.write('</td>')
        html.write('</tr>')
    
    html.write('</tr>')
    html.write('</tbody></table>\n')

    html.write('Figure II:' + '<br /><br />\n')
    html.write('<table width="200" border="1">\n')
    html.write('<tbody><tr>\n')
    
    html.write('<table width="376" border="1">')
    html.write('<tbody>')
    html.write('<tr>')
    html.write('<td colspan="2">Centrality 70-80%</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td width="36">Bin number,  Projected value of C</td>')
    html.write('<td width="61">Bin number, Statistical error</td>')
    html.write('</tr>')
    
    for i in range(len(cProjections)):
        html.write('<tr>')
        html.write('<td>')
        html.write(str(cProjections[i]))
        html.write('</td>')
        html.write('<td>')
        html.write(str(cProjError[i]))
        html.write('</td>')
        html.write('</tr>')
    
    html.write('</tr>')
    html.write('</tbody></table>\n')

    html.write('Figure II:' + '<br /><br />\n')
    html.write('<table width="200" border="1">\n')
    html.write('<tbody><tr>\n')
    
    html.write('<table width="376" border="1">')
    html.write('<tbody>')
    html.write('<tr>')
    html.write('<td colspan="2">Centrality 30-40%</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td width="36">Bin number,  Projected value of C</td>')
    html.write('<td width="61">Bin number, Statistical error</td>')
    html.write('</tr>')
    
    for i in range(len(cProjections3040)):
        html.write('<tr>')
        html.write('<td>')
        html.write(str(cProjections3040[i]))
        html.write('</td>')
        html.write('<td>')
        html.write(str(cProjError3040[i]))
        html.write('</td>')
        html.write('</tr>')
    
    html.write('</tr>')
    html.write('</tbody></table>\n')

    html.write('Figure II:' + '<br /><br />\n')
    html.write('<table width="200" border="1">\n')
    html.write('<tbody><tr>\n')
    
    html.write('<table width="376" border="1">')
    html.write('<tbody>')
    html.write('<tr>')
    html.write('<td colspan="2">Centrality 0-5%</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td width="36">Bin number,  Projected value of C</td>')
    html.write('<td width="61">Bin number, Statistical error</td>')
    html.write('</tr>')
    
    for i in range(len(cProjections05)):
        html.write('<tr>')
        html.write('<td>')
        html.write(str(cProjections05[i]))
        html.write('</td>')
        html.write('<td>')
        html.write(str(cProjError05[i]))
        html.write('</td>')
        html.write('</tr>')
    
    html.write('</tr>')
    html.write('</tbody></table>\n')

    html.write('</head>\n')
    html.write('<body>\n')
    html.write('Figure III:' + '<br /><br />\n')
    html.write('<table width="376" border="1">')
    html.write('<tbody><tr>')
    html.write('<td width="36">Npart</td>')
    html.write('<td width="33">RMS</td>')
    html.write('<td width="61">Statistical error</td>')
    html.write('<td width="102">Systematic error</td>')
    html.write('<td width="110">Lower limit on RMS</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td>14.1</td>')
    html.write('<td>0.5356</td>')
    html.write('<td>0.01912449</td>')
    html.write('<td>0.0563473</td>')
    html.write('<td>0.5247</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td>27.4</td>')
    html.write('<td>0.547</td>')
    html.write('<td>0.01994727</td>')
    html.write('<td>0.0453415</td>')
    html.write('<td>0.5352</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td>47.8</td>')
    html.write('<td>0.5726</td>')
    html.write('<td>0.02185805</td>')
    html.write('<td>0.02643868</td>')
    html.write('<td>0.5421</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td>76.6</td>')
    html.write('<td>0.5868</td>')
    html.write('<td>0.02295562</td>')
    html.write('<td>0.03157727</td>')
    html.write('<td>0.5421</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td>115.5</td>')
    html.write('<td>0.6692</td>')
    html.write('<td>0.02985524</td>')
    html.write('<td>0.02360018</td>')
    html.write('<td>0.5981</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td>166.7</td>')
    html.write('<td>0.8399</td>')
    html.write('<td>0.0470288</td>')
    html.write('<td>0.03087939</td>')
    html.write('<td>0.668</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td>234.6</td>')
    html.write('<td>0.9309</td>')
    html.write('<td>0.05777165</td>')
    html.write('<td>0.07449698</td>')
    html.write('<td>0.7135</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td>299.3</td>')
    html.write('<td>0.9906</td>')
    html.write('<td>0.06541922</td>')
    html.write('<td>0.06304327</td>')
    html.write('<td>0.7345</td>')
    html.write('</tr>')
    html.write('<tr>')
    html.write('<td>352.4</td>')
    html.write('<td>0.9423</td>')
    html.write('<td>0.05919529</td>')
    html.write('<td>0.1654794</td>')
    html.write('<td>0.7345</td>')
    html.write('/tr>')
    html.write('</tbody></table>')
    
    html.close()

main()
