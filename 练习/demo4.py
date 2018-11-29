import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ =="__main__":
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    np.set_printoptions(suppress=True)

    x =np.linspace(0, 2*np.pi, 16, endpoint=False)
    print("时域采样值：",x)
    y = np.sin(2*x) + np.sin(3*x + np.pi/4)
    # y = np.sin(x)

    N = len(x)
    print("采样点个数：",N)
    print("原始信号：",y)
    f = np.fft.fft(y)
    print("频域信号：",f/N)
    a = np.abs(f/N)
    print("频率强度：", a)

    iy = np.fft.ifft(f)
    print("'逆傅里叶变换恢复信号:",iy)
    print("虚部：", np.imag(iy))
    print("实部：", np.real(iy))
    print("回复信号与原始信号是否相同：", np.allclose(np.real(iy),y))

    plt.subplot(211)
    plt.plot(x, y, 'go-', lw=2)
    plt.title(u'时域信号', fontsize=15)
    plt.grid(True)
    plt.subplot(212)
    w = np.arange(N)*2*np.pi/N
    print("频率采样值:",w)
    plt.stem(w,a, linefmt='r-',markfmt='ro')
    plt.title(u'频域信号', fontsize=15)
    plt.grid(True)
    plt.show()