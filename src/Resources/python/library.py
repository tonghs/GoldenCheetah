#
# Python class library loaded when the interpreter
# is installed by PythonEmbed

#--------------------------------------------------
# API for accessing GC data
#--------------------------------------------------

# basic activity data
def __GCactivity(join="repeat", activity=None):
   rd={}
   for x in range(0,GC.seriesLast()):
      if (GC.seriesPresent(x, activity)):
         rd[GC.seriesName(x)] = GC.series(x, activity)
   for name in GC.xdataNames("", activity):
      for serie in GC.xdataNames(name, activity):
         xd = GC.xdata(name, serie, join, activity)
         rd[str(xd)] = xd
   return rd

# xdata
def __GCactivityXdata(name="", activity=None):
   if not name:
      return GC.xdataNames("")
   rd={}
   for serie in GC.xdataNames(name, activity):
      xd = GC.xdataSeries(name, serie, activity)
      rd[str(xd)] = xd
   return rd

# setting up the chart
def __GCsetChart(title="",type=1,animate=False):
    GC.configChart(title,type,animate)

# add a curve
def __GCsetCurve(name="",x=list(),y=list(),xaxis="x",yaxis="y", labels=list(), colors=list(),line=1,symbol=0,size=15,color="cyan",opacity=0,opengl=True):
    if (name == ""):
       raise ValueError("curve 'name' must be set and unique.")
    GC.setCurve(name,list(x),list(y),xaxis,yaxis,list(labels),list(colors),line,symbol,size,color,opacity,opengl)

# add to main GC entrypoint
GC.activity=__GCactivity
GC.activityXdata=__GCactivityXdata
GC.setChart=__GCsetChart
GC.addCurve=__GCsetCurve

# constants

# 0 reserved for uninitialised
GC.CHART_LINE=1
GC.CHART_SCATTER=2
GC.CHART_BAR=3
GC.CHART_PIE=4

GC.SERIES_SECS = 0
GC.SERIES_CAD = 1
GC.SERIES_CADD = 2
GC.SERIES_HR = 3
GC.SERIES_HRD = 4
GC.SERIES_KM = 5
GC.SERIES_KPH = 6
GC.SERIES_KPHD = 7
GC.SERIES_NM = 8
GC.SERIES_NMD = 9
GC.SERIES_WATTS = 10
GC.SERIES_WATTSD = 11
GC.SERIES_ALT = 12
GC.SERIES_LON = 13
GC.SERIES_LAT = 14
GC.SERIES_HEADWIND = 15
GC.SERIES_SLOPE = 16
GC.SERIES_TEMP = 17
GC.SERIES_INTERVAL = 18
GC.SERIES_NP = 19
GC.SERIES_XPOWER = 20
GC.SERIES_VAM = 21
GC.SERIES_WATTSKG = 22
GC.SERIES_LRBALANCE = 23
GC.SERIES_LTE = 24
GC.SERIES_RTE = 25
GC.SERIES_LPS = 26
GC.SERIES_RPS = 27
GC.SERIES_APOWER = 28
GC.SERIES_WPRIME = 29
GC.SERIES_ATISS = 30
GC.SERIES_ANTISS = 31
GC.SERIES_SMO2 = 32
GC.SERIES_THB = 33
GC.SERIES_RVERT = 34
GC.SERIES_RCAD = 35
GC.SERIES_RCONTACT = 36
GC.SERIES_GEAR = 37
GC.SERIES_O2HB = 38
GC.SERIES_HHB = 39
GC.SERIES_RPCO = 40
GC.SERIES_LPPB = 41
GC.SERIES_RPPB = 42
GC.SERIES_LPPE = 43
GC.SERIES_RPPE = 44
GC.SERIES_LPPPB = 45
GC.SERIES_RPPPB = 46
GC.SERIES_LPPPE = 47
GC.SERIES_RPPPE = 48
GC.SERIES_WBAL = 49
GC.SERIES_TCORE = 50
GC.SERIES_CLENGTH = 51
GC.SERIES_APOWERKG = 52
GC.SERIES_INDEX = 53
GC.SERIES_HRV = 54
