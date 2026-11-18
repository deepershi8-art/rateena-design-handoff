import numpy as np, scipy.signal as S, subprocess, os
SR=48000; rng=np.random.default_rng(7)
t=lambda d: np.arange(int(SR*d))/SR
def bp(x,lo,hi,o=2): return S.sosfilt(S.butter(o,[lo,hi],'band',fs=SR,output='sos'),x)
def lp(x,f,o=2): return S.sosfilt(S.butter(o,f,'low',fs=SR,output='sos'),x)
def hp(x,f,o=2): return S.sosfiltfilt(S.butter(o,f,'high',fs=SR,output='sos'),x)
def room(x,dur=0.12,mix=0.08,dec=0.04):
    n=t(dur); ir=rng.standard_normal(len(n))*np.exp(-n/dec); ir=lp(ir,5000); ir/=np.sqrt((ir**2).sum())
    return x+mix*S.fftconvolve(x,ir)[:len(x)]
def fin(x,length):
    y=np.zeros(int(SR*length)); y[:min(len(x),len(y))]=x[:len(y)]
    y=hp(y,35); y-=y.mean()
    fi=int(SR*0.0015); fo=int(SR*min(0.012,length*0.25))
    y[:fi]*=np.sin(np.linspace(0,np.pi/2,fi))**2; y[-fo:]*=np.cos(np.linspace(0,np.pi/2,fo))**2
    y[0]=y[-1]=0
    return y/np.abs(y).max()*10**(-6/20)
def env(n,a,d): return (1-np.exp(-n/a))*np.exp(-n/d)
def tone(f,d,a,dec,glide=0):
    n=t(d); ph=2*np.pi*np.cumsum(f*(1+glide*np.exp(-n/0.01)))/SR
    return np.sin(ph)*env(n,a,dec)
L=0.07
# tap A: soft felt click + warm 620 Hz body
n=t(L); click=bp(rng.standard_normal(len(n)),1800,4200)*env(n,0.0003,0.0035)*0.5
tapA=fin(room(lp(click,6000)+tone(620,L,0.0006,0.014,0.04)+0.6*tone(190,L,0.0012,0.012)+0.12*tone(1240,L,0.0004,0.006),0.06,0.06,0.015),0.065)
# tap B: small wooden block, inharmonic modes, darker
n=t(L); tk=bp(rng.standard_normal(len(n)),900,2600)*env(n,0.0002,0.002)*0.35
modes=sum(a*tone(f,L,0.0004,d) for f,a,d in [(480,1,0.018),(1310,.35,0.008),(2560,.15,0.004)])
tapB=fin(room(lp(tk+modes,5000),0.06,0.05,0.015),0.07)
# next A: soft two-note gold chime (E5 then B5), bell partials, short room
def bell(f,d,dec): 
    n=t(d); return sum(a*np.sin(2*np.pi*f*r*n+p)*env(n,0.002,dec*k) for r,a,k,p in [(1,1,1,0),(2.0,.18,.6,.3),(2.76,.07,.35,1.1),(0.5,.12,1.2,0)])
D=0.4; x=np.zeros(int(SR*D)); a=bell(659.25,D,0.11); b=bell(987.77,D-0.075,0.13)
x+=a*0.8; x[int(SR*0.075):]+=b[:len(x)-int(SR*0.075)]*0.7
nextA=fin(room(lp(x,7000),0.25,0.18,0.07),0.38)
# next B: airy swish, band-pass sweep, plus faint gold glint
D=0.32; n=t(D); no=rng.standard_normal(len(n)); out=np.zeros_like(no)
blk=256; fc=np.geomspace(700,3200,len(n)//blk+1); zi=None
sos0=S.butter(2,[500,900],'band',fs=SR,output='sos'); zi=np.zeros((sos0.shape[0],2))
for i in range(0,len(n),blk):
    f=fc[i//blk]; sos=S.butter(2,[f*0.6,f*1.5],'band',fs=SR,output='sos')
    out[i:i+blk],zi=S.sosfilt(sos,no[i:i+blk],zi=zi)
e=np.sin(np.pi*np.clip(n/0.24,0,1))**2*np.exp(-np.maximum(n-0.12,0)/0.08)
sw=lp(out*e,6000); gl=tone(1318.5,D,0.12,0.06)*0.06
gl=np.roll(gl,int(SR*0.1)); gl[:int(SR*0.1)]=0
nextB=fin(room(sw+gl,0.2,0.12,0.05),0.32)
# toggle: tiny tick
L=0.045; n=t(L)
tog=fin(room(bp(rng.standard_normal(len(n)),2500,6000)*env(n,0.0002,0.0015)*0.4+tone(1180,L,0.0004,0.006)+0.4*tone(590,L,0.0006,0.007),0.04,0.04,0.01),0.04)
os.makedirs("wav",exist_ok=True); os.makedirs("web",exist_ok=True)
sounds={"tap-A":tapA,"tap-B":tapB,"next-A":nextA,"next-B":nextB,"toggle":tog}
def wr(path,y):
    raw=path+".f32"; y.astype('<f4').tofile(raw)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","f32le","-ar",str(SR),"-ac","1","-i",raw,*args[path.split('.')[-1]],path],check=True); os.remove(raw)
args={"wav":["-c:a","pcm_s24le"],"mp3":["-c:a","libmp3lame","-b:a","128k"],"ogg":["-c:a","libvorbis","-q:a","5"]}
for k,y in sounds.items():
    for ext,d in (("wav","wav"),("mp3","web"),("ogg","web")): wr(f"{d}/{k}.{ext}",y)
    print(k,len(y)/SR*1000,"ms peak dB",20*np.log10(np.abs(y).max()),"dc",y.mean(),"edges",y[0],y[-1])
gap=np.zeros(int(SR*0.6)); sec=np.zeros(int(SR*1.2)); seq=[sec[:int(SR*.3)]]
for k in sounds: 
    for i in range(3): seq+= [sounds[k],gap]
    seq.append(sec)
wr("PREVIEW-all.mp3",np.concatenate(seq))
