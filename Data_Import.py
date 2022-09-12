from astropy.io import fits
from astropy.visualization import astropy_mpl_style
import matplotlib.pyplot as plt

plt.style.use(astropy_mpl_style)

def main():
  


  hdul =   fits.open('DATA/cleanimage.G10.99.SiO.12m.7m.combined.image.mom0.fits')

  hdul.info()
  hdr = hdul[0].header
  data = hdul[0].data
  
  print(f'Size: {data.size} \nShape: {data.shape} \nMin: {data.min()} \nMax: {data.max()}')

  ##print(f'Max Axis 1: {data.max(axis=3)} \nMin Axis1: {data.min(axis=3)}')
  data.reshape([512,512])
  plt.figure()
  plt.imshow(data, cmap = 'gray')
  plt.colorbar()

  
if __name__ == "__main__":
  main()