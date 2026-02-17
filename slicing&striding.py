Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#slicing
a = 'koushik'
a[0:3]
'kou'
a[3:7]
'shik'
a[:3]
'kou'
a[3:]
'shik'
b = 'simple is better than complex'
b[10:16]
'better'
b[22:29]
'complex'
b[0:6]
'simple'
c = 'beautiful is better than ugly'
c[0:9]
'beautiful'
c[13:19]
'better'
c[25:29]
'ugly'
d = 'work hard until you succeed'
d[-27:-23]
'work'
d[-17:-12]
'until'
d[-22:-18]
'hard'
d[-11:-8]
'you'
d[-7:0]
''
d[-7:]
'succeed'
e = 'vijayawada is a royal city'
e[-10:-5]
'royal'
e[-26:-16]
'vijayawada'
e[-4:]
'city'
#STRIDING
f = "cloud computing"
f[::]
'cloud computing'
f[::1]
'cloud computing'
f[::3]
'cucpi'
g = "data science"
g[::4]
'd e'
g[::2]
'dt cec'
g[::5]
'dsc'
>>> g[::8]
'de'
>>> g[1:8]
'ata sci'
>>> g[5:]
'science'
>>> g[3:9]
'a scie'
>>> g[4:10]
' scien'
>>> h =  'python course'
>>> h[2:12:3]
'tnos'
>>> h[5:12:4]
'nu'
>>> h[1:11:5]
'y '
>>> h[0:9:2]
'pto o'
>>> i = "machine learning"
>>> i[-1:-8:-2]
'gire'
>>> i[-2:-16:-5]
'nei'
>>> i[-4:-15:-2]
'naleic'
>>> i[-1:-12:-4]
'gr '
>>> i[-1::]
'g'
>>> i[::-1]
'gninrael enihcam'
>>> #in positive striding highest to lowest is not possible
