from bokeh.events import DoubleTap
from bokeh.models.callbacks import CustomJS
import plotly.graph_objects as go

def get_favorite_color():
  return 'yellow'

# TODO: this is just while building the class. No need after move to a package.
#add_image_and_histo_method = MethodType(add_image_and_histo, Whiteboarder)
#@staticmethod
def image_small_bokeh(an_image, a_title):
  """an_image is a skimage gray image"""
  rgb = cv2.cvtColor(img_as_ubyte(an_image),cv2.COLOR_GRAY2RGB)
  rgba = cv2.cvtColor(rgb, cv2.COLOR_RGB2RGBA)
  rgba_flipped = rgba[::-1, :]

  p = bokeh.plotting.figure(plot_width=256, plot_height=160, tools='box_zoom', title=a_title)
  #img_plot.image(image=[grayed_image], x=[0], y=[0], dw=[1080], dh=[720]) #, palette="Spectral11", level="image")
  da_image = p.image_rgba(image=[rgba_flipped], x=[0], y=[0], dw=[1080], dh=[720]) #, palette="Spectral11", level="image"
  p.toolbar.logo = None
  p.toolbar_location = None
  p.xaxis.visible = False
  p.yaxis.visible = False
  p.x_range.range_padding = p.y_range.range_padding = 0
  #p.sizing_mode = 'stretch_both'
  return p
#Whiteboarder.image_small_bokeh = image_small_bokeh


def humanize_bytes(num, suffix='B'):
  """ Via # https://stackoverflow.com/a/1094933"""

  for unit in ['','K','M','G','T','P','E','Z']:
    if abs(num) < 1024.0:
      return "%3.1f%s%s" % (num, unit, suffix)
    num /= 1024.0
  return "%.1f %s%s" % (num, 'Yi', suffix)


def image_viewer_bokeh_large(an_rgb_image):
  """Input is an RGB image, not grayscale, not BRG"""

  #print(an_rgb_image.shape)

  p = bokeh.plotting.figure(plot_width=an_rgb_image.shape[1], plot_height=an_rgb_image.shape[0],
                            #title='Pixels by Intensity [by Bokeh]', 
                            #background_fill_color="#fafafa", 
                            x_range=(0,an_rgb_image.shape[1]), 
                            y_range=(0,an_rgb_image.shape[0]),
                            )#match_aspect=True)#,
                            #height_policy='min')
  
  # TODO: maintain aspect ratio in full-screen. Is this a bug in Plotly?
  # https://docs.bokeh.org/en/latest/docs/user_guide/layout.html#modes
  p.sizing_mode = 'scale_width'
  p.toolbar.logo = None

  #print(in_file_name)
  #logo_src = ColumnDataSource(dict(url = [in_file_name]))

  # grayed_flipped = grayed_image[::-1, :]
  # ready_to_go = img_as_ubyte(grayed_flipped)
  # works: p.image(image=[ready_to_go], x=[0], y=[0], dw=[1080], dh=[720]) #, palette="Spectral11", level="image")

  rgba = cv2.cvtColor(an_rgb_image, cv2.COLOR_RGB2RGBA)
  rgba_flipped = rgba[::-1, :]
  img_glyph = p.image_rgba(image=[rgba_flipped], x=[0], y=[0], dw=[an_rgb_image.shape[1]], dh=[an_rgb_image.shape[0]]) #, palette="Spectral11", level="image")
  return p # (p, img_glyph)


#TODO: The goal is have 256 pixels wide core, each bin gets a single pixel wide vertical line to work with. Success?
def gauge_small_bokeh(binned):
  """Returns a 200x124 pixel histogram. Param binned is the main output of 
     some histogramme; should be an array with len() == 256"""
  p = bokeh.plotting.figure(plot_width=256, plot_height=160, tools='box_zoom')
  p.toolbar.logo = None
  p.toolbar_location = None
  p.xaxis.visible = False
  p.yaxis.visible = False
  p.xgrid.grid_line_color = None
  p.ygrid.grid_line_color = None
  p.x_range.range_padding = p.y_range.range_padding = 0
  # This next sets a double tap on image to reset zoom and pan
  p.js_on_event(DoubleTap, CustomJS(args=dict(p=p), code='p.reset.emit()'))
  p.vbar(x=eight_bit_range, width=1.0, bottom=0,
         top=binned, color='#404040')
  return p


# TODO: Only PIL? Why? and why PIL at all?
def display_pil_image(image_to_show, scale_factor=1.0): 
  """
  A Colab image viewer. A resizable PIL image viewer (based on Plotly) with zoom and pan that works well in fullscreen mode on Colab 
  TODO: assumes PIL.Image
  """
  # TODO: want to set viewport dimensions to output cell, not image_to_show 

  # Create figure
  fig = go.Figure()
    
  # Constants
  # TODO: for skimage: (h, w, _) = image_to_show.shape 
  h, w = image_to_show.size
  img_width = h
  img_height = w

  #scale_factor = 0.15 
  # TODO: want scale_factor sensitive to cell/window width, else controls off screen to right.
  # There is also Colab API for checking and requesting output size. What about when in full screen; there is resize logic already

  # Add invisible scatter trace.
  # This trace is added to help the autoresize logic work.
  fig.add_trace(
    go.Scatter(
    x=[0, img_width * scale_factor],
    y=[0, img_height * scale_factor],
    mode="markers",
    marker_opacity=0
   )
  )
    
  # Configure axes
  fig.update_xaxes(
    visible=True,
    showgrid=False,
    range=[0, img_width] #range=[0, img_width * scale_factor]
  )
    
  fig.update_yaxes(
    visible=True,
    showgrid=False,
    range=[0, img_height],#range=[0, img_height * scale_factor],
    # the scaleanchor attribute ensures that the aspect ratio stays constant
    scaleanchor="x"
  )
    
  # Add image
  fig.update_layout(
    images=[go.layout.Image(
      x=0,
      sizex=img_width, # * scale_factor,
      y=img_height, # * scale_factor,
      sizey=img_height, # * scale_factor,
      xref="x",
      yref="y",
      opacity=1.0,
      layer="below",
      sizing="stretch",
      source=image_to_show)] #input_image)] # "https://raw.githubusercontent.com/michaelbabyn/plot_data/master/bridge.jpg")]
  )
    
  # Configure other layout
  fig.update_layout(
    width=img_width * scale_factor,
    height=img_height * scale_factor,
    margin={"l": 0, "r": 0, "t": 0, "b": 0},
  )
    
  fig.show()

    
