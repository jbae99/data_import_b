from astropy.io import fits


def main():
  


  hdul =   fits.open('cleanimage.G10.99.SiO.12m.7m.combined.image.mom0.fits')

  hdul.info()
  
if __name__ == "__main__":
  main()