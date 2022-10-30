from matplotlib import pyplot as plt

'''

    Function recieve Histogram and Title to plot respective histogram

    Autor: Miguel Ángel Hernández Tapia :)

'''

def histplot(hist, file_name, title='Histogram'):
    
  # CREATE FIGURE
  plt.figure(figsize = (10, 5))
  plt.title(title)                    # set title
  plt.xlabel("Intensidad")            # set label in y axis 
  plt.ylabel("Número de Pixeles")     # set label in x axis 

  # STEM PLOT
  markerline, stemlines, baseline = plt.stem(
    hist, linefmt ='orange', markerfmt =' ',
    bottom = 0, use_line_collection = True)

  # lines without top point color
  markerline.set_markerfacecolor('none')
  baseline.set_color('w')             

  # domain in x axis
  plt.xlim([0, 256])

  # save plot in a image
  plt.savefig(file_name + ".png", dpi=100)

  # show plot
  plt.show()