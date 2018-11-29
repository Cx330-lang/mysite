import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 三角波
def triangle_wave(size, T):
    t = np.linspace(-1, 1, size, endpoint=False)
    y = np.abs(t)
    y = np.tile(y, T) - 0.5
    x = np.linspace(0, 2*np.pi*T, size*T, endpoint=False)
    return x,y

if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    np.set_printoptions(suppress=True)


    x,y = triangle_wave(20,5)
    N = len(y)
    f = np.fft.fft(y)
    print("原始频域信号：", np.real(f), np.imag(f))
    a = np.abs(f/N)

    f_real = np.real(f)
    eps = 0.1*f_real.max()
    print(eps)
    f_real[(f_real < eps)&(f_real > -eps)] = 0
    f_imag = np.imag(f)
    eps1 = 0.1*f_imag.max()
    print(eps1)
    f_imag[(f_imag < eps)&(f_real > -eps)] = 0
    f1 = f_real +f_imag*1j
    y1 = np.fft.ifft(f1)
    y1 = np.real(y1)
    print("恢复频域信号：",np.real(f1),np.imag(f1))


    plt.figure(figsize=(8,8), facecolor='w')
    plt.subplot(311)
    plt.plot(x,y,'g-', lw=2)
    plt.title(u'三角波',fontsize=15)
    plt.grid(True)
    plt.subplot(312)
    w = np.arange(N) * 2*np.pi/N
    plt.stem(w, a, linefmt='r-',markfmt='ro')
    plt.title(u'频域信号',fontsize=15)
    plt.grid(True)
    plt.subplot(313)
    plt.plot(x, y1, 'b-', lw=2, markersize=4)
    plt.title(u'三角波恢复信号',fontsize=15)
    plt.grid()
    plt.tight_layout(1.5,rect=[0,0.04,1,0.96])
    plt.title('快速傅里叶变换FFT与频域滤波',fontsize=17)
    plt.show()